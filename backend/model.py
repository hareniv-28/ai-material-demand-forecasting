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