import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_absolute_error
import numpy as np
from data import get_pedestrian_data

def train_model():
    df = get_pedestrian_data()

    df["sensing_date"] = pd.to_datetime(df["sensing_date"])
    df["day"] = df["sensing_date"].dt.day
    df["month"] = df["sensing_date"].dt.month
    df["hour"] = df["hourday"]

    features = ["day", "month", "hour"]
    target = "pedestriancount"

    X = df[features]
    y = df[target]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    model = LinearRegression()
    model.fit(X_train, y_train)

    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    print(f"Model trained! Mean Absolute Error: {mae:.0f} pedestrians")

    return model

def predict_traffic(model, day, month, hour):
    input_data = pd.DataFrame([[day, month, hour]], columns=["day", "month", "hour"])
    prediction = model.predict(input_data)
    return int(prediction[0])

if __name__ == "__main__":
    model = train_model()
    prediction = predict_traffic(model, day=15, month=6, hour=9)
    print(f"Predicted pedestrians: {prediction:,}")
