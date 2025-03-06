import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os

# Use the correct path relative to src/multiple_agents
DATA_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "transactions.csv")

def load_data():
    if os.path.exists(DATA_PATH):
        return pd.read_csv(DATA_PATH)
    return None

def main():
    # Set Page Config
    st.set_page_config(page_title="Fraud Detection Dashboard", layout="wide")

    # Title and Description
    st.title("🛡️ Fraud Detection & Phishing Prevention")
    st.markdown("**Developed by Nousheen Fatima Adeel**")  
    st.markdown("This app detects fraudulent transactions and phishing attacks in banking systems.")

    # Sidebar for File Upload
    st.sidebar.header("Upload Transaction Data (CSV)")
    uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type=["csv"])

    # Load default dataset or uploaded file
    df = None
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.sidebar.success("✅ Using uploaded file")
    else:
        df = load_data()
        if df is not None:
            st.sidebar.info("📂 Using default dataset from data/transactions.csv")
        else:
            st.sidebar.error("⚠ No dataset found. Please upload a CSV file.")

    if df is not None:
        st.write("### 📊 Transaction Data Preview:")
        st.dataframe(df.head(10))

        # Simulating Fraud Detection
        df["Fraud"] = np.random.choice(["✅ Safe", "⚠ Suspicious"], size=len(df), p=[0.8, 0.2])
        fraud_cases = df[df["Fraud"] == "⚠ Suspicious"]

        st.write("### 🚨 Fraudulent Transactions Detected:")
        st.dataframe(fraud_cases)

        # Bar Chart of Transactions
        st.write("### 📈 Fraud vs Safe Transactions")
        fig, ax = plt.subplots()
        df["Fraud"].value_counts().plot(kind="bar", color=["green", "red"], ax=ax)
        st.pyplot(fig)

    # Phishing URL Checker
    st.sidebar.header("🔍 Phishing Detection")
    url = st.sidebar.text_input("Enter a URL to check:")

    if url:
        is_phishing = np.random.choice([True, False], p=[0.3, 0.7])
        if is_phishing:
            st.sidebar.error("🚨 This URL is a potential phishing attack!")
        else:
            st.sidebar.success("✅ This URL seems safe.")

    st.sidebar.info("Developed with ❤️ using Streamlit")

    # Footer
    st.markdown("---")  # Adds a horizontal line
    st.markdown(
       "<p style='text-align: center; font-size: 14px;'>© 2024 All Rights Reserved | Developed by <b>Nousheen Fatima Adeel</b> | 📧 <a href='mailto:nousheenfatimaadeel@gmail.com'>nousheenfatimaadeel@gmail.com</a></p>",
    unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
