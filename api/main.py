from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
import joblib
from pathlib import Path
from .model import HouseFeatures
import pandas as pd

ROOT_DIR = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT_DIR / "model.joblib"

app = FastAPI(
    title="House Price Prediction API",
    description="API for predicting house prices",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=[
        "http://0.0.0.0:5500",
        "http://127.0.0.1:5500",
        "http://localhost:5500",
    ],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

model = joblib.load(MODEL_PATH)


@app.get("/")
def root():
    return {
        "message": "House Price Prediction API is running!"
    }
    
@app.post("/predict")
def predict(features: HouseFeatures):
    date = features.date
    
    sale_year = date.year
    sale_month = date.month
    
    house_age = sale_year - features.yr_built
    
    was_renovated = int(features.yr_renovated > 0)
    
    sqft_per_bedroom = (
        features.sqft_living / features.bedrooms
        if features.bedrooms != 0
        else 0
    )

    sqft_per_bathroom = (
        features.sqft_living / features.bathrooms
        if features.bathrooms != 0
        else 0
    )

    lot_size_per_sqft = (
        features.sqft_lot / features.sqft_living
        if features.sqft_living != 0
        else 0
    )
    
    data = {
        "bedrooms": features.bedrooms,
        "bathrooms": features.bathrooms,
        "sqft_living": features.sqft_living,
        "sqft_lot": features.sqft_lot,
        "floors": features.floors,
        "waterfront": features.waterfront,
        "view": features.view,
        "condition": features.condition,
        "grade": features.grade,
        "sqft_above": features.sqft_above,
        "sqft_basement": features.sqft_basement,
        "yr_built": features.yr_built,
        "yr_renovated": features.yr_renovated,
        "zipcode": features.zipcode,
        "lat": features.lat,
        "long": features.long,
        "sqft_living15": features.sqft_living15,
        "sqft_lot15": features.sqft_lot15,
        "sale_year": sale_year,
        "sale_month": sale_month,
        "house_age": house_age,
        "was_renovated": was_renovated,
        "sqft_per_bedroom": sqft_per_bedroom,
        "sqft_per_bathroom": sqft_per_bathroom,
        "lot_size_per_sqft": lot_size_per_sqft
    }

    input_df = pd.DataFrame([data])
    
    prediction = model.predict(input_df)

    return {
        "predicted_price": prediction[0]
    }