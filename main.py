import argparse
from pytubefix import Playlist,YouTube
from pytubefix.cli import on_progress

print("Fast Youtube Video Downloader by \033[91m" + "BWS" + "\033[0m \033[94m" + "(https://github.com/blackwallsentinel)" + "\033[0m")

parser = argparse.ArgumentParser()
group = parser.add_mutually_exclusive_group(required=True)
group.add_argument("-v", "--video", help="url of a video")
group.add_argument("-p", "--playlist", help="url of a playlist")
parser.add_argument("-a", "--audio_only", help="download audio only", action="store_true")
args = parser.parse_args()

if args.playlist:
    p = Playlist(args.playlist)
    for video in p.videos:
        v = YouTube(video.watch_url,on_progress_callback = on_progress)
        if args.audio_only:
           ys = v.streams.get_audio_only()
           print("Downloading audio of " + v.title + "...")
           ys.download(mp3=True)
           print("Done!")
           
        else:

            ys = v.streams.get_highest_resolution()
            print("Downloading audio of " + v.title + "...")
            ys.download()
            print("Done!")

elif args.video:
    v = YouTube(args.video)
    if args.audio_only:
        ys = v.streams.get_audio_only()
        print("Downloading audio of " + v.title + "...")
        ys.download(mp3=True)
        print("Done!")
    else:
        ys = v.streams.get_highest_resolution()
        print("Downloading " + v.title + "...")
        ys.download()
        print("Done!")
