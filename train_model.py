import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import GradientBoostingClassifier
import joblib

df = pd.read_csv("data/customers.csv")
X = df[['age','tenure_months','monthly_charges','total_charges']]
y = df['churn']

model = GradientBoostingClassifier(n_estimators=100, random_state=42)
model.fit(X, y)

joblib.dump(model, "data/churn_model.pkl")
print("Model trained & saved → data/churn_model.pkl")
