import streamlit as st
from streamlit_option_menu import option_menu

from login import login
from forecast_page import forecast_page
from model_insights_page import model_insights_page
from inventory_page import inventory_page
import pathlib
import streamlit as st

import pathlib
import streamlit as st


def load_css():
    css_path = pathlib.Path(".streamlit/styles.css")
    with open(css_path) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


load_css()


st.set_page_config(
    page_title="AI Material Forecasting",
    layout="wide"
)

if "authenticated" not in st.session_state:
    st.session_state["authenticated"] = False


if not st.session_state["authenticated"]:

    login()

else:
    with st.sidebar:
        st.markdown(" ## Power Utility AI")
        st.caption("Material Demand Forecasting & Procurement Support")
        st.markdown("---")

        selected = option_menu(
            "Navigation",
            [
                "Forecast & Procurement",
                "Model Insights",
                "Inventory Tracking",
                "Logout"
            ],
            icons=["graph-up", "bar-chart", "boxes", "box-arrow-right"],
            default_index=0,
            styles={
                "container": {
                    "background-color": "#f6f9fc",
                    "padding": "10px",
                    "border-radius": "12px",
                },
                "nav-link": {
                    "font-size": "16px",
                    "text-align": "left",
                    "margin": "2px",
                    "border-radius": "6px",
                    "color": "#1f2937",
                },
                "nav-link-selected": {
                    "background-color": "#6b8ecb",
                    "color": "white",
                },
    }
)
    if selected == "Forecast & Procurement":
        forecast_page()

    elif selected == "Model Insights":
        model_insights_page()

    elif selected == "Inventory Tracking":
        inventory_page()

    elif selected == "Logout":
        st.session_state["authenticated"] = False
        st.rerun()