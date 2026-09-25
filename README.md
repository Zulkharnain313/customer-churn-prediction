# Customer Churn Prediction

Predicts whether a telecom customer will churn, using their account and service details, so the company can target retention efforts at high-risk customers.

## Problem
Customer churn costs more to fix after the fact than to prevent. This project identifies customers likely to leave so the business can intervene early.

## Dataset
Telco Customer Churn dataset (Kaggle, BlastChar) — 7,043 customers, 21 features.

## Approach
1. Cleaned data (fixed TotalCharges type, removed 11 rows with missing billing history)
2. Exploratory data analysis on churn by contract type, tenure, internet service, and payment method
3. One-hot encoded categorical features, scaled numeric features
4. Balanced the training data with SMOTE (original churn rate ~27%)
5. Trained and compared Logistic Regression, Random Forest, and XGBoost
6. Evaluated using ROC-AUC and recall (recall matters most: missing a churner is costlier than a false alarm)
7. Interpreted the model using coefficient analysis
8. Deployed as an interactive Streamlit app

## Results
| Model | ROC-AUC |
|---|---|
| **Logistic Regression** | **0.820** |
| Random Forest | 0.815 |
| XGBoost | 0.809 |

Logistic Regression performed best, suggesting the churn signal in this dataset is largely linear.
## Screenshots

**App Interface**
![App interface](images/app-interface.png)

**Prediction Result**
![Prediction result](images/prediction-result.png)

**Churn by Contract Type**
![Churn by contract type](images/Churn-by-contract-type.png)

**model comparison table**
![model comparison table](images/model-comparison-table.png)

**Evaluation of models**
![Evaluation of models](images/Evaluation-of-models.png)


## Key Insights
## Key Insights
- Customers on month-to-month contracts churn far more than those on one or two-year contracts, since they face no penalty for leaving at any time.
- Customers who churn tend to have much lower tenure than those who stay, meaning the first several months are the highest-risk period for losing a customer.
- Customers with fiber optic internet churn more than those with DSL, likely due to higher monthly costs and more competition in that market segment.
- Customers paying by electronic check churn more than those on automatic payment methods (credit card or bank transfer), possibly reflecting less commitment to staying with the service.

## Business Recommendations
- Focus retention offers on customers in their first 12 months.
- Consider incentives for month-to-month customers to move to longer contracts.

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, XGBoost, imbalanced-learn (SMOTE), Matplotlib, Seaborn, Streamlit, Joblib

## Future improvements
-Try Random Forest / XGBoost with hyperparameter tuning
-Handle class imbalance (SMOTE or class weights)
-Deploy the app on Streamlit Community Cloud

## Run It Yourself
\`\`\`
```bash
git clone https://github.com/Zulkharnain313/customer-churn-prediction.git
cd customer-churn-prediction
pip install -r requirements.txt
streamlit run app.py
\`\`\`

## Live Demo
[[link once deployed — see below](https://customer-churn-prediction-apptkyhp69k8x8q8ernwlt.streamlit.app/)]

## Future improvements
-Try Random Forest / XGBoost with hyperparameter tuning
-Handle class imbalance (SMOTE or class weights)
-Deploy the app on Streamlit Community Cloud