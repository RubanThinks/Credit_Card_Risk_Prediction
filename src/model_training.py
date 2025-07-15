import joblib
from sklearn.tree import DecisionTreeClassifier
from src.data_preprocessing import load_and_preprocess_data

def train_and_save_model(data_path, model_path='model.pkl'):
    X_train, X_test, y_train, y_test = load_and_preprocess_data(data_path)
    clf = DecisionTreeClassifier(max_depth=4, random_state=42)
    clf.fit(X_train, y_train)
    joblib.dump((clf, X_train.columns), model_path)
    print("Model trained and saved to", model_path)
    print("Training accuracy:", clf.score(X_train, y_train))
    print("Test accuracy:", clf.score(X_test, y_test))