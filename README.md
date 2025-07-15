# Credit Card Risk Prediction

This project predicts the risk of credit default for credit card applicants using machine learning. It provides a Streamlit web interface to enter applicant data and get a risk prediction.

## Project Structure

- `data/credit_risk_dataset.csv` – Input dataset (CSV)
- `src/data_preprocessing.py` – Data cleaning and splitting
- `src/model_training.py` – Model training and saving
- `src/predict.py` – Model loading and prediction
- `app.py` – Streamlit Web App
- `requirements.txt` – Project dependencies

## How to Run

1. Place `credit_risk_dataset.csv` in a `data/` folder.
2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```
3. Run the app:
   ```
   streamlit run app.py
   ```

## Usage

- Enter applicant details in the interface.
- Click "Predict Risk" to see the prediction and confidence score.

## License

MIT
