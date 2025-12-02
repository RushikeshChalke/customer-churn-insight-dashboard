# generate_data.py  →  NO JAVA / NO PYSPARK VERSION  (works instantly)
import pandas as pd
import numpy as np
import os

print("Generating 100,000 customer records...")

np.random.seed(42)
n = 100000

data = pd.DataFrame({
    'customer_id': range(1, n+1),
    'age': np.random.randint(18, 70, n),
    'tenure_months': np.random.randint(1, 72, n),
    'monthly_charges': np.random.uniform(20, 120, n).round(2),
    'total_charges': 0.0,
    'churn': np.random.choice([0, 1], n, p=[0.73, 0.27])
})

data['total_charges'] = (data['tenure_months'] * data['monthly_charges']).round(2)

# Create folder + save files
os.makedirs("data", exist_ok=True)
data.to_csv("data/customers.csv", index=False)

print("100K customer data generated → data/customers.csv")
print("No Java needed – ready to go!")