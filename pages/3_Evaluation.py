from pathlib import Path

import pandas as pd
import streamlit as st
# Clear specific function's cache
if st.button('Reload Data'):
 load_dataset.clear() # Clears cache for this function only
 st.rerun() # Force immediate re-run
# Clear ALL caches
if st.button('Clear All Caches'):
 st.cache_data.clear()
 st.cache_resource.clear()
# Bust cache by passing a changing parameter
# (functions are re-run when any argument changes)
@st.cache_data
def load_versioned(path: str, version: int):
 file_path = Path(path)
 if file_path.exists():
  return pd.read_csv(file_path)
 return pd.DataFrame(
  {
   'feature_a': [1, 2, 3],
   'feature_b': [4, 5, 6],
   'label': [0, 1, 0],
  }
 )
df = load_versioned('data.csv', version=2) # version change = re-run




import streamlit as st
import pickle
import pandas as pd
import numpy as np
@st.cache_resource
def load_model():
 with open('models/disease_classifier.pkl', 'rb') as f:
    return pickle.load(f)
@st.cache_resource
def load_scaler():
 with open('models/scaler.pkl', 'rb') as f:
    return pickle.load(f)
model = load_model()
scaler = load_scaler()
st.title('Disease Risk Predictor')
with st.form('predict_form'):
 col1, col2 = st.columns(2)
 age = col1.number_input('Age', 18, 100, 45)
 glucose = col1.number_input('Glucose Level', 50, 300, 120)
 bmi = col2.number_input('BMI', 10.0, 60.0, 25.0)
 bp = col2.number_input('Blood Pressure', 40, 200, 80)
 submitted = st.form_submit_button('Predict Risk', type='primary')
if submitted:
 features = np.array([[age, glucose, bmi, bp]])
 scaled = scaler.transform(features)
 prob = model.predict_proba(scaled)[0][1]
 label = 'High Risk' if prob > 0.5 else 'Low Risk'
 col1, col2 = st.columns(2)
 col1.metric('Prediction', label)
 col2.metric('Probability', f'{prob:.1%}')
 if prob > 0.5:
    st.error(f'High risk detected ({prob:.1%} confidence). Consult a physician.')
 else:
    st.success(f'Low risk ({1-prob:.1%} confidence). Continue healthy habits.')

import streamlit as st
import numpy as np
from PIL import Image
@st.cache_resource
def load_keras_model():
 import tensorflow as tf
 return tf.keras.models.load_model('models/cnn_classifier.h5')
CLASS_NAMES = ['Healthy', 'Pneumonia', 'COVID-19']
st.title('Chest X-Ray Classifier')
uploaded = st.file_uploader('Upload X-Ray Image',
 type=['jpg','png','jpeg'])
if uploaded:
 img = Image.open(uploaded).convert('RGB')
 st.image(img, caption='Uploaded X-Ray', use_container_width=True)
 if st.button('Classify', type='primary'):
    with st.spinner('Analysing image...'):
        model = load_keras_model()
 arr = np.array(img.resize((224, 224))) / 255.0
 arr = np.expand_dims(arr, axis=0)
 pred = model.predict(arr)[0]
 st.subheader('Classification Results')
 for cls, conf in zip(CLASS_NAMES, pred):
    st.metric(cls, f'{conf:.1%}')
 st.progress(float(conf))


import streamlit as st
st.title(':robot_face: FYP Research Assistant')
# Initialise message history
if 'messages' not in st.session_state:
 st.session_state.messages = []
# Display message history
for msg in st.session_state.messages:
 with st.chat_message(msg['role']):
    st.markdown(msg['content'])
# Chat input (appears at bottom of page)
if prompt := st.chat_input('Ask about your FYP data...'):
 # Add user message
 st.session_state.messages.append({'role':'user','content':prompt})
 with st.chat_message('user'):
    st.markdown(prompt)
 # Generate and display assistant response
 with st.chat_message('assistant'):
    with st.spinner('Thinking...'):
 # response = your_llm_call(prompt)
        response = f'You asked: "{prompt}" — (connect your LLM here)'
 st.markdown(response)
 st.session_state.messages.append(
 {'role':'assistant','content':response})






