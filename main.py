from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Bienvenue sur l'API de Mafouz"

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app.run(host='0.0.0.0', port=port)

import streamlit as st
from ui import home, dashboard

st.set_page_config(page_title="FitTrack", layout="wide")

page = st.sidebar.selectbox("Navigation", ["Accueil", "Tableau de bord"])

if page == "Accueil":
    home.show()
elif page == "Tableau de bord":
    dashboard.show()
import os
