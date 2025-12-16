import numpy as np
from models.main import load_model
from models.processing import calculation_features
from processing_dataset.utils.data_processing import final_score

_model, _scaler = load_model()

def predict_song(song_path: str, lyrics_url: str):
    features = calculation_features(song_path, lyrics_url)
    features = features.reshape(1, -1)
    features = _scaler.transform(features)
    pred = _model.predict(features)[0]
    grades = np.round(pred).astype(int)
    final_score = final_score(grades)
    return grades, final_score