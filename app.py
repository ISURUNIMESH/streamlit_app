# Create app.py
import streamlit as st
st.set_page_config(
 page_title='FYP Demo',
 page_icon=':brain:',
 layout='wide', # 'centered' or 'wide'
 initial_sidebar_state='expanded'
)
st.title('Welcome to My FYP Application')
st.write('This is my Proof-of-Concept built with Streamlit 1.56.0')
# Run: streamlit run app.py
# Opens at http://localhost:8501

import streamlit as st
# Title, header, subheader — semantic hierarchy
st.title('Smart Disease Prediction Dashboard') # Largest — use once per page
st.header('Model Performance Overview') # Second level
st.subheader('Live Prediction Insights') # Third level
# Body text
st.text('Plain monospaced text')
st.write('Smart write — auto-detects type') # Most versatile
# Markdown (full GFM support)
st.markdown('''
## Markdown Section
- **Bold** and *italic* text
- `inline code` formatting
- [Link text](https://streamlit.io)
''')
# Code display with syntax highlighting
st.code('''
def predict(x):
 return model.predict(x)
''', language='python')
# LaTeX mathematical expressions
st.latex(r'\hat{y} = \sigma(W \cdot X + b)')
# Caption (small text for images/charts)
st.caption('Figure 1: Model architecture overview')


import streamlit as st
st.success('Model training completed successfully!')
st.info('Dataset loaded: 10,000 records found.')
st.warning('Missing values detected in 3 columns.')
st.error('ERROR: Model file not found at models/clf.pkl')
# Toast notification (appears temporarily — new in 1.32+)
st.toast('Predictions saved!', icon='✔')

def risky_operation():
 return 10 / 2

# Exception display with traceback
try:
 result = risky_operation()
except Exception as e:
 st.exception(e) # Shows full Python traceback in UI


import streamlit as st
col1, col2, col3, col4 = st.columns(4)
col1.metric(label='Accuracy', value='94.5%', delta='+2.1%')
col2.metric(label='Precision', value='91.2%', delta='-0.8%')
col3.metric(label='Recall', value='96.3%', delta='+1.5%')
col4.metric(label='F1 Score', value='93.7%', delta='+0.6%')
# delta_color controls arrow colour
# 'normal' = green up / red down (default)
# 'inverse' = red up / green down (for loss metrics)
# 'off' = no colour change
st.metric('Loss', '0.082', delta='-0.014', delta_color='inverse')



import streamlit as st
model_params = {
 'algorithm': 'Random Forest',
 'n_estimators': 200,
 'max_depth': 15,
 'accuracy': 0.945,
 'features': ['age', 'income', 'score']
}
# Pretty-printed, collapsible JSON tree
st.json(model_params)
# Or use write() — auto-detects dict
st.write(model_params)


import streamlit as st
# Text input
name = st.text_input('Enter your name', value='Student', max_chars=50)
# Password (hidden input)
api_key = st.text_input('API Key', type='password')
# Multi-line text area
notes = st.text_area('Research Notes', height=150,
 placeholder='Describe your methodology...')
# Number input (with step and bounds)
threshold = st.number_input('Classification Threshold',
 min_value=0.0, max_value=1.0,
 value=0.5, step=0.01,
 format='%.2f')
st.write(f'Classifying as positive if probability > {threshold}')

import streamlit as st
# Dropdown (single select)
model_type = st.selectbox('Select Model',
 options=['Logistic Regression', 'Random Forest',
 'SVM', 'Neural Network', 'XGBoost'],
 index=1) # Default: Random Forest
# Multi-select (returns list)
features = st.multiselect('Select Features',
 options=['age', 'income', 'education', 'score', 'region'],
 default=['age', 'income'])
# Radio buttons
split_method = st.radio('Train/Test Split Method',
 options=['Hold-out (80/20)', 'K-Fold CV', 'Stratified K-Fold'],
 horizontal=True) # horizontal=True available in 1.32+
