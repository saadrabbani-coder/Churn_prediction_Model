# Telco Customer Churn Prediction

An end-to-end Machine Learning project that predicts whether a telecommunications customer is likely to churn based on customer demographics, services, contract details, billing, and payment information.

## Project Overview

The goal of this project is to identify customers who are likely to leave the telecom company so that targeted retention strategies can be applied.

**Problem Type:** Binary Classification
**Dataset:** Telco Customer Churn
**Rows:** 7,043
**Columns:** 21

## Data Preparation

* Handled 11 blank `TotalCharges` values by filling them with `0` because they belonged to new customers with zero tenure.
* Converted `TotalCharges` from text to numeric.
* Checked for missing values and duplicate rows.
* Removed `customerID` because it is not useful for prediction.
* Converted `Churn` into binary values: `1 = Yes`, `0 = No`.

## Exploratory Data Analysis

Key findings:

* Overall churn rate: **26.5%**
* Month-to-month customers: **42.7% churn**
* Two-year contract customers: **2.8% churn**
* Electronic check users: **45.3% churn**
* Fiber optic users: **41.9% churn**
* Customers without OnlineSecurity or TechSupport showed substantially higher churn.
* Churned customers had lower average tenure and higher monthly charges.

## Preprocessing

* 80/20 stratified train-test split
* Numerical features: `StandardScaler`
* Categorical features: `OneHotEncoder`
* Preprocessing and model combined using `Pipeline`
* Class imbalance handled using balanced class weights / positive-class weighting

## Models

Three classification models were trained and compared:

* Logistic Regression
* Random Forest
* XGBoost

## Model Performance

| Model               | Accuracy | Precision | Recall |    F1 | ROC-AUC |
| ------------------- | -------: | --------: | -----: | ----: | ------: |
| Random Forest       |    0.769 |     0.547 |  0.762 | 0.637 |   0.843 |
| XGBoost             |    0.752 |     0.522 |  0.770 | 0.622 |   0.840 |
| Logistic Regression |    0.738 |     0.504 |  0.783 | 0.614 |   0.841 |

## Final Model

The **Random Forest** model was used as the final model.

* **Accuracy:** 76.9%
* **Recall:** 76.2%
* **F1-score:** 0.637
* **ROC-AUC:** 0.843

The model correctly identified **285 out of 374 actual churned customers** in the test set.

## Key Insights

* Contract type was an important predictor of churn.
* Month-to-month customers showed the highest churn rate.
* Customers with low tenure were more likely to churn.
* Higher monthly charges were associated with higher churn.
* OnlineSecurity and TechSupport were associated with lower churn.
* Electronic check and Fiber optic customers showed higher churn rates.

## Business Recommendations

* Encourage customers to move from month-to-month to long-term contracts.
* Focus retention strategies on new customers.
* Promote OnlineSecurity and TechSupport through bundles or trials.
* Encourage automatic payment methods.
* Investigate Fiber optic pricing and service quality.

## Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* XGBoost
* Matplotlib
* Seaborn
* Jupyter Notebook
* Streamlit

## Conclusion

This project demonstrates an end-to-end customer churn prediction workflow, from data cleaning and exploratory analysis to preprocessing, model comparison, evaluation, and final model selection.

The Random Forest model achieved a **ROC-AUC of 0.843**, providing a useful approach for identifying customers at higher risk of churn.
