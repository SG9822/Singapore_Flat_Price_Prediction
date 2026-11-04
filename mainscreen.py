import streamlit as st
from streamlit_option_menu import option_menu
from home import  home
from stats import  stats
from predictor import predictor

st.set_page_config(
    page_title="Singapore Flat Price Predictor",  # Title for browser tab
    page_icon="🏘️",
    layout="wide",
    initial_sidebar_state="expanded"  # optional
)

select = option_menu(
        menu_title=None,
        options=["Home", "Stats" ,'Price Predictor'],
        icons=["house", "pie-chart-fill","currency-dollar"],
        menu_icon=None,
        default_index=0,
        orientation="horizontal", )

if select == "Home":
    home()

elif select == "Stats":
    stats()

elif select == "Price Predictor":
    predictor()