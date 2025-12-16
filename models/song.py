from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Song(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    artist = db.Column(db.String(100), nullable=False)
    lyrics_url = db.Column(db.String(255), unique=True, nullable=False)
    grade_0 = db.Column(db.Integer)
    grade_1 = db.Column(db.Integer)
    grade_2 = db.Column(db.Integer)
    grade_3 = db.Column(db.Integer)
    grade_4 = db.Column(db.Integer)
    final_score = db.Column(db.Float)

    def __repr__(self):
        return f'<Song {self.artist} - {self.title}>'