import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
#dashboard
st.title("EMPLOYEE PAY DASHBOARD")
#emp information
st.header("Employee Information")
st.write("**Employee Name:**Rahul Sharma")
st.write("**Department:**Analytics")
st.write("**Designation:**Data Analyst")

#kpi cards

col1,col2,col3,col4=st.columns(4)
col1.metric("Grons Salary","₹105,000")
col2.metric("Net Salary","₹95,000")
col3.metric("Deductions","₹10,000")
col4.metric("Paid days","31")

st.divider()
#Salary Components
salary=pd.DataFrame({
    "Component":["Basic Salary","HRA","Conveyance","Medical","Special Allowance","Bonus"],
    "Amount":[60000,24000,4000,3000,9000,5000]})

st.subheader("Salary components (Bar Chart)")

fig , ax=plt.subplots(figsize=(7,4))
ax.bar(salary["Component"],salary["Amount"])
ax.set_xlabel("Salary Component")
ax.set_ylabel("Amount (₹)")
plt.xticks(rotation=20)
st.pyplot(fig)
st.divider()

#pie chart

st.subheader("Earnings Distribution (Pie Chart)")

fig,ax=plt.subplots(figsize=(6,6,))

ax.pie(
    salary["Amount"],
    labels=salary["Component"],
    autopct="%1.1f%%",
    startangle=360
    )
st.pyplot(fig)

st.divider()

#gross vs net vs deduction

st.subheader("Gross vs Deduction vs Net (Bar Chart)")

summary=pd.DataFrame({
    "Category":["Gross Salary","Deductions","Net Salary"],
    "Amount":[105000,10000,95000]
    })
fig, ax=plt.subplots(figsize=(6,4))

ax.bar(summary["Category"],summary["Amount"])
ax.set_ylabel("Amount (₹)")
st.pyplot(fig)
st.divider()

#employee details

st.subheader("Employee Details")

details=pd.DataFrame({
    "Field":[
        "Bank Name",
        "Account Number",
        "PAN",
        "Joining Date"],
    "Value":[
        "State Bank of India",
        "XXXX XXXX 9517",
        "ABCDE12345",
        "15-Jan-2024"]
    })
st.table(details)
