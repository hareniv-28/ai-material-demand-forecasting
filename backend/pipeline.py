import pandas as pd
from backend.feature_engineering import create_features
from backend.model import train_model, forecast_future
from backend.inventory import calculate_inventory_metrics


def run_pipeline(material_name, current_inventory):

    df = pd.read_csv("data/synthetic_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    df_features = create_features(df, material_name)

    model, mae, rmse = train_model(df_features)

    forecast_values = forecast_future(model, df_features, forecast_horizon=8)

    inventory_results = calculate_inventory_metrics(
        material_name,
        forecast_values,
        current_inventory
    )

    return {
    "forecast_values": [float(x) for x in forecast_values],
    "mae": float(round(mae, 2)),
    "rmse": float(round(rmse, 2)),
    "eoq": float(inventory_results["eoq"]),
    "safety_stock": float(inventory_results["safety_stock"]),
    "reorder_point": float(inventory_results["reorder_point"]),
    "recommendation": inventory_results["recommendation"]
}


if __name__ == "__main__":
    result = run_pipeline("Transformer", current_inventory=200)
    print(result)