from .model import HouseFeatures
from fastapi import FastAPI, status, Query
from fastapi.responses import JSONResponse
from pathlib import Path
import joblib
import pandas as pd

ROOT_PATH = Path(__file__).resolve().parents[1]
MODEL_PATH = ROOT_PATH / "model.joblib"

model = joblib.load(MODEL_PATH)


app = FastAPI(
    title="House Prices prediction"
)



@app.post("/predict")
def predict(house_features: HouseFeatures):
    date = house_features.date
    
    sale_year = date.year
    sale_month = date.month
    
    house_age = sale_year - house_features.yr_built
    
    was_renovated = int(house_features.yr_renovated > 0)
    
    sqft_per_bedroom = (
        house_features.sqft_living / house_features.bedrooms
        if house_features.bedrooms != 0
        else 0
    )

    sqft_per_bathroom = (
        house_features.sqft_living / house_features.bathrooms
        if house_features.bathrooms != 0
        else 0
    )

    lot_size_per_sqft = (
        house_features.sqft_lot / house_features.sqft_living
        if house_features.sqft_living != 0
        else 0
    )
    
    data = {
        "bedrooms": house_features.bedrooms,
        "bathrooms": house_features.bathrooms,
        "sqft_living": house_features.sqft_living,
        "sqft_lot": house_features.sqft_lot,
        "floors": house_features.floors,
        "waterfront": house_features.waterfront,
        "view": house_features.view,
        "condition": house_features.condition,
        "grade": house_features.grade,
        "sqft_above": house_features.sqft_above,
        "sqft_basement": house_features.sqft_basement,
        "yr_built": house_features.yr_built,
        "yr_renovated": house_features.yr_renovated,
        "zipcode": house_features.zipcode,
        "lat": house_features.lat,
        "long": house_features.long,
        "sqft_living15": house_features.sqft_living15,
        "sqft_lot15": house_features.sqft_lot15,
        "sale_year": sale_year,
        "sale_month": sale_month,
        "house_age": house_age,
        "was_renovated": was_renovated,
        "sqft_per_bedroom": sqft_per_bedroom,
        "sqft_per_bathroom": sqft_per_bathroom,
        "lot_size_per_sqft": lot_size_per_sqft
    }
    
    df = pd.DataFrame([data])
    
    predict_value = model.predict(df)
    
    return {
        "price" : predict_value[0]
    }
