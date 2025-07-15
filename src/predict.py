import joblib
import pandas as pd

def load_model(model_path='model.pkl'):
    clf, feature_names = joblib.load(model_path)
    return clf, feature_names

def predict_single(input_dict, model_path='model.pkl'):
    clf, feature_names = load_model(model_path)
    # Convert input dict to DataFrame, align columns
    X_input = pd.DataFrame([input_dict])
    X_input = pd.get_dummies(X_input)
    # Align columns with training
    for col in feature_names:
        if col not in X_input.columns:
            X_input[col] = 0
    X_input = X_input[feature_names]
    pred = clf.predict(X_input)[0]
    prob = clf.predict_proba(X_input).max()
    return pred, prob