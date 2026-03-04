import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

from backend.pipeline import run_pipeline


def forecast_page():

    st.markdown("""
    <style>

    .stApp {
        background-color:#f4f7fb;
    }

    .metric-small {
        text-align:center;
        padding:10px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown("## Forecast & Procurement Decision")

    st.markdown("---")

    # INPUTS

    col1, col2, col3 = st.columns([3,3,2])

    with col1:
        material = st.selectbox(
            "Select Material",
            ["Transformer","Cable","Insulator"]
        )

    with col2:
        inventory = st.number_input(
            "Current Inventory",
            min_value=0,
            value=50
        )

    with col3:
        st.write("")
        st.write("")
        run_button = st.button("Run Forecast",use_container_width=True)

    if run_button:

        result = run_pipeline(material,inventory)

        st.markdown("---")

        # DECISION BANNER

        if "Reorder Recommended" in result["recommendation"]:
            st.error(result["recommendation"])
        else:
            st.success(result["recommendation"])

        st.markdown("---")

        # FORECAST CHART

        st.subheader("Demand Forecast")

        df = pd.read_csv("data/synthetic_data.csv")

        df_material = df[df["material"]==material].tail(20)

        forecast_values = result["forecast_values"]

        fig, ax = plt.subplots(figsize=(8,3))
        ax.plot(
            range(len(df_material)),
            df_material["demand"],
            marker="o",
            linewidth=2,
            color="#2563eb",
            label="Historical Demand"
            )
        forecast_x = range(len(df_material), len(df_material)+8)
        ax.plot(
            forecast_x,
            forecast_values,
            marker="o",
            linestyle="dashed",
            linewidth=2,
            color="#f59e0b",
            label="Forecast"
            )
        ax.set_xlabel("Weeks")
        ax.set_ylabel("Demand")
        ax.grid(True, linestyle="--", alpha=0.3)
        ax.legend()

        st.pyplot(fig)

        st.markdown("---")

        # PROCUREMENT METRICS (SMALLER)

        st.subheader("Procurement Metrics")

        c1,c2,c3,c4,c5 = st.columns([1,1,1,1,1])

        with c2:
            st.metric("EOQ",f"{result['eoq']:.2f}")

        with c3:
            st.metric("ROP",f"{result['reorder_point']:.2f}")

        with c4:
            st.metric("Safety Stock",f"{result['safety_stock']:.2f}")

        st.markdown("---")

        # FORECAST TABLE

        forecast_table = pd.DataFrame({
            "Week":[f"Week {i+1}" for i in range(8)],
            "Predicted Demand":[round(v,2) for v in forecast_values]
        })

        st.dataframe(forecast_table,use_container_width=True)