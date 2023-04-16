
import zipfile
import streamlit as st
from pathlib import Path
from pytube import YouTube,Playlist
import os , time,random,sys,asyncio
# To Download Any youtube video
st.cache()
def download(link,res,option):
    yt = YouTube(link)
    #Making title 
    global title
    title=""
    til=yt.title
    for i in til :
        if (i==":"or i=="|" or i=="." or i=="/" or i=="\\" or i=="?" or i==">" or i=="<" or i==","):
            title+=" "
        else: title+=i    
    #For Audio     File - q   
    if (option==1):
        audio = yt.streams.get_by_itag(yt.streams.filter(type="audio",mime_type="audio/webm")[0].itag)
        a = audio.download()
        global q
        q=Path(a)
        q=q.rename(q.with_name(f"{number} {title}.mp3"))
    # For only quality of three types  -  File p   
    elif (res=="720p"or res=="144p"  or res=="360p"):
        video = yt.streams.get_by_itag(yt.streams.filter(res=res , progressive="True" )[0].itag)
        
        v=video.download()
        global p
        p = Path(v)
        p=p.rename(p.with_name(f"{number} {title}.mp4"))
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
st.set_page_config(page_title="Download Now",page_icon="images/logo.png",menu_items={
    "Get help": "https://github.com/dudegladiator/YoutubeDownloader",
    "Report a bug" : "https://github.com/dudegladiator/YoutubeDownloader/issues"
    
})
st.title("Download Youtube Video")
global number
number=random.randrange(1,1000)
link=st.text_input("Youtube Video or Playlist URL")

loc=st.radio("Where it is working",("On Cloud(Using Website Version)","Local Server(Highest Quality Available)"))

#Local
if (loc=="Local Server(Highest Quality Available)"):
    #For Playlist
    if ("playlist" in link):
        try :
            ytplay=Playlist(link)
        except :
            st.write("Link is not valid")
            st.stop()
        option = st.selectbox("Audio(1) or Video(2)",(1,2))
        # for video
        if (option==2):
                res=st.selectbox("Select The resolution",("720p","144p","240p","360p","480p","1080p","1440p","2160p","4320p"))
                a=st.button("Start Downloading")
                if "load_state" not in st.session_state:
                    st.session_state.load_state = False
                if a or st.session_state.load_state:
                    st.session_state.load_state=True
                    
                    for i , url in enumerate(ytplay.video_urls,random.randrange(1,1000)):
                        number=i
                        try : 
                            download(url,res,option)
                        except IndexError:
                            st.write("Resolution not available")
                            st.stop()
                        except :
                            st.write("Try Again")
                            st.experimental_rerun()    
                        st.write(f"{number} {title}")
                        if (res=="720p"or res=="144p"  or res=="360p"):
                            st.write("Automatically Saved in opened Folder or in your admisntration Folder")
                        else :
                            st.write("Automatically Saved in opened Folder or in your admisntration Folder")
                                
                                
                                
            #For Audio
        else:
                a=st.button("Start Downloading") 
                if "load_state" not in st.session_state:
                    st.session_state.load_state = False
                if a or st.session_state.load_state:
                    st.session_state.load_state=True
                    for i , url in enumerate(ytplay.video_urls,random.randrange(1,1000)):
                        number=i
                        try:
                            download(url,"360p", option)
                        except :
                            st.write("Try Again")
                            st.experimental_rerun()
                        
                        st.write(f"{number} {title}")
                        st.write("Automatically Saved in opened Folder or in your admisntration Folder")
                 
                              
    #For Single video
    else:
        option = st.selectbox("Audio(1) or Video(2)",(1,2))
        #For Video
        if (option==2):
            res=st.selectbox("Select The resolution",("720p","144p","240p","360p","480p","1080p","1440p","2160p","4320p"))
            a=st.button("Start Downloading")
            if a:
                number+=1
                try : 
                    download(link,res,option)
                except IndexError:
                    st.write("Resolution not available")
                    st.stop()
                except :
                    st.write("Try Again")
                    st.experimental_rerun()    
                        
                st.write(f"{number} {title}")
                if (res=="720p"or res=="144p"  or res=="360p"):
                   st.write("Automatically Saved in opened Folder or in your admisntration Folder") 
                else :
                    st.write("Automatically Saved in opened Folder or in your admisntration Folder")
        #For Audio
        else:
            a=st.button("Start Downloading")
            if a:
                number+=1
                try:
                    download(link, "360p", option)
                except:
                    st.write("Try Again")
                    st.experimental_rerun()
                st.write(f"{number} {title}")
                st.write("Automatically Saved in opened Folder or in your admisntration Folder")     
                      
# cloud                        
else :
    #For Playlist    
    if ("playlist" in link):
        try :
            ytplay=Playlist(link)
        except :
            st.write("Link is not valid")
            st.stop()
        #Downloading all
        
        option = st.selectbox("Audio(1) or Video(2)",(1,2))
            # for video
        if (option==2):
                res=st.selectbox("Select The resolution",("720p","144p","360p"))
                a=st.button("Start Downloading")
                if "load_state" not in st.session_state:
                    st.session_state.load_state = False
                if a or st.session_state.load_state:
                    st.session_state.load_state=True
                    k= random.randrange(1,1000)   
                    for i , url in enumerate(ytplay.video_urls,random.randrange(1,1000)):
                        number=i
                        try : 
                            download(url,res,option)
                        except IndexError:
                            st.write("Resolution not available")
                            st.stop()
                        except :
                            st.write("Try Again")
                            st.experimental_rerun()    
                            
                        st.write(f"{number} {title}")
                         
                        with zipfile.ZipFile(f"{k} Youtube videos.zip", mode="a") as archive:
                            archive.write(p)
                   with open(f"{k} Youtube videos.zip",'rb') as f:
                            st.download_button(label='Save File', data=f ,file_name=f"{k} Youtube videos.zip")         
            #For Audio
        else:
                a=st.button("Start Downloading")  
                if "load_state" not in st.session_state:
                    st.session_state.load_state = False
                if a or st.session_state.load_state:
                    st.session_state.load_state=True
                    for i , url in enumerate(ytplay.video_urls,random.randrange(1,1000)):
                        number=i
                        try:
                            download(url, "360p", option)
                        except :
                            st.write("Try Again")
                            st.experimental_rerun()
                            
                        st.write(f"{number} {title}")
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
                number+=1
                try:
                    download(link,res, option)
                except IndexError:
                    st.write("Resolution not available")
                    st.stop()
                except :
                    st.write("Try Again")
                    st.experimental_rerun() 
                st.write(f"{number} {title}")
                with open(p,'rb') as f:
                    st.download_button(label='Save Video', data=f ,file_name=f"{title}.mp4")
        #For Audio            
        else:
            a=st.button("Start Downloading")
            if a:
                number+=1
                try:
                    download(link,"360", option)
                except:
                    st.write("Try Again")
                    st.experimental_rerun()
                st.write(f"{number} {title}")
                with open(q,'rb' ) as f:
                    st.download_button("Save Audio",f,file_name=f"{title}.mp3")           
                    
"Follow Me On Github - https://github.com/dudegladiator" 
                   
