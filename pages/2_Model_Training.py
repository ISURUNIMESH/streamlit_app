# pages/2_Model_Training.py
import streamlit as st
import pickle
st.header('Model Training')
# Initialise shared state (safe to call on every page)
if 'trained_model' not in st.session_state:
 st.session_state.trained_model = None
if st.button('Train XGBoost', type='primary'):
 with st.spinner('Training...'):
 # model = XGBClassifier().fit(X_train, y_train)
 # st.session_state.trained_model = model
    st.session_state.trained_model = 'model_placeholder'
 st.success('Model trained and saved to session!')













