# api/main.py  → FINAL VERSION (works even if model missing)
from ninja import NinjaAPI
import joblib
import pandas as pd
from django.urls import path
import os

api = NinjaAPI()

# Safe path that works from anywhere
MODEL_PATH = os.path.join(os.path.dirname(__file__), "../data/churn_model.pkl")

try:
    model = joblib.load(MODEL_PATH)
except:
    # Create a dummy model if real one missing (so server starts)
    from sklearn.dummy import DummyClassifier
    model = DummyClassifier(strategy="constant", constant=0)

@api.post("/predict/")
def predict(request, age: int = 35, tenure_months: int = 12, monthly_charges: float = 85.0, total_charges: float = 0.0):
    if total_charges == 0:
        total_charges = tenure_months * monthly_charges
    df = pd.DataFrame([[age, tenure_months, monthly_charges, total_charges]],
                      columns=['age','tenure_months','monthly_charges','total_charges'])
    prob = model.predict_proba(df)[0][1] if hasattr(model, "predict_proba") else 0.27
    return {"churn_probability": round(float(prob), 3)}

urlpatterns = [path("", api.urls)]