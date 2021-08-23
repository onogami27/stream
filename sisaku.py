import streamlit as st
import huguai_excel


file = st.file_uploader("ファイルアップロード", type = "xlsx")

if bool(file) == True:
    x = huguai_excel.excel(file)

    st.write(x)
