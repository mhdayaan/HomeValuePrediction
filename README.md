# Home Value Prediction

This project aims to predict home values using various machine learning models. The project includes data preprocessing, exploratory data analysis, model training, and evaluation.

## Table of Contents

- [Introduction](#introduction)
- [Installation](#installation)
- [Usage](#usage)
- [Libraries Used](#libraries-used)
- [Data](#data)
- [Modeling](#modeling)
- [Results](#results)
- [Contributing](#contributing)

## Introduction

Home Value Prediction is a machine learning project that utilizes various regression models to estimate the value of homes based on features such as location, size, age, and more. The project includes data preprocessing, feature engineering, model training, and evaluation.

## Installation

To get started with this project, clone the repository and install the necessary dependencies.

```bash
git clone https://github.com/mhdayaan/HomeValuePrediction
cd home-value-prediction
pip install -r requirements.txt
```

## Usage

1. Run the Flask application:
   ```bash
   python main.py
   ```
2. Open your web browser and visit [http://127.0.0.1:5000/](http://127.0.0.1:5000/) to interact with the Home Value Prediction application.

## Libraries Used

The following libraries were used in this project:

- **pandas**: Data manipulation and analysis.
- **numpy**: Numerical computing.
- **matplotlib**: Data visualization.
- **seaborn**: Statistical data visualization.
- **plotly**: Interactive data visualization.
- **scikit-learn**: Machine learning models and tools.
- **xgboost**: Extreme Gradient Boosting.
- **Flask**: Web framework for Python.

## Data

The dataset used for this project contains information about various homes, including features like location, size, number of bedrooms, bathrooms, and more. Data preprocessing involved handling missing values, encoding categorical variables, and scaling numerical features.

## Modeling

Several regression models were trained and evaluated to predict home values:

- **Linear Regression**
- **Decision Tree Regressor**
- **Random Forest Regressor**
- **Gradient Boosting Regressor**
- **AdaBoost Regressor**
- **XGBoost Regressor**

## Results

The models were evaluated using metrics like Mean Absolute Error (MAE), Mean Squared Error (MSE), and Explained Variance Score. The best-performing model was selected based on these metrics.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## Front End Output
<img width="1393" alt="Screenshot 2024-07-25 at 4 13 16 PM" src="https://github.com/user-attachments/assets/f2bbee37-9b37-4937-9dcc-0537c77b66a2">