# Checkbox
normalise = st.checkbox('Normalise features', value=True)
show_conf_matrix = st.checkbox('Show Confusion Matrix')


import streamlit as st
from datetime import date
# Single value slider
n_trees = st.slider('Number of Trees', min_value=10,
 max_value=500, value=100, step=10)
# Range slider (returns a tuple)
age_range = st.slider('Age Range Filter',
 min_value=18, max_value=80,
 value=(25, 55))
st.write(f'Filtering: {age_range[0]} to {age_range[1]} years')
# Date range slider
date_range = st.slider('Date Range',
 min_value=date(2020, 1, 1),
 max_value=date(2025, 12, 31),
 value=(date(2022, 1, 1), date(2024, 12, 31)))

import streamlit as st
# Standard button — returns True only on the click run
if st.button('Train Model', type='primary', key='train_model_top_btn'):
 with st.spinner('Training in progress...'):
 # model = train_model(data, params)
    st.success('Training complete!')
# Download button — triggers file download
import pandas as pd
df = pd.DataFrame({'col1': [1,2,3], 'col2': ['a','b','c']})
csv = df.to_csv(index=False)
st.download_button(
 label='Download Results as CSV',
 data=csv,
 file_name='predictions.csv',
 mime='text/csv'
)
# Link button (navigates to URL)
st.link_button('Open GitHub Repo',
 'https://github.com/ISURUNIMESH/streamlit_app')

import streamlit as st
from datetime import date, time
# Date picker
dob = st.date_input('Date of Birth', min_value=date(1950, 1, 1),
 max_value=date.today())
# Time picker
start_time = st.time_input('Start Time', value=time(9, 0))
# Single file upload
uploaded = st.file_uploader('Upload Dataset (CSV)',
 type=['csv', 'xlsx'])
if uploaded:
 import pandas as pd
 df = pd.read_csv(uploaded)
 st.success(f'Loaded {len(df)} rows, {len(df.columns)} columns')
 st.dataframe(df.head())
# Multiple file upload
images = st.file_uploader('Upload Images',
 type=['png','jpg','jpeg'],
 accept_multiple_files=True)
st.write(f'{len(images)} image(s) uploaded')


import streamlit as st
# Equal columns
col1, col2, col3 = st.columns(3)
col1.metric('Accuracy', '94.5%', '+2%')
col2.metric('Loss', '0.082', '-0.01', delta_color='inverse')
col3.metric('F1', '93.7%', '+1%')
# Custom ratio columns (weights)
left, right = st.columns([2, 1]) # left is twice as wide

results_df = {
 'Sample': ['A', 'B', 'C', 'D'],
 'Prediction': [0.92, 0.87, 0.95, 0.81],
 'Actual': [1, 1, 1, 0]
}

with left:
 st.subheader('Prediction Results')
 st.dataframe(results_df)
with right:
 st.subheader('Controls')
 threshold = st.slider('Threshold', 0.0, 1.0, 0.5)
# Columns with gap parameter
c1, c2 = st.columns(2, gap='large') # 'small','medium','large'
with c1:
 try:
   st.image('confusion_matrix.png', caption='Confusion Matrix')
 except Exception:
   st.info('Confusion Matrix image not found: confusion_matrix.png')
with c2:
 try:
   st.image('roc_curve.png', caption='ROC Curve')
 except Exception:
   st.info('ROC Curve image not found: roc_curve.png')


import streamlit as st
# Use the sidebar for controls — keeps main area clean
with st.sidebar:
 try:
   st.image('logo.png', width=150)
 except Exception:
   st.info('Logo image not found: logo.png')
 st.title('FYP Controls')
 st.divider()
 dataset = st.selectbox('Dataset', ['Train', 'Test', 'Validation'])
 model = st.selectbox('Model', ['RF', 'SVM', 'XGBoost'])
 st.divider()
 st.subheader('Hyperparameters')
 n_estimators = st.slider('n_estimators', 10, 500, 100)
 max_depth = st.number_input('max_depth', 1, 50, 10)
 st.divider()
 run_btn = st.button('Run Experiment', type='primary', key='run_experiment_sidebar_btn')
