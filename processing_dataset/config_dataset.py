
# Paths
DATA_DIR = "data/"
TRACKS_DIR = DATA_DIR + "track/"
DATA_TRACK_DIR = TRACKS_DIR + "track_{}/"

TRACK_FILE_TEMPOLATE = "track_{}.json"

# settings fot mfss
N_MFCC = 20

# features names
FEATURES_TAGS = {
    "features_names": [
        "mfcc_0_mean", "mfcc_1_mean", "mfcc_2_mean", "mfcc_3_mean", "mfcc_4_mean",
        "mfcc_5_mean", "mfcc_6_mean", "mfcc_7_mean", "mfcc_8_mean", "mfcc_9_mean",
        "mfcc_10_mean", "mfcc_11_mean", "mfcc_12_mean", "mfcc_13_mean", "mfcc_14_mean",
        "mfcc_15_mean", "mfcc_16_mean", "mfcc_17_mean", "mfcc_18_mean", "mfcc_19_mean",
        "mfcc_0_std", "mfcc_1_std", "mfcc_2_std", "mfcc_3_std", "mfcc_4_std",
        "mfcc_5_std", "mfcc_6_std", "mfcc_7_std", "mfcc_8_std", "mfcc_9_std",
        "mfcc_10_std", "mfcc_11_std", "mfcc_12_std", "mfcc_13_std", "mfcc_14_std",
        "mfcc_15_std", "mfcc_16_std", "mfcc_17_std", "mfcc_18_std", "mfcc_19_std",
        "chroma_0_mean", "chroma_1_mean", "chroma_2_mean", "chroma_3_mean", "chroma_4_mean", "chroma_5_mean",
        "chroma_6_mean", "chroma_7_mean", "chroma_8_mean", "chroma_9_mean", "chroma_10_mean", "chroma_11_mean",
        "chroma_0_std", "chroma_1_std", "chroma_2_std", "chroma_3_std", "chroma_4_std", "chroma_5_std",
        "chroma_6_std", "chroma_7_std", "chroma_8_std", "chroma_9_std", "chroma_10_std", "chroma_11_std",
        "contrast_0_mean", "contrast_1_mean", "contrast_2_mean", "contrast_3_mean", "contrast_4_mean", "contrast_5_mean", "contrast_6_mean",
        "contrast_0_std", "contrast_1_std", "contrast_2_std", "contrast_3_std", "contrast_4_std", "contrast_5_std", "contrast_6_std", 
        "centroid_mean", "centroid_std",
        "bandwidth_mean", "bandwidth_std",
        "zcr_mean", "zcr_std",
        "tempo"
    ],
    "groups": {
        "mfcc": [0, 39],
        "chroma": [40, 63],
        "contrast": [64, 77],
        "centroid": [78, 79],
        "bandwidth": [80, 81],
        "zcr": [82, 83],
        "tempo": [84]
    }
}