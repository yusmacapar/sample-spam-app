import streamlit as st
import pickle

# Load model
with open("model/model.pkl", "rb") as model_file:
    model = pickle.load(model_file)

# Mengatur judul dan ikon
st.set_page_config(page_title="SMS Classifier", page_icon="📩")

# Judul aplikasi
st.title("Klasifikasi SMS 📩")
st.markdown("""
Selamat datang di aplikasi klasifikasi SMS! Masukkan teks pesan SMS Anda untuk melihat apakah itu **SMS Biasa**, **SMS Spam**, atau **SMS Operator**.
""")

# Input teks SMS dari pengguna
sms_text = st.text_area("Masukkan teks SMS Anda di sini:")

# Tombol untuk mengklasifikasi
if st.button("Klasifikasi"):
    if sms_text.strip() == "":
        st.warning("Silakan masukkan teks SMS terlebih dahulu.")
    else:
        # Placeholder untuk model klasifikasi
        # Sementara, hasil ditentukan secara acak; ganti dengan model Anda sendiri di implementasi nyata
        category = model.predict([sms_text])
        # Menampilkan hasil dengan skema warna
        if category == 0:
            st.success("Hasil: **SMS Biasa**", icon="✅")
            st.markdown("<style>div.stAlert p {color: green;}</style>", unsafe_allow_html=True)
        elif category == 1:
            st.error("Hasil: **SMS Spam**", icon="🚫")
            st.markdown("<style>div.stAlert p {color: red;}</style>", unsafe_allow_html=True)
        else:
            st.info("Hasil: **SMS Operator**", icon="📡")
            st.markdown("<style>div.stAlert p {color: orange;}</style>", unsafe_allow_html=True)

# Footer dengan informasi tambahan
st.markdown("""
---
**Catatan:** Aplikasi ini adalah demo. Untuk implementasi nyata, gantikan placeholder dengan model machine learning untuk klasifikasi SMS.
""")
