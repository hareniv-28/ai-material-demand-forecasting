import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
from backend.pipeline import run_pipeline


def model_insights_page():

    st.markdown("## Model Insights")

    st.markdown(
        """
        This page shows forecasting model performance and system explanation.
        """
    )

    st.markdown("---")

    # Run model once to get metrics
    result = run_pipeline("Transformer", 50)

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            label="MAE (Mean Absolute Error)",
            value=result["mae"]
        )

    with col2:
        st.metric(
            label="RMSE (Root Mean Squared Error)",
            value=result["rmse"]
        )

    st.markdown("---")

    st.subheader("Model Description")

    st.write(
        """
        The forecasting engine uses a **Random Forest Regressor** trained on
        historical demand data with engineered features such as lag demand
        and rolling averages.

        Forecasts are generated recursively for the next **8 weeks**.

        The predicted demand is then used to compute inventory decisions using:

        - Economic Order Quantity (EOQ)
        - Reorder Point (ROP)
        - Safety Stock
        """
    )