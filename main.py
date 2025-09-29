import streamlit as st
from ui import home, dashboard

st.set_page_config(page_title="FitTrack", layout="wide")

page = st.sidebar.selectbox("Navigation", ["Accueil", "Tableau de bord"])

if page == "Accueil":
    home.show()
elif page == "Tableau de bord":
    dashboard.show()
import os

api_key = os.getenv("API_KEY")
db_url = os.getenv("DB_URL")
admin_email = os.getenv("ADMIN_EMAIL")

# Exemple d’utilisation
print(f"Connexion à la base : {db_url}")
