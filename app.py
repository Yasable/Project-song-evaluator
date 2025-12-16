from flask import Flask, render_template, request, redirect, url_for, flash
from werkzeug.utils import secure_filename
import os
# from models.database import db
from models.song import Song, db
from models.prediction import predict_song

UPLOAD_FOLDER = 'static/uploads'
ALLOWED_EXTENSIONS = {'mp3', 'wav'}

app = Flask(__name__)
app.config['SECRET_KEY'] = 'your-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///songs.db'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024  # 16 MB limit

db.init_app(app)

with app.app_context():
    db.create_all()

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

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

        # Проверка: есть ли уже запись в БД?
        existing = Song.query.filter_by(lyrics_url=lyrics_url).first()
        if existing and use_db:
            return redirect(url_for('result', id=existing.id))

        # Сохраняем файл
        filename = secure_filename(f"{artist}_{song_title}.{audio_file.filename.rsplit('.', 1)[1]}")
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        os.makedirs(app.config['UPLOAD_FOLDER'], exist_ok=True)
        audio_file.save(filepath)

        try:
            # Предсказание
            grades, final_score = predict_song(filepath, lyrics_url)
        except Exception as e:
            flash(f'Ошибка обработки: {str(e)}')
            return render_template('index.html')

        # Сохраняем в БД
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
        db.session.add(new_song)
        db.session.commit()

        return redirect(url_for('result', id=new_song.id))

    return render_template('index.html')


@app.route('/result/<int:id>')
def result(id):
    song = Song.query.get_or_404(id)
    grades = [song.grade_0, song.grade_1, song.grade_2, song.grade_3, song.grade_4]
    return render_template('result.html', song=song, grades=grades)


if __name__ == '__main__':
    app.run(debug=True)

# строка необходимая для merge