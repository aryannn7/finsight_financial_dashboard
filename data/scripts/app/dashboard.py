import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(page_title="FinSight: Financial Transactions Dashboard", layout="wide")

# Load data
df = pd.read_csv("data/sample.csv")
anomalies = df[df['is_fraud'] == 1]  # Assuming 'is_fraud' column exists in sample

# anomalies = pd.read_csv("data/anomalies.csv")

st.title("FinSight: Financial Analytics & Fraud Detection")
st.caption("Built with Python, Streamlit, Pandas, and Scikit-learn | Dataset: Kaggle Credit Transactions")

# Show metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Transactions", f"{len(df):,}")
col2.metric("Avg Transaction Amount (£)", f"{df['amt'].mean():.2f}")
col3.metric("Detected Anomalies", f"{len(anomalies):,}")

st.markdown("---")

# Show table of anomalies
st.subheader("Sample Anomalous Transactions")
st.dataframe(anomalies[['trans_date_trans_time', 'merchant', 'amt', 'city', 'state']].head(10))

st.markdown("---")

# Optional: Show charts
st.subheader("Transaction Amount Distribution")
st.bar_chart(df['amt'].sample(500))  # Sample to speed up load
