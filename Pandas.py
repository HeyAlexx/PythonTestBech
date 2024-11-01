import pandas as pd
import openpyxl
import string
import plotly.express as px
import streamlit as st


st.set_page_config(page_title="tetst page",
                   page_icon="bar_chart:",
                   layout="wide")




path1 = (r"C:\Users\Alvar\OneDrive\Anime Datas.xlsx")

df = pd.read_excel(path1,engine='openpyxl',
                   sheet_name="Catalogo",
                   usecols='B:N',
                   nrows=20000)

st.dataframe(df)

#use this to run it   ----->  streamlit run Pandas.py

