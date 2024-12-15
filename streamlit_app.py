import streamlit as st

# Judul Aplikasi
st.title("🍴 Pilih Menu Makanan")

# Daftar Makanan dan Harganya
menu = {
    "Nasi Goreng": 20000,
    "Mie Goreng": 15000,
    "Sate Ayam": 25000,
    "Bakso": 18000,
    "Es Teh": 5000,
    "Es Jeruk": 7000
}

# Menampilkan Pilihan Makanan
st.subheader("Pilih Makanan dan Minuman")
selected_items = st.multiselect("Silakan pilih makanan/minuman yang Anda inginkan:", options=list(menu.keys()))

# Menampilkan Daftar Pilihan dan Total Harga
if selected_items:
    st.write("### Pesanan Anda:")
    total_price = 0
    for item in selected_items:
        st.write(f"- {item} : Rp {menu[item]:,}")
        total_price += menu[item]
    st.write("### Total Harga: Rp {:,}".format(total_price))
else:
    st.write("Anda belum memilih makanan/minuman.")
