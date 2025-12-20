import numpy as np
import matplotlib.pyplot as plt

from utils.data_processing import final_score

def grade_mean_analysis(grade_mean):
    plt.figure(figsize=(12, 4))

    fig, ax = plt.subplots()
    ax.set_facecolor("#B88AEE")
    plt.gcf().set_facecolor("#B492DC")

    plt.subplot(1, 2, 1)
    plt.hist(grade_mean, bins=10, alpha=0.7, edgecolor="k")
    plt.title("Распределение средних оценок")
    plt.xlabel("Средняя оценка")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.boxplot(grade_mean, vert=False)
    plt.title("Среднии оценки")
    plt.xlabel("Средняя оценка")

    plt.tight_layout()
    plt.savefig("processing_dataset/result_analysis/grade_mean_analysis.png")
    plt.show()

    print(f"Средняя оценка: {grade_mean.mean()} +- {grade_mean.std()}")
    print(f"Максимальная средняя оценка: {grade_mean.max()}")
    print(f"Минимальная средняя оценка: {grade_mean.min()}")

def grade_std_analysis(grade_std, grade_mean, tracks_ids):
    plt.figure(figsize=(12, 4))

    fig, ax = plt.subplots()
    ax.set_facecolor("#B88AEE")
    plt.gcf().set_facecolor("#B492DC")

    plt.subplot(1, 2, 1)
    plt.hist(grade_std, bins=20, alpha=0.7, color="orange", edgecolor="k")
    plt.title("Распределение стандартного отклонения оценок")
    plt.xlabel("Стандартное отклонение")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.scatter(grade_mean, grade_std)
    plt.title("Среднии оценки и среднее отлонение")
    plt.xlabel("Средняя оценка")
    plt.ylabel("Стандартное отклонение")
    plt.grid(True)

    plt.tight_layout()
    plt.savefig("processing_dataset/result_analysis/grade_std_analysis.png")
    plt.show()

    print(f"Среднее отклонение: {grade_std.mean()}")
    print(f"Максимальное отлонение: {grade_std.max()}, {tracks_ids[np.argmax(grade_std)]}")
    # print(f"Минимальное отлонение: {grade_std.min()}, {tracks_ids[np.argmin(grade_std)]}")

def grade_analysis(grade_raw):
    all_grades = grade_raw.flatten()

    fig, ax = plt.subplots()
    ax.set_facecolor("#B88AEE")
    plt.gcf().set_facecolor("#B492DC")

    plt.figure(figsize=(2, 4))
    plt.hist(all_grades, bins=20, alpha=0.7, color="green", edgecolor="k")
    plt.title("Количество всех оценок")
    plt.xlabel("Оценки")
    plt.ylabel("Количество")
    plt.savefig("processing_dataset/result_analysis/grades_analysis.png")
    plt.show()

def final_grade_analysis(grade_raw):
    final_grades = np.array([final_score(grades) for grades in grade_raw])
    
    fig, ax = plt.subplots()
    ax.set_facecolor("#B88AEE")
    plt.gcf().set_facecolor("#B492DC")

    plt.figure(figsize=(8, 4))

    plt.subplot(1, 2, 1)
    plt.hist(final_grades, bins=20, alpha=0.7, color="green", edgecolor="k")
    plt.title("Итоговые оцени")
    plt.xlabel("Оценки")
    plt.ylabel("Количество")

    plt.subplot(1, 2, 2)
    plt.boxplot(final_grades, vert=False)
    plt.title("Итоговые оценки")
    plt.xlabel("Итоговая оценка")

    plt.tight_layout()
    plt.savefig("processing_dataset/result_analysis/final_grade_analysis.png")
    plt.show()

    print(f"Минимальная итоговая оценка: {final_grades.min()}")
    print(f"Максимальная итоговая оценка: {final_grades.max()}")
    print(f"Средняя итоговая оценка: {final_grades.mean()}")
    print(f"Среднее отклонение итоговых оценок: {final_grades.std()}")
