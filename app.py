from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
from models.prediction import predict_song
from sqlalchemy import create_engine, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker, declarative_base
from contextlib import contextmanager

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}
DATABASE_URL = 'sqlite:///songs.db'

Base = declarative_base()
engine = create_engine(DATABASE_URL, echo=False)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

class Song(Base):
    __tablename__ = 'songs'
    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(100), nullable=False)
    artist = Column(String(100), nullable=False)
    lyrics_url = Column(String(255), unique=True, nullable=False)
    grade_0 = Column(Integer)
    grade_1 = Column(Integer)
    grade_2 = Column(Integer)
    grade_3 = Column(Integer)
    grade_4 = Column(Integer)
    final_score = Column(Integer)

Base.metadata.create_all(bind=engine)

@contextmanager
def get_db():
    session = SessionLocal()
    try:
        yield session
        session.commit()
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        song_title = request.form['song_title'].strip()
        artist = request.form['artist'].strip()
        lyrics_url = request.form['lyrics_url'].strip()
        use_db = 'use_db' in request.form
        audio_file = request.files['audio_file']

        if not (song_title and artist and lyrics_url and audio_file and allowed_file(audio_file.filename)):
            flash('Пожалуйста, заполните все поля и загрузите корректный аудиофайл (mp3/wav).')
            return render_template('index.html')

        ext = audio_file.filename.rsplit('.', 1)[1].lower()
        filename = secure_filename(f"{artist}_{song_title}.{ext}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        audio_file.save(filepath)

        with get_db() as db:
            existing = db.query(Song).filter(Song.lyrics_url == lyrics_url).first()

            if existing and use_db:
                return redirect(url_for('result', id=existing.id))

            try:
                grades, final_score = predict_song(filepath, lyrics_url)
            except Exception as e:
                flash(f'Ошибка обработки: {str(e)}')
                return render_template('index.html')

            if existing:
                existing.title = song_title
                existing.artist = artist
                existing.grade_0 = int(grades[0])
                existing.grade_1 = int(grades[1])
                existing.grade_2 = int(grades[2])
                existing.grade_3 = int(grades[3])
                existing.grade_4 = int(grades[4])
                existing.final_score = final_score
                song_id = existing.id       
            else:
                new_song = Song(
                    title=song_title,
                    artist=artist,
                    lyrics_url=lyrics_url,
                    grade_0=int(grades[0]),
                    grade_1=int(grades[1]),
                    grade_2=int(grades[2]),
                    grade_3=int(grades[3]),
                    grade_4=int(grades[4]),
                    final_score=final_score
                )
                db.add(new_song)
                db.flush()
                song_id = new_song.id

        return redirect(url_for('result', id=song_id))

    return render_template('index.html')

@app.route('/result/<int:id>')
def result(id):
    session = SessionLocal()
    try:
        song = session.query(Song).filter(Song.id == id).first()
        if not song:
            flash('Запись не найдена.')
            return redirect(url_for('index'))
        grades = [song.grade_0, song.grade_1, song.grade_2, song.grade_3, song.grade_4]
        return render_template('result.html', song=song, grades=grades, final_score=song.final_score)
    finally:
        session.close()

if __name__ == '__main__':
    app.run(debug=True)

