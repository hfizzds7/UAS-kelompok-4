import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Pertanyaan 3: Pengaruh Suhu terhadap Kualitas Udara di Stasiun Tiantan")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv('data/PRSA_Data_Tiantan_20130301-20170228.csv')

data = load_data()

# Korelasi antara suhu dan polutan
st.subheader("Korelasi antara Suhu dan Polutan")
correlation = data[['TEMP', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", fmt=".2f")
st.pyplot(plt)

# Distribusi suhu
st.subheader("Distribusi Suhu")
plt.figure(figsize=(10, 6))
sns.histplot(data['TEMP'], bins=30, kde=True, color='orange')
st.pyplot(plt)

# Hubungan suhu dan PM2.5
st.subheader("Hubungan Suhu dan PM2.5")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='TEMP', y='PM2.5', data=data, alpha=0.5, color='red')
st.pyplot(plt)

# Statistik suhu dan polutan
st.subheader("Statistik Suhu dan Polutan")
st.write(data[['TEMP', 'PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']].describe())

# Kesimpulan
st.subheader("Kesimpulan")
st.write("Suhu udara memiliki pengaruh terhadap polutan tertentu. Secara umum, suhu yang lebih rendah cenderung meningkatkan konsentrasi PM2.5 dan PM10, sementara suhu tinggi bisa meningkatkan konsentrasi O3.")
