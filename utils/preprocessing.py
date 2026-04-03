import streamlit as st
import pandas as pd
import time
@st.cache_data # Caches the return value
def load_dataset(filepath: str) -> pd.DataFrame:
 '''Loads CSV — cached so file is read only once'''
 time.sleep(2) # simulate slow IO
 df = pd.read_csv(filepath)
 return df
@st.cache_data(ttl=3600) # Cache expires after 1 hour
def fetch_live_data(api_url: str) -> dict:
 import requests
 return requests.get(api_url).json()
@st.cache_data(max_entries=5) # Limit cache size
def preprocess(df: pd.DataFrame, scaler_type: str) -> pd.DataFrame:
 # heavy preprocessing
 return df
# Usage — only runs once; subsequent calls return cached result
df = load_dataset('data/medical_records.csv')
st.dataframe(df.head())