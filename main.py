import streamlit as st
from ui import home, dashboard

st.set_page_config(page_title="FitTrack", layout="wide")

page = st.sidebar.selectbox("Navigation", ["Accueil", "Tableau de bord"])

if page == "Accueil":
    home.show()
elif page == "Tableau de bord":
    dashboard.show()

