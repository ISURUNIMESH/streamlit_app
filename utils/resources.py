import streamlit as st
import pickle
@st.cache_resource # Shared across ALL users and sessions
def load_model(path: str):
 '''Load ML model once — shared across all users'''
 with open(path, 'rb') as f:
    return pickle.load(f)
@st.cache_resource
def get_db_connection():
 import sqlite3
 return sqlite3.connect('fyp_database.db', check_same_thread=False)
@st.cache_resource
def load_transformers_model(model_name: str):
 from transformers import pipeline
 return pipeline('text-classification', model=model_name)
# Model is loaded once and reused for all predictions
model = load_model('models/xgboost_classifier.pkl')
nlp = load_transformers_model('distilbert-base-uncased')


import streamlit as st
@st.cache_resource
def load_sentiment_pipeline():
 from transformers import pipeline
 return pipeline('sentiment-analysis',
 model='distilbert-base-uncased-finetuned-sst-2-english')
@st.cache_resource
def load_summariser():
 from transformers import pipeline
 return pipeline('summarization', model='facebook/bart-large-cnn')
tab1, tab2 = st.tabs(['Sentiment Analysis', 'Text Summarisation'])
with tab1:
 text = st.text_area('Enter review text', height=100)
 if st.button('Analyse Sentiment'):
    clf = load_sentiment_pipeline()
 result = clf(text)[0]
 emoji = ':green_heart:' if result['label']=='POSITIVE' else ':red_circle:'
 st.metric(f'{emoji} Sentiment', result['label'],
 f'Confidence: {result["score"]:.1%}')
with tab2:
 article = st.text_area('Paste article text', height=200)
 if st.button('Summarise'):
  ariser = load_summariser()
 summary = summariser(article, max_length=130, min_length=30)
 st.write(summary[0]['summary_text'])









