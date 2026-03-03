import pandas as pd

def create_features(df, material_name):
    """
    Creates lag and rolling features for a specific material.
    """

    df_material = df[df["material"] == material_name].copy()
    df_material = df_material.sort_values("date")

    # Lag features
    df_material["lag_1"] = df_material["demand"].shift(1)
    df_material["lag_2"] = df_material["demand"].shift(2)
    df_material["lag_4"] = df_material["demand"].shift(4)

    # Rolling mean
    df_material["rolling_mean_4"] = df_material["demand"].rolling(window=4).mean()

    # Drop rows with NaN (due to lagging)
    df_material = df_material.dropna()

    return df_material