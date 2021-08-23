import streamlit as st
import huguai_excel
import os
import datetime
file = st.file_uploader("ファイルアップロード", type = "xlsx")

if bool(file) == True:
    time = datetime.datetime.now()
    file_name = os.path.basename(str(file))
    print("更新時間:",time,file.name)

    x = huguai_excel.excel(file)

    st.write(x)
