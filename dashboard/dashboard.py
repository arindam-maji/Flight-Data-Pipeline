import mysql.connector
import pandas as pd
import streamlit as st

DB_CONFIG = {
    'host': 'localhost',
    'user': 'arindam',
    'password': 'Arindam@81',
    'database': 'flights_db'
}

st.title("✈ Flight Data Dashboard")

def get_data():
    conn = mysql.connector.connect(**DB_CONFIG)
    df = pd.read_sql("SELECT * FROM flights", conn)
    conn.close()
    return df

df = get_data()
st.dataframe(df)
