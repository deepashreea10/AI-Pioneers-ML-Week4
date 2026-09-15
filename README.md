# 🏠 AI Pioneers ML - Week 4

## House Price Prediction System

An end-to-end Machine Learning project that predicts house values using Linear Regression. The project covers data preprocessing, model training, evaluation, model serialization using Joblib, and deployment of a Flask prediction API on Render.

---

## 🎯 Project Objective

The objective of this project is to build and deploy a complete Machine Learning application. The project demonstrates the workflow from preparing a dataset and training a Machine Learning model to saving the trained model and exposing it through a Flask API.

---

## 📊 Dataset

The project uses the **California Housing dataset** available through Scikit-learn.

- **Samples:** 20,640
- **Features:** 8
- **Target:** HouseValue

### Features Used

| Feature | Description |
|---|---|
| MedInc | Median income |
| HouseAge | Median house age |
| AveRooms | Average number of rooms |
| AveBedrms | Average number of bedrooms |
| Population | Block population |
| AveOccup | Average house occupancy |
| Latitude | Latitude of the location |
| Longitude | Longitude of the location |

---

## ⚙️ Project Workflow

Dataset Loading ↓ Data Inspection ↓ Train-Test Split ↓ Feature Scaling ↓ Linear Regression Model ↓ Model Evaluation ↓ Model Serialization using Joblib ↓ Flask Prediction API ↓ Deployment using Render ↓ Live Prediction

---

## 🤖 Machine Learning Model

The project uses **Linear Regression** for house value prediction.

The dataset was divided into:

- **Training data:** 16,512 samples
- **Testing data:** 4,128 samples
- **Split ratio:** 80:20
- **Random state:** 42

The numerical features were standardized using `StandardScaler` before training the model.

---

## 📈 Model Performance

The trained Linear Regression model was evaluated using the following metrics:

| Metric | Value |
|---|---:|
| MAE | 0.5332 |
| MSE | 0.5559 |
| RMSE | 0.7456 |
| R² Score | 0.5758 |

The model achieved an R² score of approximately **57.58%**, indicating that the model explains a reasonable portion of the variation in house values.

---

## 💾 Model Serialization

The trained Machine Learning model and the scaler were saved using **Joblib**.

### Files Created

- `house_price_model.joblib`
- `house_price_scaler.joblib`

Saving both the model and scaler allows the deployed application to use the same preprocessing and trained model without retraining.

---

## 🌐 Flask Prediction API

A Flask API was created to provide predictions from new house data.

### API Endpoint

`POST /predict`

The API accepts the following features:

- `MedInc`
- `HouseAge`
- `AveRooms`
- `AveBedrms`
- `Population`
- `AveOccup`
- `Latitude`
- `Longitude`

The input data is scaled using the saved scaler and then passed to the saved Linear Regression model.

---

## 🧪 API Testing

The deployed API was tested successfully using Python `requests`.

### Example Input

```json
{
    "MedInc": 5.0,
    "HouseAge": 20.0,
    "AveRooms": 5.0,
    "AveBedrms": 1.0,
    "Population": 1000.0,
    "AveOccup": 3.0,
    "Latitude": 34.0,
    "Longitude": -118.0
}
```

### Example Response

```json
{
    "predicted_house_value": 2.4731
}
```

The API returned **HTTP Status Code 200**, confirming that the deployed prediction endpoint was working successfully.

---

## 🚀 Deployment

The Flask application was deployed using **Render**.

### Live Application

[https://ai-pioneers-ml-week4.onrender.com](https://ai-pioneers-ml-week4.onrender.com)

The root endpoint confirms that the House Price Prediction API is running.

### Deployment Configuration

**Build Command:**

`pip install -r requirements.txt`

**Start Command:**

`gunicorn app:app`

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib
- Flask
- Gunicorn
- Google Colab
- GitHub
- Render

---

## 📁 Project Files

```text
AI-Pioneers-ML-Week4/
│
├── app.py
├── requirements.txt
├── house_price_model.joblib
└── house_price_scaler.joblib
```

The complete model development process is documented in the Google Colab notebook:

`Week_4_House_Price_Prediction.ipynb`

---

## 🎓 Learning Outcomes

Through this project, I learned how to:

- Prepare a dataset for Machine Learning.
- Split data into training and testing sets.
- Apply feature scaling using StandardScaler.
- Train a Linear Regression model.
- Evaluate a regression model using MAE, MSE, RMSE, and R².
- Serialize Machine Learning models using Joblib.
- Build a prediction API using Flask.
- Handle JSON input and prediction responses.
- Deploy a Python Flask application using Render.
- Connect a trained Machine Learning model with a live web API.

---

## ✅ Conclusion

This project demonstrates a complete end-to-end Machine Learning workflow, from dataset preprocessing and model training to model serialization, API development, and cloud deployment. The deployed Flask API successfully accepts house-related features and returns a predicted house value using the trained Linear Regression model.

---

## 🔗 Project Links

**GitHub Repository:**

https://github.com/deepashreea10/AI-Pioneers-ML-Week4

**Live API:**

---

## 📑 Project Presentation

The project presentation is included in this repository as part of the Week 4 capstone deliverables.

**Presentation:** `Week_4_Presentation.pdf`

[https://ai-pioneers-ml-week4.onrender.com](https://ai-pioneers-ml-week4.onrender.com)
