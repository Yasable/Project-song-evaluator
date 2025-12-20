import numpy as np
import matplotlib.pyplot as plt

from config_dataset import FEATURES_TAGS, ANALYSIS_DIR

def audio_analisys(X_audio, audio_type):
    ids = FEATURES_TAGS["groups"][audio_type]
    mfccs = np.array([mfcc[ids[0]:ids[1] + 1] for mfcc in X_audio])
    all_mfccs = np.array(mfccs).flatten()

    mfcc_mean = np.array([mfcc.mean() for mfcc in mfccs])
    mfcc_std = np.array([mfcc.std() for mfcc in mfccs])

    plt.figure(figsize=(12, 4))

    fig, ax = plt.subplots()
    ax.set_facecolor("#B88AEE")
    plt.gcf().set_facecolor("#B492DC")

    plt.subplot(1, 2, 1)
    plt.hist(all_mfccs, bins=10, alpha=0.7, edgecolor="k")
    plt.title("Распределение mfcc")
    plt.xlabel("mfcc")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.boxplot(all_mfccs, vert=False)
    plt.title("mfcc")
    plt.xlabel("mfcc")

    plt.tight_layout()
    plt.savefig('processing_dataset/result_analysis/mffc_analysis.png')
    plt.show()

    print(f"\n ЗНАЧЕНИЯ MFCC")
    print(f"Среднее значение mfcc: {all_mfccs.mean()}")
    print(f"Минимальное значение mfcc: {all_mfccs.min()}")
    print(f"Максимальное значение mfcc: {all_mfccs.max()}")

def mfccs_analisys(X_audio):
    ids = FEATURES_TAGS["groups"]["mfcc"]
    mfccs = np.array([mfcc[ids[0]:ids[1] + 1] for mfcc in X_audio])
    all_mfccs = np.array(mfccs).flatten()

    mfcc_mean = np.array([mfcc.mean() for mfcc in mfccs])
    mfcc_std = np.array([mfcc.std() for mfcc in mfccs])

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.hist(all_mfccs, bins=10, alpha=0.7, edgecolor="k")
    plt.title("Распределение mfcc")
    plt.xlabel("mfcc")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.boxplot(all_mfccs, vert=False)
    plt.title("mfcc")
    plt.xlabel("mfcc")

    plt.tight_layout()
    plt.savefig('processing_dataset/result_analysis/mffc_analysis.png')
    plt.show()

    print(f"\n ЗНАЧЕНИЯ MFCC")
    print(f"Среднее значение mfcc: {all_mfccs.mean()}")
    print(f"Минимальное значение mfcc: {all_mfccs.min()}")
    print(f"Максимальное значение mfcc: {all_mfccs.max()}")

def mfcc_mean_std_analysis(X_audio):
    ids = FEATURES_TAGS["groups"]["mfcc"]
    mfccs = np.array([mfcc[ids[0]:ids[1] + 1] for mfcc in X_audio])

    mfcc_mean = np.array([mfcc.mean() for mfcc in mfccs])
    mfcc_std = np.array([mfcc.std() for mfcc in mfccs])

    plt.figure(figsize=(12, 8))

    plt.subplot(2, 2, 1)
    plt.hist(mfcc_mean, bins=10, alpha=0.7, edgecolor="k")
    plt.title("Распределение среднего mfcc")
    plt.xlabel("Средняя mfcc")
    plt.ylabel("Количество")

    plt.subplot(2, 2, 2)
    plt.boxplot(mfcc_mean, vert=False)
    plt.title("Среднии mfcc")
    plt.xlabel("Средняя mfcc")

    plt.subplot(2, 2, 3)
    plt.hist(mfcc_std, bins=10, alpha=0.7, edgecolor="k")
    plt.title("Распределение среднего отклонения mfcc")
    plt.xlabel("Среднее распределение mfcc")
    plt.ylabel("Количество")

    plt.subplot(2, 2, 4)
    plt.boxplot(mfcc_std, vert=False)
    plt.title("Среднее распределение mfcc")
    plt.xlabel("Среднее распределение mfcc")

    plt.tight_layout()
    plt.savefig('processing_dataset/result_analysis/mffc_mean_std_analysis.png')
    plt.show()

    print(f"\n ЗНАЧЕНИЯ MFCC MEAN")
    print(f"Среднее значение mfcc_mean: {mfcc_mean.mean()}")
    print(f"Минимальное значение mfcc_mean: {mfcc_mean.min()}")
    print(f"Максимальное значение mfcc_mean: {mfcc_mean.max()}")

    print(f"\n ЗНАЧЕНИЯ MFCC STD")
    print(f"Среднее значение mfcc_std: {mfcc_std.mean()}")
    print(f"Минимальное значение mfcc_std: {mfcc_std.min()}")
    print(f"Максимальное значение mfcc_std: {mfcc_std.max()}")

# Анализ chroma

def chroma_analisys(X_audio):
    ids = FEATURES_TAGS["groups"]["chroma"]
    chromas = np.array([chroma[ids[0]:ids[1] + 1] for chroma in X_audio])
    all_chroma = np.array(chromas).flatten()

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.hist(all_chroma, bins=10, alpha=0.7, edgecolor="k")
    plt.title("Распределение chroma")
    plt.xlabel("Chroma")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.boxplot(all_chroma, vert=False)
    plt.title("Chroma")
    plt.xlabel("Chroma")

    plt.tight_layout()
    plt.savefig('processing_dataset/result_analysis/chroma_analisys.png')
    plt.show()

    print(f"\n ЗНАЧЕНИЯ CHROMA")
    print(f"Среднее значение chroma: {all_chroma.mean()}")
    print(f"Минимальное значение chroma: {all_chroma.min()}")
    print(f"Максимальное значение chroma: {all_chroma.max()}")

