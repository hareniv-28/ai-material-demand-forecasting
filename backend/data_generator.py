import pandas as pd
import numpy as np

def generate_synthetic_data():
    np.random.seed(42)

    materials = {
        "Transformer": 20,
        "Cable": 100,
        "Insulator": 60
    }

    weeks = pd.date_range(start="2021-01-01", periods=156, freq="W")

    all_data = []

    for material, base_demand in materials.items():
        for date in weeks:
            month = date.month
            week_number = date.week

            monsoon_flag = 1 if month in [6, 7, 8, 9] else 0
            outage_count = np.random.poisson(2)
            maintenance_flag = np.random.choice([0, 1], p=[0.7, 0.3])

            seasonal_wave = 10 * np.sin(2 * np.pi * week_number / 52)
            monsoon_effect = 15 * monsoon_flag
            outage_effect = 3 * outage_count
            random_noise = np.random.normal(0, 5)

            demand = (
                base_demand
                + seasonal_wave
                + monsoon_effect
                + outage_effect
                + random_noise
            )

            demand = max(0, round(demand))

            all_data.append([
                date,
                material,
                demand,
                month,
                week_number,
                monsoon_flag,
                outage_count,
                maintenance_flag
            ])

    df = pd.DataFrame(all_data, columns=[
        "date",
        "material",
        "demand",
        "month",
        "week",
        "monsoon_flag",
        "outage_count",
        "maintenance_flag"
    ])

    return df


if __name__ == "__main__":
    df = generate_synthetic_data()
    df.to_csv("data/synthetic_data.csv", index=False)
    print("Synthetic dataset generated successfully.")