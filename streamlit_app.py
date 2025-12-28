import streamlit as st
import pandas as pd

st.title("Data Diri Mahasiswa")
st.header("Profil Pribadi")
st.subheader("Informasi Umum")
st.caption("Contoh web page Streamlit bertema data diri")
st.text(
    "Halaman ini menampilkan data diri saya (Andi Hariandi) mahasiswa Jurusan Elektro, Prodi Rekayasa Pembangkit Energi "
    "menggunakan beberapa komponen dasar pada Streamlit."
)
st.subheader("Contoh Kode Streamlit")
st.code("""
st.title("Data Diri Mahasiswa")
st.write("Andi Hariandi, 4232401054, dan Rekayasa Pembangkit Energi")
""", language="python")
st.subheader("Data Diri")
data_diri = {
    "Keterangan": [
        "Nama                    :",
        "NIM                        :",
        "Program Studi  :",
        "Vokasi                  :",
        "Politeknik:         :",
        "Tahun Masuk    :"
    ],
    "Data": [
        "Andi Hariandi",
        "4232401054",
        "Teknik Elektro",
        "Teknik",
        "Politeknik Negeri Batam",
        "2024"
    ]
}
df = pd.DataFrame(data_diri)
st.dataframe(df, use_container_width=True)
st.subheader("Visualisasi Aktivitas Akademik")

aktivitas = {
    "Semester": ["Semester 1", "Semester 2", "Semester 3"],
    "Jumlah SKS": [17, 19, 20,]
}

df_chart = pd.DataFrame(aktivitas).set_index("Semester")

st.line_chart(df_chart)
