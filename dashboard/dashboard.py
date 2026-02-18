import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st

# ===============================
# Konfigurasi Halaman
# ===============================
st.set_page_config(
    page_title="Dashboard Persebaran Seller",
    layout="wide"
)

st.title("📊 Dashboard Persebaran Seller E-Commerce")
st.write("Dashboard ini menampilkan distribusi seller berdasarkan State dan Kota.")

import os
import pandas as pd
import streamlit as st

st.set_page_config(page_title="Dashboard", layout="wide")

# ===============================
# Load Data
# ===============================
@st.cache_data
def load_data():
    base_dir = os.path.dirname(__file__)
    data_path = os.path.join(base_dir, "main_data.csv")
    return pd.read_csv(data_path)

df = load_data()   # <<< INI WAJIB ADA DAN DI ATAS FILTER

# ===============================
# Sidebar Filter
# ===============================
st.sidebar.header("Filter Data")

state_list = sorted(df["seller_state"].unique())
selected_state = st.sidebar.multiselect(
    "Pilih State:",
    options=state_list,
    default=state_list
)

filtered_df = df[df["seller_state"].isin(selected_state)]

# ===============================
# KPI Metrics
# ===============================
col1, col2, col3 = st.columns(3)

col1.metric("Total Seller", len(filtered_df))
col2.metric("Jumlah State", filtered_df["seller_state"].nunique())
col3.metric("Jumlah Kota", filtered_df["seller_city"].nunique())

st.divider()

# ===============================
# Pertanyaan Bisnis 1
# ===============================
st.subheader("1️⃣ Distribusi Seller Berdasarkan State")

seller_by_state = (
    filtered_df["seller_state"]
    .value_counts()
    .head(10)
)

fig1, ax1 = plt.subplots()
seller_by_state.plot(kind="bar", ax=ax1)
ax1.set_title("Top 10 State dengan Seller Terbanyak")
ax1.set_xlabel("State")
ax1.set_ylabel("Jumlah Seller")
plt.xticks(rotation=45)

st.pyplot(fig1)

# ===============================
# Pertanyaan Bisnis 2
# ===============================
st.subheader("2️⃣ Distribusi Seller Berdasarkan Kota")

seller_by_city = (
    filtered_df["seller_city"]
    .value_counts()
    .head(10)
)

fig2, ax2 = plt.subplots()
seller_by_city.plot(kind="bar", ax=ax2)
ax2.set_title("Top 10 Kota dengan Seller Terbanyak")
ax2.set_xlabel("Kota")
ax2.set_ylabel("Jumlah Seller")
plt.xticks(rotation=45)

st.pyplot(fig2)

# ===============================
# Insight Section
# ===============================
st.divider()
st.subheader("📌 Insight")

st.write("""
- Seller terkonsentrasi pada wilayah tertentu, terutama state dan kota besar.
- State dengan jumlah seller tertinggi menunjukkan dominasi aktivitas penjualan.
- Kota besar seperti Sao Paulo menjadi pusat aktivitas seller.
- Terdapat peluang ekspansi di wilayah dengan jumlah seller lebih rendah.
""")
