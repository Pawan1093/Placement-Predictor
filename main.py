from fastapi import FastAPI , Request , Form
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
import pickle
import numpy as np

app = FastAPI(title="Student Placment Predictor")
templates = Jinja2Templates(directory="templates")


with open('knn_model.pkl' , 'rb') as f:
    knn_data = pickle.load(f)
    knn_model = knn_data['model']
    scaler = knn_data['scaler']

with open('lr_model.pkl','rb') as f:
    lr_model = pickle.load(f)

@app.get("/" , response_class=HTMLResponse)
async def home(request : Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/predict", response_class=HTMLResponse)
async def predict(
    request: Request,
    cgpa: float = Form(...),
    aptitude_score: int = Form(...),
    communication_score: int = Form(...),
    projects_done: int = Form(...),
    internship: int = Form(...)
):
    input_data = np.array([[
        cgpa, aptitude_score,
        communication_score,
        projects_done, internship
    ]])

    input_scaled = scaler.transform(input_data)
    placement_pred = knn_model.predict(input_scaled)[0]
    placement_proba = knn_model.predict_proba(input_scaled)[0]
    placement_chance = round(placement_proba[1] * 100, 1)

    salary_pred = lr_model.predict(input_data)[0]
    salary_pred = round(max(salary_pred, 1.8), 2)
    result = {
        "placed": "✅ PLACED" if placement_pred == 1 else "❌ NOT PLACED",
        "placement_chance": placement_chance,
        "salary": salary_pred,
        "cgpa": cgpa,
        "aptitude_score": aptitude_score,
        "communication_score": communication_score,
        "projects_done": projects_done,
        "internship": "Yes" if internship == 1 else "No"
    }
    
    return templates.TemplateResponse(
        "index.html",
        {"request": request, "result": result}
    )