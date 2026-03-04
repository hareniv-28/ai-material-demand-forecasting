import pandas as pd
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error
import numpy as np

def train_model(df_features):
    """
    Trains Random Forest model and returns trained model + evaluation metrics
    """

    # Define target and features
    X = df_features.drop(columns=["date", "material", "demand"])
    y = df_features["demand"]

    # Train-test split (last 20% as test)
    split_index = int(len(df_features) * 0.8)

    X_train, X_test = X[:split_index], X[split_index:]
    y_train, y_test = y[:split_index], y[split_index:]

    # Model
    model = RandomForestRegressor(
        n_estimators=200,
        max_depth=8,
        random_state=42
    )

    model.fit(X_train, y_train)

    # Predictions
    predictions = model.predict(X_test)

    # Metrics
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))

    return model, mae, rmse
def forecast_future(model, df_features, forecast_horizon=8):
    """
    Recursive 8-week forecasting
    """
    df_temp = df_features.copy()

    future_predictions = []

    for _ in range(forecast_horizon):
        X_last = df_temp.drop(columns=["date", "material", "demand"]).iloc[-1:]
        next_pred = model.predict(X_last)[0]

        future_predictions.append(next_pred)

        # Create new row
        new_row = df_temp.iloc[-1:].copy()
        new_row["demand"] = next_pred

        # Update lag features
        new_row["lag_1"] = df_temp.iloc[-1]["demand"]
        new_row["lag_2"] = df_temp.iloc[-1]["lag_1"]
        new_row["lag_4"] = df_temp.iloc[-1]["lag_2"]
        new_row["rolling_mean_4"] = (
            df_temp["demand"].iloc[-4:].mean()
        )

        df_temp = pd.concat([df_temp, new_row], ignore_index=True)

    return future_predictions