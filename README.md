## 👥 Anggota Kelompok  
Kami adalah tim yang bekerja sama dalam menyelesaikan proyek ini dengan kontribusi yang setara. Setiap anggota berperan aktif dalam seluruh tahap pengembangan, mulai dari analisis data, pemrograman, hingga penyusunan dokumentasi.  

1. **Haafiz Dauz Syahputra** (10123087)  
2. **Dionisius Deni Mardiansyah** (10123089)  
3. **Muhammad Hafiz Hafiyyan** (10123096)  
4. **Muhamad Haikal** (10123103)  
5. **Muhammad Harlan Fadhillah** (10123109)  
6. **Saadilah Fahmi Husaini** (10123128)  

💡 *Informasi pekerjaan dari anggota dan penjelasan informasi pada dashboard sangat baik, menunjukkan kerja sama tim yang solid dalam proyek ini.*  


# 🌍 Analisis Kualitas Udara dengan Streamlit

Proyek ini bertujuan untuk menganalisis data kualitas udara dari beberapa stasiun pemantauan di China menggunakan **Streamlit** dan **Python**. Analisis ini mencakup faktor-faktor seperti arah angin, kecepatan angin, suhu, curah hujan, serta hubungan dengan berbagai polutan udara (PM2.5, PM10, NO2, CO, O3).  

---

## 🏆 **Tujuan Proyek**
1. Menentukan hubungan antara arah angin dan kualitas udara.
2. Menganalisis kecepatan angin dan polusi udara di Stasiun Tiantan.
3. Menyelidiki dampak suhu terhadap tingkat polutan udara.
4. Mengidentifikasi stasiun dengan kualitas udara terburuk.
5. Mengkaji hubungan curah hujan dan PM10 di Stasiun Aotizhongxin.
6. Membandingkan kualitas udara saat hujan dan tidak hujan.

---

## 📂 **Struktur Proyek**
📁 project-folder/ │── 📂 data/ # Folder untuk menyimpan dataset │── 📜 Pertanyaan_1.py # Analisis arah angin & kualitas udara │── 📜 Pertanyaan_2.py # Kecepatan angin & PM2.5 di Tiantan │── 📜 Pertanyaan_3.py # Pengaruh suhu terhadap kualitas udara │── 📜 Pertanyaan_4.py # Stasiun dengan kualitas udara terburuk │── 📜 Pertanyaan_5.py # Hubungan curah hujan dan PM10 │── 📜 Pertanyaan_6.py # Pengaruh hujan terhadap kualitas udara │── 📜 requirements.txt # Dependensi proyek │── 📜 README.md # Dokumentasi proyek


---

## 🔍 **Analisis yang Dilakukan**
### **1️⃣ Arah Angin dan Kualitas Udara**
- Menunjukkan distribusi arah angin dan hubungannya dengan PM2.5.
- Menggunakan **seaborn** untuk visualisasi distribusi data.

### **2️⃣ Kecepatan Angin di Stasiun Tiantan**
- Memeriksa hubungan kecepatan angin dengan kualitas udara.
- Menampilkan data dengan **scatter plot** dan **regresi linear**.

### **3️⃣ Pengaruh Suhu terhadap Polutan**
- Menganalisis korelasi antara suhu dan polutan seperti PM2.5, PM10, NO2, CO, dan O3.
- Menggunakan **heatmap korelasi** untuk melihat hubungan antarvariabel.

### **4️⃣ Stasiun dengan Kualitas Udara Terburuk**
- Menentukan stasiun dengan tingkat PM2.5 tertinggi pada tahun 2016.
- Memvisualisasikan data menggunakan **bar chart**.

### **5️⃣ Hubungan Curah Hujan dan PM10**
- Mengkaji efek curah hujan terhadap kadar PM10 di Stasiun Aotizhongxin.
- Menampilkan analisis menggunakan **boxplot**.

### **6️⃣ Pengaruh Hujan terhadap Kualitas Udara**
- Membandingkan tingkat polutan saat hujan dan tidak hujan.
- Menganalisis rata-rata PM2.5, PM10, dan NO2 dalam kondisi cuaca berbeda.

---

## 🚀 **Cara Menjalankan Proyek**
### **1️⃣ Instalasi Dependensi**
Pastikan Python sudah terinstal di sistem. Kemudian, jalankan perintah berikut untuk menginstal pustaka yang dibutuhkan:  

```sh
pip install -r requirements.txt


2️⃣ Menjalankan Analisis
Gunakan Streamlit untuk menjalankan aplikasi visualisasi. Misalnya, untuk menjalankan Pertanyaan_1.py, gunakan perintah berikut:

streamlit run Pertanyaan_1.py

🛠 Teknologi yang Digunakan
Python 3.x: Bahasa pemrograman utama.
Pandas: Manipulasi dan analisis data.
Matplotlib & Seaborn: Visualisasi data.
Streamlit: Membangun antarmuka pengguna berbasis web.
Folium: Visualisasi peta interaktif.
Streamlit-Folium: Integrasi peta ke dalam Streamlit.


📌 Contoh Visualisasi
Scatter Plot Kecepatan Angin vs PM2.5
Heatmap Korelasi Suhu dan Polutan

✉ Kontak
Jika ada pertanyaan atau ingin berdiskusi lebih lanjut, silakan hubungi saya melalui:
📧 Email: saadilah.10123128@mahasiswa.unikom.ac.id


