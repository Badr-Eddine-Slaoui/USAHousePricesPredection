import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error, mean_squared_error, root_mean_squared_error, r2_score

print("Loading DataFrame from CSV file...")
df = pd.read_csv("kc_house_data.csv")
print("DataFrame loaded successfully.")

print("\n--------------------------------------------\n")
print("DataFrame head:")
print(df.head())
print("\n--------------------------------------------\n")

print("DataFrame shape:")
print(df.shape)
print("\n--------------------------------------------\n")

print("DataFrame columns:")
print(df.columns)
print("\n--------------------------------------------\n")

print("DataFrame info:")
print(df.info())
print("\n--------------------------------------------\n")

print("DataFrame describe:")
print(df.describe())
print("\n--------------------------------------------\n")
print("DataFrame null values count:")
missing = df.isnull().sum()
print(missing)
print("\n--------------------------------------------\n")

print("DataFrame null values percentage:")
missing_percentage = (missing / len(df)) * 100
print(missing_percentage)
print("\n--------------------------------------------\n")
print("Converting 'date' column to datetime type...")
df["date"] = pd.to_datetime(df["date"])

print("Extracting year and month from 'date' column...")
df["sale_year"] = df["date"].dt.year
df["sale_month"] = df["date"].dt.month

print("Adding 'house_age' column...")
df["house_age"] = df["sale_year"] - df["yr_built"]

print("Adding 'was_renovated' column...")
df["was_renovated"] = (df["yr_renovated"] > 0).astype(int)

print("Adding 'sqft_per_bedroom' column...")
df["sqft_per_bedroom"] = (
    df["sqft_living"] / df["bedrooms"].replace(0, np.nan)
)

print("Adding 'sqft_per_bathroom' column...")
df["sqft_per_bathroom"] = (
    df["sqft_living"] / df["bathrooms"].replace(0, np.nan)
)

print("Adding 'lot_size_per_sqft' column...")
df["lot_size_per_sqft"] = (
    df["sqft_lot"] / df["sqft_living"].replace(0, np.nan)
)

print("\n--------------------------------------------\n")
FEATURES = [
    "bedrooms",
    "bathrooms",
    "sqft_living",
    "sqft_lot",
    "floors",
    "waterfront",
    "view",
    "condition",
    "grade",
    "sqft_above",
    "sqft_basement",
    "yr_built",
    "yr_renovated",
    "zipcode",
    "lat",
    "long",
    "sqft_living15",
    "sqft_lot15",
    "sale_year",
    "sale_month",
    "house_age",
    "was_renovated",
    "sqft_per_bedroom",
    "sqft_per_bathroom",
    "lot_size_per_sqft"
]

TARGET = "price"

df[FEATURES] = df[FEATURES].fillna(0)

x = df[FEATURES]
y = df[TARGET]

print("Splitting data into training and testing sets...")
x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.2, random_state=42)
print("Data split completed.")
print("\n--------------------------------------------\n")
print("Training Linear Regression model...")
model = LinearRegression()
model.fit(x_train, y_train)
print("Model training completed.")
print("\n--------------------------------------------\n")
print("Making predictions on the test set...")
y_pred = model.predict(x_test)
print("Predictions completed.")
print("\n--------------------------------------------\n")

comparison = pd.DataFrame({
    "actual": y_test.values,
    "predicted": y_pred
})

print("Comparison of actual and predicted values:")
print(comparison.head(10))
print("\n--------------------------------------------\n")

print("Model Evaluation Metrics:")
mae = mean_absolute_error(y_test, y_pred)
mse = mean_squared_error(y_test, y_pred)
rmse = root_mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)
print(f"Mean Absolute Error (MAE): {mae}")
print(f"Mean Squared Error (MSE): {mse}")
print(f"Root Mean Squared Error (RMSE): {rmse}")
print(f"R-squared (R2): {r2}")
print("\n--------------------------------------------\n")
coefficients = pd.DataFrame({
    "feature": x.columns,
    "coefficient": model.coef_
})

print("Model coefficients:")
print(coefficients)
print("\n--------------------------------------------\n")

print("Intercept:", model.intercept_)
print("\n--------------------------------------------\n")
