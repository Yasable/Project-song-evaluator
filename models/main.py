import pandas as pd
import numpy as np
import joblib
import os

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

from models.processing import calculation_features

MODEL_PATH = 'models/rf_model.pkl'
SCALER_PATH = 'models/scaler.pkl'

def load_labels_features():
    df = pd.read_csv('data/dataset_none_norm.csv')

    grade_cols = [col for col in df.columns if col.startswith('grade_')]
    drop_cols = ['track_id', 'grade_mean', 'grade_std'] + grade_cols
    feature_columns = [col for col in df.columns if col not in drop_cols]
    X = df[feature_columns]
    y = df[['grade_0', 'grade_1', 'grade_2', 'grade_3', 'grade_4']]

    X_train, X_validation_test, y_train, y_validation_test = train_test_split(
        X, y, test_size=0.4, random_state=100)

    X_validation, X_test, y_validation, y_test = train_test_split(
        X_validation_test, y_validation_test, test_size=0.5, random_state=100)

    print("X.shape:", X.shape)
    print("y.shape:", y.shape)

    scaler = StandardScaler()
    X_train_scaled = scaler.fit_transform(X_train)
    X_validation_scaled = scaler.transform(X_validation)
    X_test_scaled = scaler.transform(X_test)

    return X_train_scaled, X_test_scaled, X_validation_scaled, y_train, y_test, y_validation, scaler


def learn_model():
    X_train, X_test, X_val, y_train, y_test, y_val, scaler = load_labels_features()

    rf_model = RandomForestRegressor(max_depth=7, n_estimators=200, random_state=42)
    rf_model.fit(X_train, y_train)

    os.makedirs(os.path.dirname(MODEL_PATH), exist_ok=True)

    joblib.dump(rf_model, MODEL_PATH)
    joblib.dump(scaler, SCALER_PATH)

    score(X_val, y_val, rf_model, "(Validation)")
    score(X_test, y_test, rf_model, "(Test)")


def load_model():
    if os.path.exists(MODEL_PATH) and os.path.exists(SCALER_PATH):
        model = joblib.load(MODEL_PATH)
        scaler = joblib.load(SCALER_PATH)
        return model, scaler
    else:
        print("Модель или скалер не найдены. Выполните learn_model() для обучения.")
        return None, None


def score(features_validation, labels_validation, model, type_model):
    y_true = labels_validation
    y_pred = model.predict(features_validation)
    print(type_model)
    print("Score:", model.score(features_validation, labels_validation))
    print("MAE:", mean_absolute_error(y_true, y_pred))
    print("MSE:", mean_squared_error(y_true, y_pred))
    print("RMSE:", np.sqrt(mean_squared_error(y_true, y_pred)))
    print("R²:", r2_score(y_true, y_pred), "\n")


def main():
    model, scaler = load_model()
    if model is None:
        print("Обучение новой модели...")
        learn_model()
        model, scaler = load_model()

    X_train, X_test, X_val, y_train, y_test, y_val, _ = load_labels_features()

    score(X_val, y_val, model, "(Validation)")
    score(X_test, y_test, model, "(Test)")

    features_song = calculation_features("models/5opka_-_SLAVA_BOSSU.mp3", "https://genius.com/5opka-glory-to-boss-lyrics")
    features_song = features_song.reshape(1, -1)
    features_song = scaler.transform(features_song)

    pred = model.predict(features_song)
    pred_int = np.round(pred).astype(int)
    print("Предсказанные оценки (целые):", pred_int)

if __name__ == '__main__':
    main()