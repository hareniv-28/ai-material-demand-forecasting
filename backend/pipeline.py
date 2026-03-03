import pandas as pd
from feature_engineering import create_features
from model import train_model

def test_training(material_name):
    df = pd.read_csv("data/synthetic_data.csv")
    df["date"] = pd.to_datetime(df["date"])

    df_features = create_features(df, material_name)
    model, mae, rmse = train_model(df_features)

    print(f"Material: {material_name}")
    print(f"MAE: {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")

if __name__ == "__main__":
    test_training("Insulator")