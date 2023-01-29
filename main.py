def download(link,res,option): 
    
    from pathlib import Path
    from pytube import YouTube
    import os 
    
    #taking link and res as input
    # link = input("Enter the Youtube Video URL : ")
    # res=input ("Resolution e.g-2160p,1440p,4320p etc : ")
    # option=int(input('''To get Audio - Type 1 \nTo get Video - Type 2 \nTo get Both -  Type 3 \nYour Option No - '''))
    #creating a  object of youtube video
    yt = YouTube(link)
    
    
    audio = yt.streams.get_by_itag(yt.streams.filter(type="audio")[0].itag)
    
    
    a=audio.download()
    
    
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
        subprocess.run(f"ffmpeg -i {p} -i {q} -c copy YoutubeVideo.mp4")
        
    if (option==2):
        os.remove(p)
        os.remove(q)
    
        
    
    