# Main page uses sidebar values
st.header(f'Results: {model} on {dataset} set')
if run_btn:
 st.info(f'Running {model} with {n_estimators} trees...')

import streamlit as st
tab1, tab2, tab3, tab4 = st.tabs([
 'Data Overview', 'Model Training',
 'Evaluation', 'Predictions'
])
with tab1:
 st.subheader('Dataset Overview')
 st.dataframe(df.describe())
with tab2:
 st.subheader('Model Configuration')
 # training controls here
with tab3:
 st.subheader('Performance Metrics')
 col1, col2 = st.columns(2)
 col1.metric('Accuracy', '94.5%')
 col2.metric('F1 Score', '93.7%')
with tab4:
 st.subheader('Live Predictions')
 # prediction inputs here


import streamlit as st
# Expander — collapsible section
with st.expander('Advanced Configuration', expanded=False):
 st.write('These settings are for advanced users only.')
 learning_rate = st.number_input('Learning Rate', 0.0001, 0.1, 0.001)
 batch_size = st.selectbox('Batch Size', [16, 32, 64, 128])
# Container — groups elements, can be filled later
result_container = st.empty() # Placeholder updated later
if st.button('Generate Report', key='generate_report_btn'):
 result_container.success('Report generated at 14:32:05')
# st.container — logical grouping with border
with st.container(border=True):
 st.subheader('Model Summary')
 st.write('Algorithm: Random Forest | Trees: 200 | Depth: 15')

import streamlit as st
import time
# Progress bar — useful for long training loops
progress = st.progress(0, text='Initialising...')
for epoch in range(100):
 time.sleep(0.02) # simulate work
 progress.progress(epoch + 1,
 text=f'Training epoch {epoch+1}/100...')
progress.empty() # Remove bar when done
# Spinner — wraps a block of code
with st.spinner('Loading model weights...'):
 time.sleep(2) # simulate load
st.success('Model loaded!')
# Status container (structured multi-step status)
with st.status('Running pipeline...', expanded=True) as status:
 st.write('Loading data...')
 time.sleep(1)
 st.write('Preprocessing features...')
 time.sleep(1)
 st.write('Running inference...')
 status.update(label='Done!', state='complete')

import streamlit as st
import pandas as pd
import numpy as np
df = pd.DataFrame({
 'Patient_ID': range(1, 6),
 'Age': [34, 45, 56, 29, 67],
 'Diagnosis': ['Positive','Negative','Positive','Negative','Positive'],
 'Confidence': [0.92, 0.87, 0.95, 0.73, 0.89]
})
# Interactive dataframe (sortable, searchable in 1.32+)
st.dataframe(df, use_container_width=True,
 column_config={
 'Patient_ID': st.column_config.NumberColumn('ID'),
 'Confidence': st.column_config.ProgressColumn(
 'Confidence', min_value=0, max_value=1, format='%.2f'),
 'Diagnosis': st.column_config.SelectboxColumn(
 'Diagnosis', options=['Positive','Negative'])
 }
)
# Static table (no interaction)
st.table(df.head(3))

import streamlit as st
import pandas as pd
import numpy as np
# Generate sample data
chart_data = pd.DataFrame(
 np.random.randn(20, 3), columns=['Model A', 'Model B', 'Baseline']
)
st.subheader('Line Chart — Training Loss')
st.line_chart(chart_data)
st.subheader('Bar Chart — Feature Importance')
feat_imp = pd.DataFrame({'importance':[0.35,0.28,0.19,0.11,0.07]},
 index=['income','age','score','region','edu'])
st.bar_chart(feat_imp)
st.subheader('Area Chart — Cumulative Accuracy')
st.area_chart(chart_data)
st.subheader('Scatter Chart')
st.scatter_chart(chart_data, x='Model A', y='Model B')

