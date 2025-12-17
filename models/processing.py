import numpy as np

from processing_dataset.audio_processing.mfccs import extract_mfccs_from_mp3
from processing_dataset.text_processing.embendding import lyric_embedding
from parser.parsers.genius_parser import get_lyrics

def calculation_features(song_path: str, song_url: str):
    audio_features = extract_mfccs_from_mp3(song_path)
    text_features = lyric_embedding(get_lyrics(song_url))

    features = np.hstack((audio_features, text_features))
    return features