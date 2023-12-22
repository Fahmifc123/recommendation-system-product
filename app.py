import streamlit as st
import pandas as pd
import numpy as np
from sklearn.cluster import KMeans
import joblib

# Load the K-Means model
model_filename = 'kmeans_model.pkl'
kmeans_model = joblib.load(model_filename)

df = pd.read_csv('data_baru.csv')
product_customer_matrix = df.pivot_table(index='product_id', columns='customer_id', values='purchase_day', fill_value=0)

# Function to get top recommendations using K-Means
def get_top_recommendations_kmeans(customer_id, n=3):
    try:
        customer_index = int(customer_id) - 1  # Adjust index since customer_id starts from 1
        cluster_label = kmeans_model.predict(product_customer_matrix.iloc[:, customer_index].values.reshape(1, -1))[0]

        # Get customers in the same cluster
        cluster_customers = product_customer_matrix.columns[kmeans_model.labels_ == cluster_label]

        # Get top products purchased by customers in the same cluster
        top_recommendations = product_customer_matrix.loc[:, cluster_customers].sum(axis=1).sort_values(ascending=False).head(n).index
        # top_recommendations = product_encoder.inverse_transform(top_recommendations)
    except ValueError:
        # Handle the case where customer ID is not in the dataset
        # Provide random recommendations from the entire product list
        all_products = np.arange(len(product_customer_matrix.index))
        top_recommendations = np.random.choice(all_products, size=n, replace=False)

    return top_recommendations

# Streamlit App
st.title('Product Recommendation App')

# Input customer ID
customer_id_input = st.text_input('Masukkan ID Customer:', '')

# Perform inference and display recommendations
if customer_id_input:
    recommendations_kmeans = get_top_recommendations_kmeans(customer_id_input, n=3)

    # Display recommendations in a nice format
    st.markdown(f"## Recommendations for Customer ID {customer_id_input}")
    st.markdown("Here are the top 3 product recommendations using K-Means Clustering:")
    
    for i, product_id in enumerate(recommendations_kmeans, 1):
        st.write(f"{i}. Product ID: {product_id}")