import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
# Confusion matrix with matplotlib heatmap
cm = np.array([[85, 5], [8, 102]])
fig, ax = plt.subplots(figsize=(5, 4))
ax.imshow(cm, cmap='Blues', aspect='auto')
for i in range(cm.shape[0]):
 for j in range(cm.shape[1]):
   ax.text(j, i, str(cm[i, j]), ha='center', va='center', color='black')
ax.set_xticks([0, 1])
ax.set_yticks([0, 1])
ax.set_xticklabels(['Pred Neg', 'Pred Pos'])
ax.set_yticklabels(['True Neg', 'True Pos'])
ax.set_title('Confusion Matrix')
ax.set_ylabel('Actual')
ax.set_xlabel('Predicted')
st.pyplot(fig)
plt.close(fig) # IMPORTANT: always close to free memory
# ROC Curve
fpr = np.linspace(0, 1, 100)
tpr = np.sqrt(fpr) # mock curve
fig2, ax2 = plt.subplots()
ax2.plot(fpr, tpr, 'b-', lw=2, label='ROC (AUC=0.94)')
ax2.plot([0,1],[0,1],'r--', label='Random')
ax2.set_xlabel('False Positive Rate')
ax2.set_ylabel('True Positive Rate')
ax2.legend()
ax2.set_title('ROC Curve')
st.pyplot(fig2)

import streamlit as st
import plotly.express as px
import plotly.graph_objects as go
import pandas as pd
# Interactive scatter plot
df = px.data.iris()
fig = px.scatter(df, x='sepal_width', y='sepal_length',
 color='species', size='petal_length',
 title='Iris Dataset — Feature Correlation')
st.plotly_chart(fig, use_container_width=True)
# Model comparison bar chart
models = ['Logistic Reg', 'Random Forest', 'SVM', 'XGBoost']
scores = [0.87, 0.94, 0.91, 0.96]
fig2 = go.Figure(go.Bar(x=models, y=scores,
 marker_color=['#636EFA','#EF553B','#00CC96','#AB63FA'],
 text=[f'{s:.0%}' for s in scores], textposition='outside'))
fig2.update_layout(title='Model Accuracy Comparison',
 yaxis_range=[0.8, 1.0])
st.plotly_chart(fig2, use_container_width=True)

import streamlit as st
from pathlib import Path
from PIL import Image
# Display image from file
xray_path = Path('data/sample_xray.jpg')
if xray_path.exists():
 img = Image.open(xray_path)
 st.image(img, caption='Chest X-Ray — Patient 001', use_container_width=True)
else:
 st.info('Chest X-ray image not found: data/sample_xray.jpg')
# Display from URL
st.image('https://upload.wikimedia.org/...',
 caption='Sample Image', width=400)
# Multiple images in columns
imgs = ['img1.png', 'img2.png', 'img3.png']
cols = st.columns(len(imgs))
for col, path in zip(cols, imgs):
 image_path = Path(path)
 if image_path.exists():
   col.image(str(image_path), use_container_width=True)
 else:
   col.info(f'Missing image: {path}')
# Video
video_path = Path('demo.mp4')
if video_path.exists():
 video = video_path.read_bytes()
 st.video(video)
else:
 st.info('Demo video not found: demo.mp4')
# Audio
audio_path = Path('output.wav')
if audio_path.exists():
 audio = audio_path.read_bytes()
 st.audio(audio, format='audio/wav')
else:
 st.info('Demo audio not found: output.wav')



# PROBLEM: Without session_state, count resets to 0 on every re-run
import streamlit as st
count = 0 # This is reset to 0 EVERY TIME the script runs
if st.button('Increment', key='increment_basic_btn'):
 count += 1 # This never actually persists
st.write(f'Count: {count}') # Always shows 0
# SOLUTION: Use session_state
import streamlit as st
# Initialise (only runs if key doesn't exist)
if 'count' not in st.session_state:
 st.session_state.count = 0
