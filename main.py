import streamlit as st
from pathlib import Path
from pytube import YouTube
import os , time
def download(link,res,option): 
    e=time.time()
    latest_iteration = st.empty()
    latest_iteration.text(f"{1} Second")
    bar = st.progress(2)
    #taking link and res as input
    # link = input("Enter the Youtube Video URL : ")
    # res=input ("Resolution e.g-2160p,1440p,4320p etc : ")
    # option=int(input('''To get Audio - Type 1 \nTo get Video - Type 2 \nTo get Both -'''))
    #creating a  object of youtube video
    yt = YouTube(link)
    

    audio = yt.streams.get_by_itag(yt.streams.filter(type="audio")[0].itag)
    
    
    a=audio.download()
    
    latest_iteration.text(f'{int(time.time()-e)} Second')
    bar.progress(30)
    #to change the file name of audio
    q=Path(a)
    q=q.rename(q.with_name("Audio.mp3"))
    if (option==2):
        video = yt.streams.get_by_itag(yt.streams.filter(res=res,type="video")[0].itag)
        b=video.download()
        #to change the file name of video
        p=Path(b)
        p=p.rename(p.with_name("Cache.mp4"))
        
        latest_iteration.text(f'{int(time.time()-e)} Second')
        bar.progress(60)
        #to merge the file 
        import ffmpeg
        import subprocess    
        p='Cache.mp4'
        q='Audio.mp3'
        subprocess.call("cd", shell=True )
        subprocess.call(f"ffmpeg -i {p} -i {q} -c:v copy -c:a aac -strict experimental YoutubeVideo.mp4",shell=True)
        latest_iteration.text(f'{int(time.time()-e)} Second')
        bar.progress(90)
    if (option==2):
        os.remove(p)
        os.remove(q)
    
        
    
    latest_iteration.text(f'{int(time.time()-e)} Second')
    bar.progress(100)
st.title("Download Youtube Video")
link=st.text_input("Youtube URL")
res=st.selectbox("Select The resolution",("720p","144p","240p","360p","480p","720p","1080p","1460p","2160p","4320p"))
option = st.selectbox("Audio(1) or Video(2)",(1,2))
a=st.button("Start Downloading")
if (a):
    download(link,res,option)
    if option==2:
        with open('YoutubeVideo.mp4', 'rb') as f:
            st.download_button('Save Video', f, file_name='YoutubeVideo.mp4')
        os.remove("YoutubeVideo.mp4")    
    else :
        with open("Audio.mp3",'rb' ) as f:
            st.download_button("Save Audio",f,"Music.mp3") 
        os.remove("Audio.mp3")

