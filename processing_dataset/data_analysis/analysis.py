import numpy as np
import os
import matplotlib.pyplot as plt

from utils.file_io import load_data_from_npz
from utils.data_processing import normalization_features
from config_dataset import FEATURES_TAGS, LABELS_NAME

from data_analysis.grades_analysis import grade_analysis, grade_mean_analysis, grade_std_analysis, final_grade_analysis
from data_analysis.text_features_analysis import text_embedding_analysis
from data_analysis.audio_features_analysis import (mfccs_analisys, mfcc_mean_std_analysis,
                                                   values_audio_features, chroma_analisys,
                                                   chroma_mean_analisys, chroma_std_analisys)

from data_analysis.correlation_analysis import (correlation_features_grade_mean,
                                                correlation_features_grade_std,
                                                correlation_features_grade)
# def analysis():
    # pass
    # data = load_data_from_csv()

    # grades_dict = {
    #     "grades": [],
    #     "grades_mean": [],
    #     "grades_std": [],
    # }

    # audio_features = []

    # # print(data)
    # for i in range(1, 6):
    #     grades = []
    #     for j in range(0, 5):
    #         grades.append(int(data[i][LABELS_NAME["groups"][f"grade_{j}"]]))
    #     grades_dict["grades"].append(grades)
    #     grades_dict["grades_mean"].append(data[i][5])
    #     grades_dict["grades_std"].append(data[i][6])

    #     audio_features.append(data[7, 90])

    # print(grades_dict)
    # print(audio_features)

    # print(labels)

    # data = load_data_from_npz()
    # grade_mean_analysis(data["grade_mean"])
    # grade_std_analysis(data["grade_std"], data["grade_mean"], data["track_ids"])
    # text_embedding_analysis(data["X_text"])
    # correlation_of_features_with_grade(data["X_audio"],
    #                                    data["X_text"],
    #                                    data["grade_mean"],
    #                                    data["grade"])
    # scaler_audio = StandardScaler()
    # scaler_text = StandardScaler()

    # X_audio_norm = scaler_audio.fit_transform(data["X_audio"])
    # X_text_norm = scaler_text.fit_transform(["X_text"])

    # X_full = np.hstack([X_audio_norm, X_text_norm])

    # audio_names = FEATURES_TAGS["features_names"]
    # text_names = [f"emb_{i}" for i in range(384)]
    # features_names = audio_names + text_names
    # print(data["grades_raw"])
    # compute_feature_correlations(X_full, data["grades_raw"], features_names)

    
def analysis():
    model_ver = "v1"

    data = load_data_from_npz("data/dataset_none_norm.npz")

    track_ids = data["track_ids"] # номер трека
    grades_raw = data["grades_raw"] # оценки
    grade_mean = data["grade_mean"] # стредняя оценка
    grade_std = data["grade_std"] # среднее отлоненик оценкок
    x_audio = data["X_audio"] # аудио признаки
    x_text = data["X_text"] # текстовые признаки

    grades = np.array(grades_raw).astype(np.int16)

    # анализ оценок
    grade_analysis(grade_raw=grades_raw)
    grade_mean_analysis(grade_mean=grade_mean)
    grade_std_analysis(grade_std=grade_std, grade_mean=grade_mean, tracks_ids=track_ids)
    final_grade_analysis(grade_raw=grades_raw)

    x_audio_norm, x_text_norm = normalization_features(x_audio, x_text, model_ver)

    correlation_features_grade_mean(X_audio_norm=x_audio_norm, X_text_norm=x_text_norm, grade_mean=grade_mean)
    correlation_features_grade_std(X_audio_norm=x_audio_norm, X_text_norm=x_text_norm, grade_std=grade_std)

    correlation_features_grade(X_audio_norm=x_audio_norm, X_text_norm=x_text_norm,
                               grade=np.array(grades[:,0]), grade_type="rhymes")
    correlation_features_grade(X_audio_norm=x_audio_norm, X_text_norm=x_text_norm,
                               grade=np.array(grades[:,1]), grade_type="structure")
    correlation_features_grade(X_audio_norm=x_audio_norm, X_text_norm=x_text_norm,
                               grade=np.array(grades[:,2]), grade_type="personality")
    correlation_features_grade(X_audio_norm=x_audio_norm, X_text_norm=x_text_norm,
                               grade=np.array(grades[:,2]), grade_type="realization")
    correlation_features_grade(X_audio_norm=x_audio_norm, X_text_norm=x_text_norm,
                               grade=np.array(grades[:,4]), grade_type="atmosphere")
    
    # анализ аудио признаков
    mfccs_analisys(X_audio=x_audio)
    mfcc_mean_std_analysis(X_audio=x_audio)
    chroma_analisys(X_audio=x_audio)
    chroma_mean_analisys(X_audio=x_audio)
    chroma_std_analisys(X_audio=x_audio)

    values_audio_features(X_audio=x_audio)

    # анализ текстовых признаков
    text_embedding_analysis(X_text=x_text)

