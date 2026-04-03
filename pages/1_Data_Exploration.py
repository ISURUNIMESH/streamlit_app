import streamlit as st
import pandas as pd
import time
from pathlib import Path


@st.cache_data # Caches the return value
def load_dataset(filepath: str) -> pd.DataFrame:
 '''Loads CSV — cached so file is read only once'''
 time.sleep(2) # simulate slow IO
 path = Path(filepath)
 if path.exists():
  return pd.read_csv(path)
 return pd.DataFrame(
  {
   'age': [34, 51, 28, 62],
   'income': [42000, 58000, 36000, 72000],
   'label': [0, 1, 0, 1],
  }
 )


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
if not Path('data/medical_records.csv').exists():
 st.info('Using demo data because data/medical_records.csv is missing.')
st.dataframe(df.head())
