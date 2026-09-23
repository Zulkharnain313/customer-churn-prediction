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

## Key Insights
- [Write your real top insight from Phase 5/12, e.g. contract type]
- Customers who churn tend to have much lower tenure than those who stay.
- [Add 1-2 more from your own EDA/coefficient findings]

## Business Recommendations
- Focus retention offers on customers in their first 12 months.
- Consider incentives for month-to-month customers to move to longer contracts.

## Tech Stack
Python, Pandas, NumPy, Scikit-learn, XGBoost, imbalanced-learn (SMOTE), Matplotlib, Seaborn, Streamlit, Joblib

## Run It Yourself
\`\`\`
pip install -r requirements.txt
streamlit run app.py
\`\`\`

## Live Demo
[link once deployed — see below]