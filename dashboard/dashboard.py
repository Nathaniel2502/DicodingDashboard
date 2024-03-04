import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st


#Load dataset
df_all_data = pd.read_csv('/complete_data.csv')
df_all_data['order_approved_at'] = pd.to_datetime(df_all_data['order_approved_at'], errors='coerce')

#Visualization function

def plot_most_sold_product_categories(data):
    category_counts = data['product_category_name_english'].value_counts().head(5)
    plt.figure(figsize=(10, 6))
    category_counts.plot(kind='bar', color='lightgreen')
    plt.title('Top 5 Most Sold Product Categories')
    plt.xlabel('Product Category')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

def plot_customer_distribution_by_state(data):
    state_counts = data['customer_state'].value_counts()
    plt.figure(figsize=(10, 6))
    state_counts.plot(kind='bar', color='coral')
    plt.title('Customer Distribution by State')
    plt.xlabel('State')
    plt.ylabel('Number of Customers')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)

def plot_payment_type_distribution(data):
    payment_type = data['payment_type'].value_counts()
    plt.figure(figsize=(10, 6))
    payment_type.plot(kind='bar', color='skyblue')
    plt.title('Payment Types Distribution')
    plt.xlabel('Payment Type')
    plt.ylabel('Number of Orders')
    plt.xticks(rotation=45)
    plt.grid(axis='y', linestyle='--', alpha=0.7)
    st.pyplot(plt)




#sidebar
    
# Sidebar - Date filter
st.sidebar.title('Filter by Date')
min_date = df_all_data['order_approved_at'].min().date()
max_date = df_all_data['order_approved_at'].max().date()
start_date, end_date = st.sidebar.date_input('Date range', [min_date, max_date], min_value=min_date, max_value=max_date)
filtered_data = df_all_data[(df_all_data['order_approved_at'].dt.date >= start_date) & (df_all_data['order_approved_at'].dt.date <= end_date)]



#Main Area
#title
st.title('Dashboard')


# Calculate and display metrics

column_1, column_2 = st.columns(2)
with column_1:
    total_orders = filtered_data['order_id'].nunique()
    st.metric(label="Total Orders", value=total_orders)

with column_2:
    total_sales = filtered_data['price'].sum()
    st.metric(label="Total Sales", value=f"BRL {total_sales:,.2f}")

# Display visualization for most sold product categories   
st.header('Most Sold Product Categories')
if 'plot_most_sold_product_categories' in globals():
    plot_most_sold_product_categories(filtered_data)

# Display visualization for most sold product categories
st.header('Customer Distribution by State')
if 'plot_customer_distribution_by_state' in globals():
    plot_customer_distribution_by_state(filtered_data)

# Display visualization for most sold product categories
st.header('Payment Type Distribution')
if 'plot_payment_type_distribution' in globals():
    plot_payment_type_distribution(filtered_data)




