import streamlit as st
from multipage import MultiPage
from pages import page_1, page_2, page_3

main_page = MultiPage()
st.markdown('sjseijf')

#menambahkan semua halaman di sini
main_page.add_web("page_1", page_1.main_page)
main_page.add_web("page_2", page_2.main_page)
main_page.add_web("page_3", page_3.main_page)
# Main Page
main_page.run()

st.title("Home Page")


