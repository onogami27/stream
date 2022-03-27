from pytube import YouTube
import os
import shutil

cwd = os.getcwd()

#mp4形式で動画をダウンロード
def dl_mp4(url):
    mystream = YouTube(url = url)
    mystream_mp4 = mystream.streams.filter(progressive=True, res="720p",file_extension="mp4").get_highest_resolution()
    out_file_mp4 = mystream_mp4.download("mp4")
    out_file_name_mp4 = os.path.split("{}".format(out_file_mp4))[1]
    print(out_file_mp4)
    shutil.rmtree("mp4")        

#音声ファイルをダウンロード
def dl_audio(url):
    mystream = YouTube(url = url)
    mystream_audio = mystream.streams.filter(type="audio",mime_type="audio/mp4").first()
    out_file_audio = mystream_audio.download("audio")
    out_file_name_audio = os.path.split("{}".format(out_file_audio))[1]
    
    #os.remove(out_file_audio)   
    
    
dl_mp4("https://youtu.be/_T-Gx4UBFHo")
#dl_audio("https://youtu.be/_T-Gx4UBFHo")