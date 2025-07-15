# Credit Risk Prediction App

A machine learning-powered web application that predicts credit card approval risk using Streamlit. The app analyzes various applicant features to determine the likelihood of credit default.

##  Features

- **Interactive Web Interface**: User-friendly Streamlit application
- **Real-time Risk Prediction**: Instant risk assessment based on applicant data
- **Multiple Input Parameters**: Comprehensive analysis using various financial and personal factors
- **Machine Learning Model**: Trained model for accurate risk prediction
- **Confidence Score**: Provides prediction confidence level

##  Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Project Structure](#project-structure)
- [Input Parameters](#input-parameters)
- [Model Information](#model-information)
- [Running the Application](#running-the-application)
- [Contributing](#contributing)
- [License](#license)

##  Installation

### Prerequisites

- Python 3.7 or higher
- pip package manager

### Step 1: Clone the Repository

```bash
git clone https://github.com/Rakesh-ai-ds/credit-risk-prediction.git
cd credit-risk-prediction
```

### Step 2: Create Virtual Environment (Recommended)

```bash
# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On macOS/Linux:
source venv/bin/activate
```

### Step 3: Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 4: Verify Installation

Ensure all required packages are installed:
- streamlit
- pandas
- scikit-learn
- pickle
- numpy

##  Usage

### Running the Application

1. **Start the Streamlit App**:
   ```bash
   streamlit run app.py
   ```

2. **Access the Application**:
   - Local URL: `http://localhost:8501`
   - Network URL: `http://172.16.12.6:8501` (or your network IP)

3. **Using the App**:
   - Fill in the applicant data form
   - Click "Predict Risk" button
   - View the prediction result and confidence score

##  Project Structure

```
credit-risk-prediction/
├── data/
│   └── credit_risk_dataset.csv          # Training dataset
├── notebooks/
│   └── credit_risk.ipynb                # Jupyter notebook for analysis
├── src/
│   ├── __pycache__/                     # Python cache files
│   ├── data_preprocessing.py            # Data preprocessing functions
│   ├── model_training.py                # Model training script
│   ├── predict.py                       # Prediction functions
│   └── utils.py                         # Utility functions
├── app.py                               # Main Streamlit application
├── model.pkl                            # Trained machine learning model
├── pickle_app.py                        # Pickle operations
├── requirements.txt                     # Python dependencies
├── README.md                            # Project documentation
├── LICENSE                              # License file
└── .gitignore                          # Git ignore file
```

##  Input Parameters

The application accepts the following input parameters:

### Personal Information
- **Person Age**: Age of the applicant (years)
- **Person Income**: Annual income (₹)
- **Person Home Ownership**: Housing status (RENT/OWN/MORTGAGE)
- **Person Employment Length**: Years of employment

### Loan Information
- **Loan Intent**: Purpose of loan (PERSONAL/EDUCATION/MEDICAL/VENTURE/HOMEIMPROVEMENT/DEBTCONSOLIDATION)
- **Loan Grade**: Credit grade (A/B/C/D/E/F/G)
- **Loan Amount**: Requested loan amount (₹)
- **Loan Interest Rate**: Interest rate (%)
- **Loan Status**: Current loan status
- **Loan Percent Income**: Loan amount as percentage of income

### Credit Bureau Information
- **CB Person Default on File**: Previous defaults (Y/N)
- **CB Person Credit History Length**: Length of credit history (years)

##  Model Information

### Model Training Process

1. **Data Preprocessing**:
   - Data cleaning and handling missing values
   - Feature encoding for categorical variables
   - Data normalization and scaling

2. **Feature Engineering**:
   - Selection of relevant features
   - Creating derived features
   - Handling categorical variables

3. **Model Training**:
   - Algorithm selection and training
   - Cross-validation for model evaluation
   - Hyperparameter tuning

4. **Model Evaluation**:
   - Performance metrics calculation
   - Validation on test dataset
   - Model persistence using pickle

### Model Output

- **Predicted Risk**: Binary classification (0 = Low Risk, 1 = High Risk)
- **Confidence Score**: Probability score indicating prediction confidence

##  Running the Application

### Method 1: Direct Run

```bash
# Navigate to project directory
cd credit-risk-prediction

# Run the application
streamlit run app.py
```

### Method 2: With Custom Configuration

```bash
# Run with custom port
streamlit run app.py --server.port 8502

# Run with custom host
streamlit run app.py --server.address 0.0.0.0
```

##  Development Setup

### For Model Training

1. **Prepare Data**:
   ```bash
   python src/data_preprocessing.py
   ```

2. **Train Model**:
   ```bash
   python src/model_training.py
   ```

3. **Test Predictions**:
   ```bash
   python src/predict.py
   ```

### For Local Development

1. **Install development dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Run in development mode**:
   ```bash
   streamlit run app.py --server.runOnSave true
   ```

##  Example Usage

### Sample Input Data

```
Person Age: 28
Person Income: 60000
Person Home Ownership: RENT
Person Employment Length: 4.78
Loan Intent: PERSONAL
Loan Grade: D
Loan Amount: 9589.37
Loan Interest Rate: 11.01
Loan Status: 0.22
Loan Percent Income: 0.17
CB Person Default on File: Y
CB Person Credit History Length: 5.80
```

### Expected Output

```
Predicted Risk: 1
Confidence: 0.58
```

##  Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

##  License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

##  Author

**Ruban**
- Ruban – AI & Data Science Student
- rubans0908@gmail.com



##  Acknowledgments

- Dataset source and contributors
- Streamlit framework for the web interface
- Scikit-learn for machine learning capabilities
- Open source community for various tools and libraries

##  Support

If you encounter any issues or have questions:
1. Check the existing issues on GitHub
2. Create a new issue with detailed description
3. Provide steps to reproduce the problem

---
![image alt](https://github.com/Rakesh-ai-ds/credit-risk-prediction/blob/135533a2771787811dcb1d13290e0e2c5823c7b8/9d537fd3-1f76-4109-b093-52cb0e5959f9.jpg)

