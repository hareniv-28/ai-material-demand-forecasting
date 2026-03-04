import numpy as np

# Fixed assumptions
LEAD_TIME = 2
SERVICE_LEVEL_Z = 1.65
ORDERING_COST = 5000
HOLDING_RATE = 0.20

UNIT_COST = {
    "Transformer": 50000,
    "Cable": 2000,
    "Insulator": 500
}

def calculate_inventory_metrics(material, forecast_values, current_inventory):

    avg_forecast = np.mean(forecast_values)
    std_forecast = np.std(forecast_values)

    # Annual demand estimate
    annual_demand = avg_forecast * 52

    holding_cost = HOLDING_RATE * UNIT_COST[material]

    # EOQ
    eoq = np.sqrt((2 * annual_demand * ORDERING_COST) / holding_cost)

    # Lead Time Demand
    ltd = avg_forecast * LEAD_TIME

    # Safety Stock
    safety_stock = SERVICE_LEVEL_Z * std_forecast

    # Reorder Point
    reorder_point = ltd + safety_stock

    # Recommendation
    if current_inventory < reorder_point:
        recommendation = f"Reorder Recommended: Order approximately {int(eoq)} units."
    else:
        recommendation = "Inventory sufficient. No immediate order required."

    return {
        "eoq": round(eoq, 2),
        "safety_stock": round(safety_stock, 2),
        "reorder_point": round(reorder_point, 2),
        "recommendation": recommendation
    }