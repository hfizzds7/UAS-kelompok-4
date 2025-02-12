import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.title("Pertanyaan 6: Pengaruh Hujan terhadap Kualitas Udara")

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

# Konversi nilai curah hujan menjadi kategori (Hujan atau Tidak Hujan)
data['Rain_Category'] = data['RAIN'].apply(lambda x: 'Hujan' if x > 0 else 'Tidak Hujan')

st.subheader("Perbandingan Tingkat Polutan Saat Hujan dan Tidak Hujan")
pollutants = ['PM2.5', 'PM10', 'SO2', 'NO2', 'CO', 'O3']

for pollutant in pollutants:
    st.write(f"### {pollutant}")
    plt.figure(figsize=(10, 6))
    sns.boxplot(x='Rain_Category', y=pollutant, data=data)
    st.pyplot(plt)

# Analisis statistik rata-rata polutan berdasarkan kondisi hujan
st.subheader("Rata-rata Konsentrasi Polutan Berdasarkan Kondisi Hujan")
avg_pollution = data.groupby('Rain_Category')[pollutants].mean()
st.write(avg_pollution)

st.subheader("Kesimpulan")
st.write("Hujan secara signifikan mengurangi konsentrasi polutan seperti PM2.5, PM10, dan SO2, tetapi memiliki efek yang lebih kecil pada CO dan O3. Dengan demikian, curah hujan memiliki peran penting dalam membersihkan udara dari partikel polutan.")
