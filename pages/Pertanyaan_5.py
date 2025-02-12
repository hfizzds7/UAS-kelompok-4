import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Pertanyaan 5: Hubungan Curah Hujan dan Kadar PM10 di Stasiun Aotizhongxin")

# Fungsi untuk memuat data dengan cache agar lebih efisien
@st.cache_data
def load_data():
    return pd.read_csv('data/PRSA_Data_Aotizhongxin_20130301-20170228.csv')

data = load_data()

# Filter data untuk tahun 2016
data_2016 = data[data['year'] == 2016]

# Scatter plot hubungan curah hujan dengan PM10
st.subheader("Hubungan Curah Hujan dan PM10")
plt.figure(figsize=(10, 6))
sns.scatterplot(x='RAIN', y='PM10', data=data_2016, alpha=0.5, color='green')
st.pyplot(plt)

# Korelasi antara curah hujan dan PM10
correlation = data_2016[['RAIN', 'PM10']].corr().iloc[0, 1]
st.subheader("Korelasi antara Curah Hujan dan PM10")
st.write(f"Korelasi antara curah hujan dan PM10: {correlation:.2f}")

st.subheader("Kesimpulan")
st.write("Curah hujan memiliki korelasi negatif dengan kadar PM10, yang berarti hujan dapat membantu mengurangi konsentrasi PM10 di udara.")
