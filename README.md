# USA House Prices Prediction (HousePredict)

An end-to-end Machine Learning web application designed to estimate residential property market values in King County, USA. The project incorporates an end-to-end data pipeline: exploratory data analysis, feature engineering, linear regression model training and evaluation, an asynchronous FastAPI backend service, and a modern glassmorphic web interface.

---

## Architecture Overview

```
USAHousePricesPredection/
├── kc_house_data.csv        # King County housing dataset (21k+ records)
├── train.py                 # Data preprocessing, feature engineering & model training
├── model.joblib             # Serialized trained scikit-learn LinearRegression model
├── api/
│   ├── __init__.py          # API package marker
│   ├── model.py             # Pydantic schema for request validation (HouseFeatures)
│   └── main.py              # FastAPI application, CORS middleware & /predict endpoint
├── frontend/
│   ├── index.html           # Modern UI with responsive property details form
│   ├── style.css            # Dark mode glassmorphism styling, ambient orbs & animations
│   └── script.js            # Dynamic form handling, API integration & price formatting
└── .gitignore               # Excludes virtualenvs, bytecode, and temporary files
```

---

## Features & Highlights

- **Comprehensive Feature Engineering**:
  - Temporal decomposition: parses sale date to extract `sale_year` and `sale_month`.
  - Property age: computes `house_age = sale_year - yr_built`.
  - Renovation indicator: derives binary `was_renovated` flag from `yr_renovated`.
  - Spatial and room ratios: calculates `sqft_per_bedroom`, `sqft_per_bathroom`, and `lot_size_per_sqft`.
- **Model Evaluation**:
  - Linear Regression baseline evaluated on an 80/20 train/test split.
  - Metrics tracked: Mean Absolute Error (MAE), Mean Squared Error (MSE), Root Mean Squared Error (RMSE), and R² Score.
  - Feature coefficient and intercept explainability.
- **Production-Ready REST API**:
  - Built with **FastAPI** and **Pydantic** for automatic input validation and serialization.
  - Runtime feature transformation mirrors training pipeline logic.
  - Configured with CORS middleware for local frontend development.
- **Modern User Interface**:
  - Responsive multi-section form covering basic details, property quality, construction specs, coordinates, and neighborhood metrics.
  - Glassmorphic card design with subtle micro-animations and loading spinners.
  - Formatted currency presentation using the JavaScript Internationalization API (`Intl.NumberFormat`).

---

## Tech Stack

- **Machine Learning & Data Processing**: Python 3, Pandas, NumPy, Scikit-Learn, Joblib
- **API & Backend**: FastAPI, Uvicorn, Pydantic
- **Frontend**: HTML5, TailwindCSS (CDN), Vanilla CSS3, Modern JavaScript (ES6+)

---

## Getting Started

### 1. Prerequisites
- Python 3.10+
- Node.js / Live Server (optional, for hosting the frontend)

### 2. Environment Setup

Create and activate a Python virtual environment:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Install the required dependencies:

```bash
pip install pandas numpy scikit-learn joblib fastapi uvicorn pydantic
```

### 3. Model Training

Train the regression model and generate `model.joblib`:

```bash
python train.py
```

### 4. Running the API

Start the FastAPI application with Uvicorn:

```bash
uvicorn api.main:app --reload --host 127.0.0.1 --port 8000
```

The interactive API documentation (Swagger UI) will be available at:
- `http://127.0.0.1:8000/docs`

### 5. Launching the Frontend

Serve the `frontend/` directory using any static file server (such as Python's HTTP server or VS Code Live Server):

```bash
# Using Python's built-in HTTP server on port 5500
python3 -m http.server 5500 --directory frontend
```

Open your browser and navigate to `http://localhost:5500`.

---

## API Endpoints

### `GET /`
Health check endpoint returning API status.

**Response:**
```json
{
  "message": "House Price Prediction API is running!"
}
```

### `POST /predict`
Predicts property market value based on input features.

**Sample Request Body:**
```json
{
  "bedrooms": 3,
  "bathrooms": 2.5,
  "sqft_living": 1800,
  "sqft_lot": 5000,
  "floors": 1.5,
  "waterfront": 0,
  "view": 0,
  "condition": 3,
  "grade": 7,
  "sqft_above": 1800,
  "sqft_basement": 0,
  "yr_built": 1990,
  "yr_renovated": 0,
  "zipcode": 98103,
  "lat": 47.68,
  "long": -122.35,
  "sqft_living15": 1700,
  "sqft_lot15": 5000,
  "date": "2014-10-13T00:00:00"
}
```

**Sample Response:**
```json
{
  "predicted_price": 542310.45
}
```

---

## License

This project is open-source under the MIT License.
