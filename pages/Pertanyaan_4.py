import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import folium
from streamlit_folium import folium_static

st.title("Pertanyaan 4: Stasiun dengan Kualitas Udara Terburuk pada Tahun 2016")

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

# Filter data untuk tahun 2016
data_2016 = data[data['year'] == 2016]

# Pastikan kolom 'PM2.5' tidak berisi NaN dan bertipe numerik
data_2016['PM2.5'] = pd.to_numeric(data_2016['PM2.5'], errors='coerce')
data_2016 = data_2016.dropna(subset=['PM2.5'])  # Hapus nilai NaN

# Debugging: Tampilkan 10 data pertama setelah diproses
st.subheader("🔍 Debugging Data PM2.5")
st.write(data_2016[['station', 'PM2.5']].head(10))  

# Hitung rata-rata PM2.5 per stasiun dan ambil 5 terburuk
station_buruk = data_2016.groupby('station')['PM2.5'].mean().sort_values(ascending=False).head(5)

# Debugging: Tampilkan hasil pengelompokan sebelum membuat grafik
st.subheader("🔍 Debugging Hasil Pengelompokan")
st.write(station_buruk)

st.subheader("📊 5 Stasiun dengan Udara Terburuk")

# Pastikan data tersedia sebelum menampilkan grafik
if station_buruk.empty:
    st.write("⚠️ Tidak ada data kualitas udara yang bisa ditampilkan.")
else:
    # Gunakan Matplotlib untuk menampilkan grafik agar lebih stabil
    fig, ax = plt.subplots()
    station_buruk.plot(kind='bar', ax=ax, color='red', alpha=0.7)
    ax.set_ylabel("Rata-rata PM2.5 (µg/m³)")
    ax.set_xlabel("Stasiun")
    ax.set_title("5 Stasiun dengan Udara Terburuk Tahun 2016")
    st.pyplot(fig)

# Data lokasi stasiun (Tambahkan koordinat lokasi stasiun)
station_locations = {
    "Aotizhongxin": [39.9821, 116.4179],
    "Changping": [40.2181, 116.2359],
    "Dingling": [40.2906, 116.2202],
    "Dongsi": [39.9296, 116.4174],
    "Guanyuan": [39.9322, 116.3561],
    "Gucheng": [39.9135, 116.1854],
    "Huairou": [40.3982, 116.6318],
    "Nongzhanguan": [39.9355, 116.4613],
    "Shunyi": [40.1259, 116.6542],
    "Tiantan": [39.8866, 116.4121],
    "Wanliu": [39.9490, 116.2958],
    "Wanshouxigong": [39.8882, 116.3437]
}

st.subheader("🗺️ Peta Lokasi Stasiun")
m = folium.Map(location=[39.9042, 116.4074], zoom_start=10)  # Lokasi Beijing

# Tambahkan marker untuk setiap stasiun terburuk
for station, pm25 in station_buruk.items():
    if station in station_locations:  # Pastikan ada koordinatnya
        lat, lon = station_locations[station]
        folium.Marker(
            location=[lat, lon],
            popup=f"{station}: {pm25:.2f} µg/m³",
            icon=folium.Icon(color="red")
        ).add_to(m)

folium_static(m)

st.subheader("📌 Kesimpulan")
if station_buruk.empty:
    st.write("Tidak ada data yang dapat ditampilkan.")
else:
    st.write("Stasiun dengan kualitas udara terburuk pada tahun 2016 adalah:")
    st.write(station_buruk.index.tolist())
