import os
import yt_dlp


def download_playlist_audio_from_youtube(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data',
                                '%(title)s.%(ext)s'),
        'yesplaylist': True
    }
    if not os.path.exists(os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data')):
        os.makedirs(os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data'))
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

def download_audio_from_youtube(url):
    ydl_opts = {
        'format': 'bestaudio/best',
        'outtmpl': os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data', '%(title)s.%(ext)s')
    }
    if not os.path.exists(os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data')):
        os.makedirs(os.path.join(os.path.expanduser('~'), 'Downloads', 'Youtube download', 'data'))
    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url])

print("1- une seule vidéo")
print("2- une playlist")
choix = int(input("choisissez 1 ou 2"))

if choix == 1:
    url = input("URL de la vidéo YouTube : ")
    download_audio_from_youtube(url)
elif choix == 2:
    url = input("URL de la playlist YouTube : ")
    download_playlist_audio_from_youtube(url)
else:
    print("on t'a dis 1 ou 2!")

