import argparse
import logging
import threading
from pytubefix import Playlist,YouTube
from pytubefix.cli import on_progress

print("Fast Youtube Video Downloader by \033[91m" + "BWS" + "\033[0m \033[94m" + "(https://github.com/blackwallsentinel)" + "\033[0m")


import tkinter as tk
from tkinter import ttk


class DownloadThread(threading.Thread):
    def __init__(self, url, audio_only):
        threading.Thread.__init__(self)
        self.url = url
        self.audio_only = audio_only

    def run(self):
        if self.audio_only:
            v = YouTube(self.url, client='web')
            ys = v.streams.get_audio_only()
            print("Downloading audio of " + v.title + "...")
            try:
                ys.download(mp3=True)
            except Exception as e:
                if "IncompleteRead" in str(e):
                    print("Incomplete read. Continuing anyway.")
                else:
                    raise
            print("Done!")

        else:
            v = YouTube(self.url,client='web')
            ys = v.streams.get_highest_resolution()
            print("Downloading " + v.title + "...")
            try:
                ys.download()
            except Exception as e:
                if "IncompleteRead" in str(e):
                    print("Incomplete read. Continuing anyway.")
                else:
                    raise
            print("Done!")


class PlaylistDownloadThread(threading.Thread):
    def __init__(self, url, audio_only):
        threading.Thread.__init__(self)
        self.url = url
        self.audio_only = audio_only

    def run(self):
        p = Playlist(self.url)
        for video in p.videos:
            v = YouTube(video.watch_url,client='web')
            if self.audio_only:
                ys = v.streams.get_audio_only()
                print("Downloading audio of " + v.title + "...")
                try:
                    ys.download(mp3=True)
                except Exception as e:
                    if "IncompleteRead" in str(e):
                        print("Incomplete read. Continuing anyway.")
                    else:
                        raise
                print("Done!")
            else:
                ys = v.streams.get_highest_resolution()
                print("Downloading " + v.title + "...")
                try:
                    ys.download()
                except Exception as e:
                    if "IncompleteRead" in str(e):
                        print("Incomplete read. Continuing anyway.")
                    else:
                        raise
                print("Done!")


def select_video():
    url = entry.get()
    DownloadThread(url, var.get()).start()


def select_playlist():
    url = entry.get()
    PlaylistDownloadThread(url, var.get()).start()


window = tk.Tk()
window.title("Youtube Video Downloader")

# Create style
style = ttk.Style()
style.configure('TFrame', background='#f0f0f0')
style.configure('TButton', font=('Helvetica', 12), foreground='#000000')
style.configure('TLabel', font=('Helvetica', 12), foreground='#000000')
style.configure('TEntry', font=('Helvetica', 12), foreground='#000000')
style.configure('TCheckbutton', font=('Helvetica', 12), foreground='#000000')

frame = ttk.Frame(window, style='TFrame', padding="30 30 30 30")
frame.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
window.columnconfigure(0, weight=1)
window.rowconfigure(0, weight=1)

ttk.Label(frame, text="Enter video or playlist URL:", style='TLabel').grid(column=0, row=0, sticky=(tk.W, tk.E))
entry = ttk.Entry(frame, width=50, style='TEntry')
entry.grid(column=0, row=1, sticky=(tk.W, tk.E))
ttk.Button(frame, text="Download Video", command=select_video, style='TButton').grid(column=0, row=2, sticky=tk.W)
ttk.Button(frame, text="Download Playlist", command=select_playlist, style='TButton').grid(column=1, row=2, sticky=tk.W)
var = tk.IntVar()
ttk.Checkbutton(frame, text="Audio only", variable=var, style='TCheckbutton').grid(column=0, row=3, sticky=tk.W)


window.mainloop()


