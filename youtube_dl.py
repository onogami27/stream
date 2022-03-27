import streamlit as st
from pytube import YouTube
import os 
import shutil

#カレントディレクトリpathを取得
cwd = os.getcwd()


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

#mp4形式で動画をダウンロード
def dl_mp4(url):
    mystream = YouTube(url = url)
    st.text_input(label="動画タイトル",value=tube_title(url))
    mystream_mp4 = mystream.streams.filter(progressive=True, res="720p",file_extension="mp4").get_highest_resolution()
    out_file_mp4 = mystream_mp4.download("mp4")
    out_file_name_mp4 = os.path.split("{}".format(out_file_mp4))[1]
    #ダウンロードする
    with open(out_file_mp4,"rb") as mp4:
        dl_bt_mp4 = st.download_button(label="動画のダウンロード",data=mp4,file_name=out_file_name_mp4)
    shutil.rmtree("mp4")          

#音声ファイルをダウンロード
def dl_audio(url):
    mystream = YouTube(url = url)
    mystream_audio = mystream.streams.filter(type="audio",mime_type="audio/mp4").first()
    out_file_audio = mystream_audio.download("audio")
    out_file_name_audio = os.path.split("{}".format(out_file_audio))[1]
    with open(out_file_audio,"rb") as audio:
        dl_bt_audio = st.download_button(label="音声のみダウンロード",data=audio,file_name=out_file_name_audio)
    shutil.rmtree("audio")

#ページタイトルを記載
st.title("YOUTUBE動画ダウンローダー")


url = st.text_input("動画URLを入力")


        
start = st.button("開始")
if start:
    if bool(url) == False:
        st.warning("動画URLを入力してください")
        pass
    else:
        dl_mp4(url)
        dl_audio(url)
        #mystream = YouTube(url = url)
        #st.text_input(label="動画タイトル",value=tube_title(url))
        #mystream_mp4 = mystream.streams.filter(progressive=True, res="720p",file_extension="mp4").get_highest_resolution()
        #mystream_audio = mystream.streams.filter(type="audio",mime_type="audio/mp4").first()
        #out_file_mp4 = mystream_mp4.download()
        #out_file_audio = mystream_audio.download()
        #out_file_name_mp4 = os.path.split("{}".format(out_file_mp4))[1]
        #out_file_name_audio = os.path.split("{}".format(out_file_audio))[1]
        #ダウンロードする
        #with open(out_file_mp4,"rb") as mp4:
        #    dl_bt_mp4 = st.download_button(label="動画のダウンロード",data=mp4,file_name=out_file_name_mp4)
        
        #with open(out_file_audio,"rb") as audio:
        #    dl_bt_audio = st.download_button(label="音声のみダウンロード",data=audio,file_name=out_file_name_audio+"audio")
        #os.remove(out_file_mp4)
        #os.remove(out_file_audio)
        

    
    
   

    

