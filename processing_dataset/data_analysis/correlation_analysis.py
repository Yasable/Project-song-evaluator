import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import pearsonr

from config_dataset import FEATURES_TAGS

def correlation_features_grade_mean(X_audio_norm, X_text_norm, grade_mean):
    X_full = np.hstack([X_audio_norm, X_text_norm])

    audio_names = FEATURES_TAGS["features_names"]
    text_names = [f"emb_{i}" for i in range(384)]
    features_names = audio_names + text_names
    
    corrs = []

    for i in range(X_full.shape[1]):
        r, _ = pearsonr(X_full[:, i], grade_mean)
        corrs.append((abs(r), r, i, features_names[i]))

    corrs.sort(reverse=True)

    names = []
    values = []

    print("\n Признаки по корреляции с оценкой")
    for abs_r, r, idx, name in corrs[:50]:
        print(f"{name}, {r}")
        names.append(name)
        values.append(abs(r))

    plt.figure(figsize=(12, 6))
    plt.bar(names, values)
    plt.title("Корреляция признаков с средней оценкой")
    plt.xticks(rotation=90)
    plt.xlabel("Признаки")
    plt.ylabel("Влияние")
    plt.savefig('processing_dataset/result_analysis/corr_grade_mean.png')
    plt.show()

def correlation_features_grade_std(X_audio_norm, X_text_norm, grade_std):
    X_full = np.hstack([X_audio_norm, X_text_norm])

    audio_names = FEATURES_TAGS["features_names"]
    text_names = [f"emb_{i}" for i in range(384)]
    features_names = audio_names + text_names
    
    corrs = []

    for i in range(X_full.shape[1]):
        r, _ = pearsonr(X_full[:, i], grade_std)
        corrs.append((abs(r), r, i, features_names[i]))

    corrs.sort(reverse=True)

    names = []
    values = []

    print("\n Признаки по корреляции с среднем отклонением оценки")
    for abs_r, r, idx, name in corrs[:50]:
        print(f"{name}, {r}")
        names.append(name)
        values.append(abs(r))

    plt.figure(figsize=(12, 6))
    plt.bar(names, values)
    plt.title("Корреляция признаков с среднем отклонением оценки")
    plt.xticks(rotation=90)
    plt.xlabel("Признаки")
    plt.ylabel("Влияние")
    plt.savefig('processing_dataset/result_analysis/corr_grade_std.png')
    plt.show()

def correlation_features_grade(X_audio_norm, X_text_norm, grade, grade_type):
    X_full = np.hstack([X_audio_norm, X_text_norm])

    audio_names = FEATURES_TAGS["features_names"]
    text_names = [f"emb_{i}" for i in range(384)]
    features_names = audio_names + text_names
    
    corrs = []

    for i in range(X_full.shape[1]):
        r, _ = pearsonr(X_full[:, i], grade)
        corrs.append((abs(r), r, i, features_names[i]))

    corrs.sort(reverse=True)

    names = []
    values = []

    print(f"\n Признаки по корреляции с {grade_type}")
    for abs_r, r, idx, name in corrs[:50]:
        print(f"{name}, {r}")
        names.append(name)
        values.append(abs(r))

    plt.figure(figsize=(12, 6))
    plt.bar(names, values)
    plt.title(f"Корреляция признаков с {grade_type}")
    plt.xticks(rotation=90)
    plt.xlabel("Признаки")
    plt.ylabel("Влияние")
    plt.savefig(f"processing_dataset/result_analysis/corr_grade_{grade_type}.png") 
    plt.show()