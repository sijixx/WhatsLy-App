import streamlit as st
from multiapp import MultiApp
import pandas as pd
import requests
from streamlit_lottie import st_lottie
from apps import home, dashboard # import your app modules here

st.set_page_config(page_title='Welcome to WhatsLy', page_icon= ':speech_balloon:', layout='wide')

app = MultiApp()

# Add all your application here
app.add_app("Dashboard", dashboard.app)
app.add_app("Home", home.app)


# The main app
app.run()

