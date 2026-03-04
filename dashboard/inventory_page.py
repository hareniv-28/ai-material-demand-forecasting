import streamlit as st
import pandas as pd


def inventory_page():

    st.markdown("## Inventory Tracking")

    st.info(
        "Monitor current inventory levels and identify materials approaching reorder thresholds."
    )

    st.markdown("---")

    data = {
        "Material": ["Transformer", "Cable", "Insulator"],
        "Current Stock": [50, 120, 200],
        "Reorder Point": [46, 100, 150],
        "Status": ["Safe", "Safe", "Safe"]
    }

    df = pd.DataFrame(data)

    st.dataframe(df, use_container_width=True)