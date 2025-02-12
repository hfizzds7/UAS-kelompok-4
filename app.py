import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
import folium
from streamlit_folium import folium_static


# Load dataset
def load_data():
    files = [
        'data/PRSA_Data_Aotizhongxin_20130301-20170228.csv',
        'data/PRSA_Data_Changping_20130301-20170228.csv',
        'data/PRSA_Data_Dingling_20130301-20170228.csv',
        'data/PRSA_Data_Dongsi_20130301-20170228.csv',
        'data/PRSA_Data_Guanyuan_20130301-20170228.csv',
        'data/PRSA_Data_Gucheng_20130301-20170228.csv',
        'data/PRSA_Data_Huairou_20130301-20170228.csv',
        'data/PRSA_Data_Nongzhanguan_20130301-20170228.csv',
        'data/PRSA_Data_Shunyi_20130301-20170228.csv',
        'data/PRSA_Data_Tiantan_20130301-20170228.csv',
        'data/PRSA_Data_Wanliu_20130301-20170228.csv',
        'data/PRSA_Data_Wanshouxigong_20130301-20170228.csv'
    ]
    df_list = [pd.read_csv(file) for file in files]
    df = pd.concat(df_list, ignore_index=True)
    return df

df = load_data()

# Sidebar filtering
st.sidebar.header("Filter Data")
station_filter = st.sidebar.multiselect("Pilih Stasiun:", df["station"].unique(), default=df["station"].unique())
year_filter = st.sidebar.slider("Pilih Tahun:", int(df["year"].min()), int(df["year"].max()), (2013, 2017))

df_filtered = df[(df["station"].isin(station_filter)) & (df["year"].between(year_filter[0], year_filter[1]))]

# Trend Analysis
st.title("Trend Analysis Polusi Udara")
st.write("Analisis perubahan polutan berdasarkan waktu")
station_choice = st.selectbox("Pilih Stasiun:", df_filtered["station"].unique())
df_station = df_filtered[df_filtered["station"] == station_choice]

fig = px.line(df_station, x="month", y=["PM2.5", "PM10", "SO2", "NO2", "CO", "O3"], title=f"Tren Polutan di {station_choice}")
st.plotly_chart(fig)

# Heatmap Korelasi
st.title("Heatmap Korelasi Polutan & Cuaca")
correlation = df_filtered[["PM2.5", "PM10", "SO2", "NO2", "CO", "O3", "TEMP", "PRES", "DEWP", "RAIN"]].corr()
fig, ax = plt.subplots(figsize=(10, 6))
sns.heatmap(correlation, annot=True, cmap="coolwarm", ax=ax)
st.pyplot(fig)

# Perbandingan Antar Stasiun
st.title("Perbandingan Antar Stasiun")
st.write("Pilih dua stasiun untuk dibandingkan")
station1 = st.selectbox("Stasiun 1:", df_filtered["station"].unique())
station2 = st.selectbox("Stasiun 2:", df_filtered["station"].unique())

df_compare = df_filtered[df_filtered["station"].isin([station1, station2])]
fig_compare = px.bar(df_compare, x="station", y=["PM2.5", "PM10"], title=f"Perbandingan PM2.5 & PM10 di {station1} dan {station2}", barmode='group')
st.plotly_chart(fig_compare)



# Peta Interaktif Lokasi Stasiun
st.title("Peta Lokasi Stasiun")
station_coords = {
    "Aotizhongxin": [40.0, 116.4],
    "Changping": [40.2, 116.2],
    "Dingling": [40.3, 116.2],
    "Dongsi": [39.9, 116.4],
    "Guanyuan": [39.9, 116.3],
    "Gucheng": [39.9, 116.2],
    "Huairou": [40.3, 116.6],
    "Nongzhanguan": [39.9, 116.5],
    "Shunyi": [40.1, 116.6],
    "Tiantan": [39.8, 116.4],
    "Wanliu": [39.9, 116.3],
    "Wanshouxigong": [39.9, 116.3]
}
map_center = [39.9, 116.4]
map_ = folium.Map(location=map_center, zoom_start=11)
for station, coord in station_coords.items():
    folium.Marker(coord, popup=station).add_to(map_)
folium_static(map_)

st.write("Dashboard selesai dengan fitur filtering, analisis tren, heatmap korelasi, perbandingan antar stasiun, prediksi PM2.5, dan peta interaktif!")

st.sidebar.markdown("""
## 👥 Anggota Kelompok
Kami bekerja sama dalam semua aspek proyek ini, dari analisis data hingga pengembangan aplikasi.

- **Haafiz Dauz Syahputra** (10123087)
- **Dionisius Deni Mardiansyah** (10123089)
- **Muhammad Hafiz Hafiyyan** (10123096)
- **Muhamad Haikal** (10123103)
- **Muhammad Harlan Fadhillah** (10123109)
- **Saadilah Fahmi Husaini** (10123128)

💡 *Informasi yang disajikan dalam dashboard ini dikembangkan dengan analisis dan perencanaan yang matang oleh seluruh tim.*
""")

