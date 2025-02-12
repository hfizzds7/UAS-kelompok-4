import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Pertanyaan 2: Pengaruh Kecepatan dan Arah Angin di Stasiun Tiantan")

# Fungsi untuk memuat data dengan cache agar lebih efisien
@st.cache_data
def load_data():
    return pd.read_csv('data/PRSA_Data_Tiantan_20130301-20170228.csv')

data = load_data()

# Filter data untuk tahun 2016
data_2016 = data[data['year'] == 2016]

# Distribusi Kecepatan Angin
st.subheader("Distribusi Kecepatan Angin")
plt.figure(figsize=(10, 6))
sns.histplot(data_2016['WSPM'], bins=30, kde=True, color='blue')
st.pyplot(plt)

# Hubungan Kecepatan Angin dan PM2.5
st.subheader("Hubungan Kecepatan Angin dan PM2.5")
plt.figure(figsize=(10, 6))
sns.scatterplot(x=data_2016['WSPM'], y=data_2016['PM2.5'], alpha=0.5, color='green')
st.pyplot(plt)

# Hubungan Arah Angin dan Kecepatan Angin
st.subheader("Rata-rata Kecepatan Angin berdasarkan Arah Angin")
wind_speed_by_dir = data_2016.groupby('wd')['WSPM'].mean().sort_values(ascending=False)
st.bar_chart(wind_speed_by_dir)

st.subheader("Kesimpulan")
st.write("Kecepatan angin yang lebih rendah cenderung meningkatkan konsentrasi PM2.5, sementara kecepatan angin yang lebih tinggi membantu menyebarkan polutan. Arah angin tertentu juga dapat mempengaruhi kecepatan angin yang terukur di stasiun.")