if st.button('Increment', key='increment_session_btn'):
 st.session_state.count += 1
st.write(f'Count: {st.session_state.count}') # Persists correctly

import streamlit as st
import pickle
# --- Initialise all state keys at top of script ---
defaults = {
 'model': None,
 'training_history': [],
 'current_dataset': None,
 'predictions': None,
 'is_trained': False,
}
for key, val in defaults.items():
 if key not in st.session_state:
    st.session_state[key] = val
# --- Sidebar: training controls ---
with st.sidebar:
 if st.button('Train Model', type='primary', key='train_model_session_btn'):
    with st.spinner('Training...'):
 # st.session_state.model = train(data) # your function
        st.session_state.is_trained = True
 st.session_state.training_history.append(
 {'epoch': len(st.session_state.training_history)+1,'accuracy': 0.94}
 )
 st.success('Model ready!')
# --- Main page: use trained model ---
if st.session_state.is_trained:
 st.success(f'Model trained — {len(st.session_state.training_history)} run(s)')
 if st.button('Predict', key='predict_session_btn'):
 # st.session_state.predictions = st.session_state.model.predict(X)
    pass
else:
 st.warning('Please train the model first.')

import streamlit as st
def on_model_change():
 # Called BEFORE the re-run when selectbox changes
 st.session_state.model = None # Reset model on algorithm change
 st.session_state.is_trained = False
 st.toast('Model reset — please retrain.', icon='!')
if 'model' not in st.session_state:
 st.session_state.model = None
 st.session_state.is_trained = False
algorithm = st.selectbox(
 'Algorithm',
 ['Random Forest', 'SVM', 'XGBoost'],
 on_change=on_model_change
)

import streamlit as st
with st.form('patient_form'):
 st.subheader('Patient Information')
 col1, col2 = st.columns(2)
 with col1:
    age = st.number_input('Age', 0, 120, 35)
 gender = st.selectbox('Gender', ['Male','Female','Other'])
 with col2:
    weight = st.number_input('Weight (kg)', 30.0, 200.0, 70.0)
 height = st.number_input('Height (cm)', 100.0, 250.0, 170.0)
 symptoms = st.multiselect('Symptoms',
 ['Fever','Cough','Fatigue','Breathlessness'])
 notes = st.text_area('Clinical Notes')
 submitted = st.form_submit_button('Run Diagnosis',
    type='primary')

# Only True when button clicked
 bmi = weight / ((height/100) ** 2)
 st.metric('BMI', f'{bmi:.1f}')
 st.info(f'Processing {age}yr {gender} patient with {len(symptoms)} symptoms...')

# app.py — Home / Landing page
import streamlit as st
st.set_page_config( # MUST be first st.* call, defined only here
 page_title='FYP: Smart Disease Predictor',
 page_icon=':stethoscope:',
 layout='wide'
)
st.title(':brain: Smart Disease Prediction System')
st.subheader('Final Year Project — BSc (Hons) in IT')
st.divider()
col1, col2, col3, col4 = st.columns(4)
col1.metric('Dataset Size', '15,000 records')
col2.metric('Features', '18 variables')
col3.metric('Best Accuracy', '96.2%')
col4.metric('Model', 'XGBoost')
st.divider()
st.markdown('''
### Navigation
Use the sidebar to navigate between sections:
- **Data Overview** — explore and visualise the dataset
- **Model Training** — configure and train classifiers
- **Evaluation** — view performance metrics and charts
- **Live Prediction** — enter patient data and get predictions
''')


import streamlit as st

api_keys = st.secrets.get("api_keys", {})
database_cfg = st.secrets.get("database", {})

openai_key = api_keys.get("openai_key")
db_pass = database_cfg.get("password")

if not openai_key:
 st.info("Missing secret: api_keys.openai_key")
if not db_pass:
 st.info("Missing secret: database.password")



