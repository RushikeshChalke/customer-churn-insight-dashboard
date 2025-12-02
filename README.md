# Customer Churn Insight Dashboard  
**Full-Stack | ML | Real-time Prediction System**  

Live demo runs in 30 seconds | 100K customers | Real churn model  

**Tech Stack**  
Python • Django • FastAPI • Pandas • Scikit-learn • HTML5 • CSS3 • Chart.js  

**Features**  
- 100K synthetic customer dataset + real Gradient Boosting model  
- Live churn prediction API (`POST /api/predict/`)  
- Responsive interactive dashboard with Chart.js  
- Django admin panel  

**Run locally**  
```bash
python -m venv venv && venv\Scripts\activate
pip install -r requirements.txt
python generate_data.py && python train_model.py
python manage.py migrate && python manage.py runserver
