# FinSight: Financial Transactions Dashboard & Fraud Detection

[![Streamlit App](https://img.shields.io/badge/Streamlit-Live--Demo-brightgreen?logo=streamlit)](https://finsightfinancialdashboard-ruv8mtesgfxtxudhetrqgh.streamlit.app/)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

## Overview

**FinSight** is an interactive data dashboard that analyzes financial transaction data and detects fraudulent patterns in real time. 

Built using Python, Streamlit, and Scikit-learn, the app is designed to simulate how banks or fintech platforms monitor transaction health and flag anomalies.


This is part of my effort to showcase real-world data engineering and machine learning workflows with a finance twist.

---

## Features

  Visual KPIs: Total transactions, average amount, anomalies
  Fraud detection using Isolation Forest
  Clean Streamlit UI for end-users
  Demo-ready dataset (`sample.csv`) for fast load time
  Optimized for recruiters and demoing in interviews

---

## Tech Stack

  Python 3.10 +
  Streamlit – frontend/dashboard
  Pandas – data handling
  Scikit-learn – machine learning (anomaly detection)
  GitHub + Streamlit Cloud – deployment

---

## Folder Structure

├── app/
│ └── dashboard.py # Streamlit app
├── data/
│ └── sample.csv # Lightweight demo dataset
├── scripts/
│ ├── process_data.py # Cleans and loads dataset
│ └── anomaly_model.py # Trains the fraud detection model
├── requirements.txt
├── README.md
└── .gitignore

---

## 📊 Live Demo

👉 [Click here to use the app](https://finsightfinancialdashboard-ruv8mtesgfxtxudhetrqgh.streamlit.app/)

---

## 🔧 Setup Locally

```bash
git clone https://github.com/aryannn7/finsight_financial_dashboard.git
cd finsight_financial_dashboard
pip install -r requirements.txt
streamlit run app/dashboard.py



