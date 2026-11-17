
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st

st.set_page_config(
    page_title="Supermarket Sales Dashboard",
    layout="wide"
)

st.title("Supermarket Sales Dashboard")
st.write("Sales and Data Analysis")

# Sample supermarket data
data = {
    "Product": ["Milk", "Bread", "Rice", "Sugar", "Oil"],
    "Sales": [5000, 3500, 7000, 4500, 6000],
    "Quantity": [50, 70, 35, 45, 30],
    "Profit": [1000, 700, 1500, 900, 1200]
}

df = pd.DataFrame(data)

# Key metrics
total_sales = df["Sales"].sum()
total_profit = df["Profit"].sum()
total_quantity = df["Quantity"].sum()
avg_order_value = df["Sales"].mean()

col1, col2, col3, col4 = st.columns(4)

col1.metric("Total Sales", f"KES {total_sales:,.2f}")
col2.metric("Total Profit", f"KES {total_profit:,.2f}")
col3.metric("Total Quantity", total_quantity)
col4.metric("Average Sales", f"KES {avg_order_value:,.2f}")

st.subheader("Sales Data")
st.dataframe(df, use_container_width=True)

# Sales chart
st.subheader("Sales by Product")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="Product", y="Sales", ax=ax)

ax.set_title("Product Sales")
ax.set_xlabel("Product")
ax.set_ylabel("Sales (KES)")

st.pyplot(fig)
plt.close(fig)

# Profit chart
st.subheader("Profit Analysis")

fig, ax = plt.subplots(figsize=(10, 5))
sns.barplot(data=df, x="Product", y="Profit", ax=ax)

ax.set_title("Profit by Product")
st.pyplot(fig)
plt.close(fig)

st.success("Dashboard loaded successfully!")
