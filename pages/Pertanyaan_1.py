import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.title("Pertanyaan 1: Arah Angin dan Kualitas Udara")

# Load data
@st.cache_data
def load_data():
    dataframes = [
        pd.read_csv('data/PRSA_Data_Aotizhongxin_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Changping_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Dingling_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Dongsi_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Guanyuan_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Gucheng_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Huairou_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Nongzhanguan_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Shunyi_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Tiantan_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Wanliu_20130301-20170228.csv'),
        pd.read_csv('data/PRSA_Data_Wanshouxigong_20130301-20170228.csv')
    ]
    all_data = pd.concat(dataframes, ignore_index=True)
    return all_data

data = load_data()

# Filter data berdasarkan tahun
st.sidebar.header("Filter Data")
selected_year = st.sidebar.selectbox("Pilih Tahun", sorted(data['year'].dropna().unique()))
filtered_data = data[data['year'] == selected_year]

# Analisis arah angin
st.subheader("Distribusi Arah Angin")
wind_distribution = filtered_data['wd'].value_counts()
st.bar_chart(wind_distribution)

# Rata-rata PM2.5 Berdasarkan Arah Angin
st.subheader("Rata-rata PM2.5 Berdasarkan Arah Angin")

# Hapus nilai NaN pada PM2.5 sebelum analisis
filtered_data = filtered_data.dropna(subset=['PM2.5'])

if not filtered_data.empty:
    wind_quality = filtered_data.groupby('wd')['PM2.5'].mean().sort_values(ascending=False)
    
    fig, ax = plt.subplots(figsize=(10, 5))
    sns.barplot(x=wind_quality.index, y=wind_quality.values, ax=ax, palette="Blues_r")
    ax.set_xlabel("Arah Angin")
    ax.set_ylabel("Rata-rata PM2.5")
    ax.set_title("Rata-rata PM2.5 Berdasarkan Arah Angin")
    
    st.pyplot(fig)
else:
    st.warning("Tidak ada data yang tersedia untuk tahun yang dipilih.")

st.subheader("Kesimpulan")
st.write("Arah angin tertentu memiliki pengaruh yang signifikan terhadap kualitas udara, terutama yang membawa polutan dari sumber tertentu.")
