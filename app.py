from flask import Flask, render_template, redirect, request
# from flask_ngrok import run_with_ngrok
from pytube import YouTube, Playlist
import subprocess
import os


app = Flask(__name__)


# Tried ngrok to make it temporarily accessible over the internet
# run_with_ngrok(app)


# Functions
def download(url):
    yt = YouTube(url)
    video = yt.streams.get_highest_resolution()

    # find the user's download directory, if doesn't exist, then create it for them
    userHomeDir = os.path.expanduser("~")
    userDownloadDir = os.path.join(userHomeDir, "Downloads")
    os.makedirs(userDownloadDir, exist_ok=True)
    targetDownloadPath = userDownloadDir

    videoPath = video.download(targetDownloadPath)
    print(videoPath)
    audioPath = videoPath.replace(".mp4", ".mp3")
    print(audioPath)

    subprocess.run(['ffmpeg', '-i', videoPath, '-q:a', '0', '-map', 'a', audioPath])


# Routes
@app.route('/')
def start():
    return 'This is a Chrome extension for downloading YouTube Videos simply by inputting their URLs!'


@app.route('/downloadVideo', methods=['GET'])
def downloadVideo():
    try:
        YouTubeUrl = request.args.get('youTubeUrl')
        print(YouTubeUrl)
        download(YouTubeUrl)

        print("Successfully Downloaded Video")
        return redirect('/')
    
    except Exception as e:
        return f"Error Occurred: {e}"
    

@app.route('/downloadPlaylist', methods=['GET'])
def downloadPlaylist():
    try:
        playlistUrl = request.args.get('playlistUrl')

        playlist = Playlist(playlistUrl)

        # show the number of videos contained in the playlist
        print(f"Number of videos in the playlist: {len(playlist.video_urls)}")

        for url in playlist:
            download(url)

        print("Successfully Downloaded Playlist")
        return redirect('/')
    
    except Exception as e:
        return f"Error Occurred: {e}"


# flask run will successfully run the server without the code below, but python3 app.py can only run the server successfully with the code below
if __name__ == '__main__':
    app.run(port=8000, debug=False)

# using heroku:
    # to update the heroku website: git push heroku main
    # to open the heroku website: heroku open