# 🧠 Intelligent Systems FYP — Streamlit App

## 🚀 Live Demo

👉 [https://appapp-knnshso8wv7khdekn3x5zy.streamlit.app)


---

## 📌 Project Overview

This project is a **Streamlit-based Intelligent System** developed for FYP (Final Year Project). It integrates multiple AI components including:

* Machine Learning (Scikit-learn)
* Deep Learning (CNN for image classification)
* Natural Language Processing (HuggingFace Transformers)
* Chatbot Interface

The application provides an interactive web interface for prediction, analysis, and user interaction.

---

## ⚙️ Features

### 🔹 Disease Risk Prediction

* Predicts risk level based on user inputs
* Uses trained ML model (`classifier.pkl`)

### 🔹 X-Ray Image Classification

* Upload chest X-ray images
* Detect conditions like:

  * Healthy
  * Pneumonia
  * COVID-19

### 🔹 NLP Analysis

* Sentiment Analysis
* Text Summarization

### 🔹 Chatbot Assistant

* Interactive chatbot UI
* Can be extended with OpenAI / HuggingFace APIs

---

## 📂 Project Structure

```
project/
├── app.py
├── requirements.txt
├── Dockerfile
├── models/
│   ├── classifier.pkl
│   ├── scaler.pkl
│   └── cnn_classifier.h5
├── utils/
│   ├── preprocessing.py
│   └── resources.py
├── data/
│   └── sample.csv
└── .streamlit/
    ├── config.toml
    └── secrets.toml
```

---

## 🛠️ Installation (Local Setup)

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/streamlit_app.git
cd streamlit_app

# Install dependencies
pip install -r requirements.txt

# Run app
streamlit run app.py
```

---

## 🐳 Docker Setup

```bash
# Build image
docker build -t fyp-app .

# Run container
docker run -p 8501:8501 fyp-app
```

👉 Open: [http://localhost:8501](http://localhost:8501)

---

## ☁️ Deployment

### 🔹 Streamlit Community Cloud

* Connect GitHub repo
* Select `app.py`
* Deploy in minutes

### 🔹 Render

* Add start command:

```
streamlit run app.py --server.port $PORT --server.headless true
```

---

## 🔐 Secrets Management

Create `.streamlit/secrets.toml`:

```toml
[api_keys]
openai_key = "your-api-key"
```

Access in code:

```python
st.secrets["api_keys"]["openai_key"]
```

---

## 📦 Requirements

Key libraries:

* streamlit
* pandas
* numpy
* scikit-learn
* tensorflow
* transformers
* torch

---

## 👨‍🎓 Author

**Isuru Nimesh**
3rd Year — 2nd Semester
Faculty of IT | Horizon Campus

---

## 📄 License

This project is for academic purposes (FYP).
