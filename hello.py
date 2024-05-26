from pytube import YouTube
from tkinter import *

def downloader(url,radval):
    yt = YouTube(url=url)
    # if radval == 1:

    print("Download started")
    print(yt.streams.filter(progressive=True))
    print(yt.streams.filter())
    # stream = yt.streams.get_by_itag(itag=18)
    # for i in range(3):
    #     if stream is None:
    #         print(f"Stream none.....Retrying attempt {i}")
    #         stream = yt.streams.get_by_itag(itag=18)

    # #     # print(stream)
    #     else:
    #         stream.download(filename="ytdownload.mp4",output_path="C:/Users/masge/Downloads")
    #         print("Download done")
    #         break
    # # [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="24fps" vcodec="avc1.640028" progressive="False" type="video">, <Stream: itag="248" mime_type="video/webm" res="1080p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="24fps" vcodec="avc1.4d401f" progressive="False" type="video">, <Stream: itag="247" mime_type="video/webm" res="720p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="244" mime_type="video/webm" res="480p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="24fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="24fps" vcodec="avc1.4d4015" progressive="False" type="video">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="24fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="24fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]
    # [<Stream: itag="18" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.42001E" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="22" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001F" acodec="mp4a.40.2" progressive="True" type="video">, <Stream: itag="137" mime_type="video/mp4" res="1080p" fps="30fps" vcodec="avc1.640028" progressive="False" type="video">, <Stream: itag="248" mime_type="video/webm" res="1080p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="136" mime_type="video/mp4" res="720p" fps="30fps" vcodec="avc1.64001f" progressive="False" type="video">, <Stream: itag="247" mime_type="video/webm" res="720p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="135" mime_type="video/mp4" res="480p" fps="30fps" vcodec="avc1.4d401f" progressive="False" type="video">, <Stream: itag="244" mime_type="video/webm" res="480p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="134" mime_type="video/mp4" res="360p" fps="30fps" vcodec="avc1.4d401e" progressive="False" type="video">, <Stream: itag="243" mime_type="video/webm" res="360p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="133" mime_type="video/mp4" res="240p" fps="30fps" vcodec="avc1.4d4015" progressive="False" type="video">, <Stream: itag="242" mime_type="video/webm" res="240p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="160" mime_type="video/mp4" res="144p" fps="30fps" vcodec="avc1.4d400c" progressive="False" type="video">, <Stream: itag="278" mime_type="video/webm" res="144p" fps="30fps" vcodec="vp9" progressive="False" type="video">, <Stream: itag="139" mime_type="audio/mp4" abr="48kbps" acodec="mp4a.40.5" progressive="False" type="audio">, <Stream: itag="140" mime_type="audio/mp4" abr="128kbps" acodec="mp4a.40.2" progressive="False" type="audio">, <Stream: itag="249" mime_type="audio/webm" abr="50kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="250" mime_type="audio/webm" abr="70kbps" acodec="opus" progressive="False" type="audio">, <Stream: itag="251" mime_type="audio/webm" abr="160kbps" acodec="opus" progressive="False" type="audio">]

def user_input():
    url = text_inp.get()
    if var.get() == 1:
        downloader(url=url,radval=1)
    if var.get() == 2:
        downloader(url=url,radval=2)
    if var.get() == 3:
        downloader(url=url,radval=3)
    if var.get() == 4:
        downloader(url=url,radval=4)
    if var.get() == 5:
        downloader(url=url,radval=5)

# def radio():
   

root = Tk()
var = IntVar()
label = Label(text="YouTube Downloader",font=50)
label.place(x=410,y=0)
chkbtn1 = Radiobutton(root,text="144p",value=1,variable=var)
chkbtn2 = Radiobutton(text="240p",value=2,variable=var)
chkbtn3 = Radiobutton(text="360p",value=3,variable=var)
chkbtn4 = Radiobutton(text="720p",value=4,variable=var)
chkbtn5 = Radiobutton(text="1080p",value=5,variable=var)
chkbtn1.place(x=350,y=200)
chkbtn2.place(x=350,y=230)
chkbtn3.place(x=350,y=260)
chkbtn4.place(x=350,y=290)
chkbtn5.place(x=350,y=320)
text_inp = Entry(width=50)
text_inp.place(x=350,y=100)
button = Button(text="Download",command=user_input)
button.place(x=450,y=150)
root.title("YouTube Downloader")
root.geometry("900x500")
root.mainloop()