import streamlit as st
from pathlib import Path
from pytube import YouTube,Playlist
import os , time,random,sys

# To Download Any youtube video
def download(link,res,option,number=1):
    yt = YouTube(link)
    #Making title 
    global title
    title=""
    til=yt.title
    for i in til :
        if (i==":"or i=="|" or i=="."):
            title+=" "
        else: title+=i    
    #For Audio     File - q   
    if (option==1):
        audio = yt.streams.get_by_itag(yt.streams.filter(type="audio")[0].itag)
        a = audio.download()
        global q
        q=Path(a)
        q=q.rename(q.with_name(f"{number}music.mp3"))
    # For only quality of three types  -  File p   
    if (res=="720p"or res=="144p"  or res=="360p"):
        video = yt.streams.get_by_itag(yt.streams.filter(res=res , progressive="True" )[0].itag)
        
        v=video.download()
        global p
        p = Path(v)
    #This can't be run on cloud based  - File k    
    else :
        audio = yt.streams.get_by_itag(yt.streams.filter(type="audio")[0].itag)  
        video = yt.streams.get_by_itag(yt.streams.filter(res=res , type="video" )[0].itag)
        
        v = video.download()
        p=Path(v)
        
        p = p.rename(p.with_name("CacheVid.mp4"))
        a = audio.download()
        q=Path(a)
        q = q.rename(q.with_name("CacheAud.mp3"))
        import ffmpeg
        import subprocess
        subprocess.run(f"ffmpeg -i {p} -i {q} -c copy youtube.mp4")
        global k
        k=Path("youtube.mp4")
        k=k.rename(k.with_name(f"{number} {title}.mp4"))
        os.remove(p)
        os.remove(q)


# From here Website start

st.title("Download Youtube Video")
link=st.text_input("Youtube Video or Playlist URL")
loc=st.radio("Where it is working",("Local","Cloud"))
#Local
if (loc=="Local"):
    #For Playlist
    if ("playlist" in link):
        ytplay=Playlist(link)
        opt=st.radio("Choose the Option",("Download All","Choose(Bug)"))
        #Downloading all
        if (opt=="Download All"):
            option = st.selectbox("Audio(1) or Video(2)",(1,2))
            # for video
            if (option==2):
                res=st.selectbox("Select The resolution",("720p","144p","240p","360p","480p","1080p","1440p","2160p","4320p"))
                a=st.button("Start Downloading")
                if a:
                    for i , url in enumerate(ytplay.video_urls,1):
                        st.write(f"Video-{i}")
                        download(url,res,option,i)
                        if (res=="720p"or res=="144p"  or res=="360p"):
                            with open(p,'rb') as f:
                                st.download_button(label='Save Video', data=f ,file_name=f"{i} {title}.mp4") 
                        else :
                            with open(k,'rb') as f:
                                st.download_button(label='Save Video', data=f ,file_name=f"{i} {title}.mp4")
            #For Audio
            else:
                a=st.button("Start Downloading")  
                if a:
                    for i , url in enumerate(ytplay.video_urls,1):
                        st.write(f"Audio-{i}")
                        download(url, "720p", option)
                        with open(q,'rb' ) as f:
                            st.download_button("Save Audio",f,file_name=f"{i} {title}.mp3")
        #Choosing
        else:
            option = st.selectbox("Audio(1) or Video(2)",(1,2))
            # for video
            if (option==2):
                a=st.button("Start Downloading")
                if a:
                    for i , url in enumerate(ytplay.video_urls,1):
                        st.write(f"Video-{i}")
                        res=st.selectbox(f"Select The resolution {i}",("720p","144p","240p","360p","480p","1080p","1440p","2160p","4320p"))
                        w=st.radio(f"Wanna Download {i}",("k","No2","Yes2"))
                        if (w=="Yes2"):
                            download(url,res,option,i)
                            if (res=="720p"or res=="144p"  or res=="360p"):
                                with open(p,'rb') as f:
                                    st.download_button(label='Save Video', data=f ,file_name=f"{i} {title}.mp4") 
                            else :
                                with open(k,'rb') as f:
                                    st.download_button(label='Save Video', data=f ,file_name=f"{i} {title}.mp4")
                        elif(w=="No2") :
                            continue            
            #For Audio
            else:
                a=st.button("Start Downloading")  
                if a:
                    for i , url in enumerate(ytplay.video_urls,1):
                        st.write(f"Audio-{i}")
                        z=st.radio(f"Wanna Download {i}",("No1","Yes1"))
                        if (z=="Yes1"): 
                            download(url, "720p", option)
                            with open(q,'rb' ) as f:
                                st.download_button("Save Audio",f,file_name=f"{i} {title}.mp3")
                        elif(z=="No1") : 
                            continue         
                           
                              
    #For Single video
    else:
        option = st.selectbox("Audio(1) or Video(2)",(1,2))
        #For Video
        if (option==2):
            res=st.selectbox("Select The resolution",("720p","144p","240p","360p","480p","1080p","1440p","2160p","4320p"))
            a=st.button("Start Downloading")
            if a:
                download(link,res,option)
                if (res=="720p"or res=="144p"  or res=="360p"):
                   with open(p,'rb') as f:
                        st.download_button(label='Save Video', data=f ,file_name=f"{title}.mp4") 
                else :
                    with open(k,'rb') as f:
                        st.download_button(label='Save Video', data=f ,file_name=f"{title}.mp4")
        #For Audio
        else:
            a=st.button("Start Downloading")
            if a:
                download(link, "720p", option)
                with open(q,'rb' ) as f:
                    st.download_button("Save Audio",f,file_name=f"{title}.mp3")       
# cloud                        
else :
    #For Playlist    
    if ("playlist" in link):
        ytplay=Playlist(link)
        opt=st.radio("Choose the Option",("Download All","Choose(BUG)"))
        #Downloading all
        if (opt=="Download All"):
            option = st.selectbox("Audio(1) or Video(2)",(1,2))
            # for video
            if (option==2):
                res=st.selectbox("Select The resolution",("720p","144p","360p"))
                a=st.button("Start Downloading")
                if a:
                    for i , url in enumerate(ytplay.video_urls,1):
                        st.write(f"Video-{i}")
                        download(url,res,option,i)
                        with open(p,'rb') as f:
                            st.download_button(label='Save Video', data=f ,file_name=f"{i} {title}.mp4") 
                        
            #For Audio
            else:
                a=st.button("Start Downloading")  
                if a:
                    for i , url in enumerate(ytplay.video_urls,1):
                        st.write(f"Audio-{i}")
                        download(url, "720p", option)
                        with open(q,'rb' ) as f:
                            st.download_button("Save Audio",f,file_name=f"{i} {title}.mp3")

    #For single Video
    else:
        option = st.selectbox("Audio(1) or Video(2)",(1,2))
        #For Video
        if (option==2):
            res=st.selectbox("Select The resolution",("720p","144p","360p"))
            a=st.button("Start Downloading")
            if a:
                download(link,res,option)
                with open(p,'rb') as f:
                    st.download_button(label='Save Video', data=f ,file_name=f"{title}.mp4")
        #For Audio            
        else:
            a=st.button("Start Downloading")
            if a:
                download(link, "720p", option)
                with open(q,'rb' ) as f:
                    st.download_button("Save Audio",f,file_name=f"{title}.mp3")           
