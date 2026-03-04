import streamlit as st


def login():

    st.markdown("""
    <style>

    .stApp {
        background: linear-gradient(135deg,#eef2f7,#dfe7f1);
    }

    .login-box {
        background:white;
        padding:40px;
        border-radius:12px;
        box-shadow:0px 6px 20px rgba(0,0,0,0.08);
        max-width:500px;
        margin:auto;
        margin-top:80px;
    }

    .title {
        text-align:center;
        font-size:38px;
        font-weight:700;
        color:#1f2937;
    }

    .subtitle {
        text-align:center;
        font-size:18px;
        color:#4b5563;
        margin-bottom:30px;
    }

    </style>
    """, unsafe_allow_html=True)

    st.markdown('<div class="title">AI Material Demand Forecasting</div>', unsafe_allow_html=True)
    st.markdown('<div class="subtitle">Power Utility Procurement Decision Support</div>', unsafe_allow_html=True)

    st.markdown("### Admin Login")

    username = st.text_input("Username")
    password = st.text_input("Password", type="password")

    if st.button("Login", use_container_width=True):

        if username == "admin" and password == "admin123123":
            st.session_state["authenticated"] = True
            st.rerun()

        else:
            st.error("Invalid credentials")