def chroma_mean_analisys(X_audio):
    ids = FEATURES_TAGS["groups"]["chroma"]
    chromas = np.array([chroma[ids[0]:ids[1] + 1] for chroma in X_audio])

    chroma_mean = np.array([chroma.mean() for chroma in chromas])

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.hist(chroma_mean, bins=10, alpha=0.7, edgecolor="k")
    plt.title("Распределение среднего chroma")
    plt.xlabel("Средняя chroma")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.boxplot(chroma_mean, vert=False)
    plt.title("Среднии chroma")
    plt.xlabel("Средняя chroma")

    plt.tight_layout()
    plt.savefig('processing_dataset/result_analysis/chroma_mean_analisys.png')
    plt.show()

    print(f"\n ЗНАЧЕНИЯ CHROMA MEAN")
    print(f"Среднее значение mfcc_mean: {chroma_mean.mean()}")
    print(f"Минимальное значение mfcc_mean: {chroma_mean.min()}")
    print(f"Максимальное значение mfcc_mean: {chroma_mean.max()}")

def chroma_std_analisys(X_audio):
    ids = FEATURES_TAGS["groups"]["chroma"]
    chromas = np.array([chroma[ids[0]:ids[1] + 1] for chroma in X_audio])

    chroma_std = np.array([chroma.std() for chroma in chromas])

    plt.figure(figsize=(12, 4))

    plt.subplot(1, 2, 1)
    plt.hist(chroma_std, bins=10, alpha=0.7, edgecolor="k")
    plt.title("Распределение среднего chroma")
    plt.xlabel("Средняя chroma")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.boxplot(chroma_std, vert=False)
    plt.title("Среднии chroma")
    plt.xlabel("Средняя chroma")

    plt.tight_layout()
    plt.savefig('processing_dataset/result_analysis/chroma_std_analisys.png')
    plt.show()

    print(f"\n ЗНАЧЕНИЯ CHROMA STD")
    print(f"Среднее значение mfcc_std: {chroma_std.mean()}")
    print(f"Минимальное значение mfcc_std: {chroma_std.min()}")
    print(f"Максимальное значение mfcc_std: {chroma_std.max()}")



def values_audio_features(X_audio):
    ids_mfcc = FEATURES_TAGS["groups_2"]["mfcc"]
    ids_chroma = FEATURES_TAGS["groups_2"]["chroma"]
    ids_contrast = FEATURES_TAGS["groups_2"]["contrast"]
    ids_centroid = FEATURES_TAGS["groups_2"]["centroid"]
    ids_bandwidth = FEATURES_TAGS["groups_2"]["bandwidth"]
    ids_zcr = FEATURES_TAGS["groups_2"]["zcr"]

    mfccs = np.array([mfcc[ids_mfcc[0]:ids_mfcc[1] + 1] for mfcc in X_audio])
    chromas = np.array([chroma[ids_chroma[0]:ids_chroma[1] + 1] for chroma in X_audio])
    contrasts = np.array([contrast[ids_contrast[0]:ids_contrast[1] + 1] for contrast in X_audio])
    centroids = np.array([centroid[ids_centroid[0]:ids_centroid[1] + 1] for centroid in X_audio])
    bandwidths = np.array([bandwidth[ids_bandwidth[0]:ids_bandwidth[1] + 1] for bandwidth in X_audio])
    zcrs = np.array([zcr[ids_zcr[0]:ids_zcr[1] + 1] for zcr in X_audio])

    all_mfccs = np.array(mfccs).flatten()
    all_chromas = np.array(chromas).flatten()
    all_contrasts = np.array(contrasts).flatten()
    all_centroids = np.array(centroids).flatten()
    all_bandwidths = np.array(bandwidths).flatten()
    all_zcrs = np.array(zcrs).flatten()

    print(f"\n CРЕДНИЕ ЗНАЧЕНИЯ")
    print(f"Среднее значение mfcc: {all_mfccs.mean()}")
    print(f"Среднее значение chroma: {all_chromas.mean()}")
    print(f"Среднее значение contrast: {all_contrasts.mean()}")
    print(f"Среднее значение centroid: {all_centroids.mean()}")
    print(f"Среднее значение bandwidths: {all_bandwidths.mean()}")
    print(f"Среднее значение zrc: {all_zcrs.mean()}")

    print(f"\n МАКСИМАЛЬНЫЕ ЗНАЧЕНИЯ")
    print(f"Максимальное значение mfcc: {all_mfccs.max()}")
    print(f"Максимальное значение chroma: {all_chromas.max()}")
    print(f"Максимальное значение contrast: {all_contrasts.max()}")
    print(f"Максимальное значение centroid: {all_centroids.max()}")
    print(f"Максимальное значение bandwidth: {all_bandwidths.max()}")
    print(f"Максимальное значение zcr: {all_zcrs.max()}")

    print(f"\n МИНИМАЛЬНЫЕ ЗНАЧЕНИЯ")
    print(f"Максимальное значение mfcc: {all_mfccs.min()}")
    print(f"Максимальное значение chroma: {all_chromas.min()}")
    print(f"Максимальное значение contrast: {all_contrasts.min()}")
    print(f"Максимальное значение centroid: {all_centroids.min()}")
    print(f"Максимальное значение bandwidth: {all_bandwidths.min()}")
    print(f"Максимальное значение zcr: {all_zcrs.min()}")