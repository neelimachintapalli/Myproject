import streamlit as st
import pandas as pd

# Read CSV file
df = pd.read_csv("SuperMarket Analysis.csv")

# Data Preparation
branch_sales = df.groupby('Branch')['Sales'].sum()
product_sales = df.groupby('Product line')['Sales'].sum()
product_profit = df.groupby('Product line')['gross income'].sum()
payment_counts = df['Payment'].value_counts()

# Convert Date column to datetime
df['Date'] = pd.to_datetime(df['Date'])
df['Month'] = df['Date'].dt.month_name()

monthly_sales = df.groupby('Month')['Sales'].sum()

# Dashboard Title
st.title("🛒 Supermarket Sales Dashboard")

# First Row
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("💰 Total Revenue", f"{df['Sales'].sum():,.2f}")

with col2:
    st.metric("👥 Total Customers", df['Invoice ID'].nunique())

with col3:
    st.metric("🏢 Best Branch", branch_sales.idxmax())

# Second Row
col4, col5, col6 = st.columns(3)

with col4:
    
    st.metric("📦 Best Product", product_sales.idxmax())

with col5:
    st.metric("💵 Most Profitable Product", product_profit.idxmax())

with col6:
    st.metric("📅 Highest Revenue Month", monthly_sales.idxmax())

# Third Row
col7, col8 = st.columns(2)

with col7:
    st.metric("💳 Most Popular Payment", payment_counts.idxmax())

with col8:
    st.metric("⭐ Average Customer Rating", round(df['Rating'].mean(), 2))
