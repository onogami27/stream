import streamlit as st
from pytube import YouTube
import os 





#動画タイトルを取得
def tube_title(URL):
    mystream = YouTube(url=f"{URL}").title
    return mystream

#ダウンロードする動画形式を取得
def tube_in(URL):
    mystream = YouTube(url=URL)
    mystream_1 = mystream.streams.filter(file_extension="mp4").all()

    return mystream_1
#選択した動画形式でダウンロードする
def tube_out(URL,tag,path):
    mystream = YouTube(url=URL).streams.filter().get_by_itag(tag)
    mystream.download(path)
#動画の説明文を取得    
def tube_gaiyou(URL):
    mystream = YouTube(url=URL).description
    return mystream

def event():
    st.success("aaaa")
    st.success("s")
def eee():
    for i in tube_in(r"https://www.youtube.com/watch?v=EkifUgWUk1w&list=RDZCOa3YY1MLc&index=2"):
        st.checkbox("{}".format(i))



st.title("YOUTUBE動画ダウンローダー")
dl_bt = st.download_button("ds","",disabled=True)

url = st.text_input("動画URLを入力")


        
start = st.button("開始")
if start:
    if bool(url) == False:
        st.warning("動画URLを入力してください")
        pass
    else:
        
        mystream = YouTube(url = url)
        mystream = mystream.streams.filter(progressive=True, res="720p",file_extension="mp4").get_highest_resolution()
        global out_file
        out_file = mystream.download()
        out_file_name = os.path.split("{}".format(out_file))[1]
        #ダウンロードする
        with open(out_file,"rb") as f:
    
            dl_bt = st.download_button(label="動画のダウンロード",data=f,file_name=out_file_name)
        
        os.remove(out_file)
        

    
    
   

    

