import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_preprocess_data(filepath):
    df = pd.read_csv(filepath)
    df = df.dropna()
    if 'id' in df.columns:
        df = df.drop(columns=['id'])
    # Use the correct target column
    X = df.drop('loan_status', axis=1)
    y = df['loan_status']
    # If the target is categorical (e.g., 1/0 or Good/Bad), you may want to encode it:
    # y = y.astype(int)  # If it's 1/0
    X = pd.get_dummies(X)
    return train_test_split(X, y, test_size=0.2, random_state=42)