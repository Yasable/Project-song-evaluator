import numpy as np
import matplotlib.pyplot as plt

def text_embedding_analysis(X_text):
    all_features = np.array(X_text).flatten()
    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.hist(all_features, bins=20, alpha=0.7, color="green", edgecolor="k")
    plt.title("Итоговые оцени")
    plt.xlabel("Оценки")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.boxplot(all_features, vert=False)
    plt.title("Итоговые оценки")
    plt.xlabel("Итоговая оценка")

    plt.tight_layout()
    plt.savefig("processing_dataset/result_analysis/te_analysis.png")
    plt.show()

    norms = np.linalg.norm(X_text, axis=1)
    print(f"L2-норма текстовых эмбеддингов: {norms.mean()} +- {norms.std()}")

    print(f"Минимальное значение текстового эмбеддинга: {all_features.min()}")
    print(f"Максимальное значение текстового эмбеддинга: {all_features.max()}")
