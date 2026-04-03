# pages/4_Live_Prediction.py
import streamlit as st
st.header('Live Prediction')
# Access the model trained in page 2
if st.session_state.get('trained_model') is None:
 st.warning('No model found. Please go to Model Training first.')
 st.stop() # Halt rendering if prerequisite not met
st.success('Model loaded from session — ready for predictions!')
# predictions = st.session_state.trained_model.predict(X_input)


import streamlit as st
# Navigate programmatically to another page
if st.button('Go to Evaluation'):
 st.switch_page('pages/3_Evaluation.py')
# Navigation with st.Page and st.navigation (1.36+)
# For custom navigation menus without file-based routing:
# pg = st.navigation([
# st.Page('app.py', title='Home', icon=':house:'),
# st.Page('pages/2_Model_Training.py', title='Train'),
# ])
# pg.run()

