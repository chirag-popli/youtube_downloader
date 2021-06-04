import pytube
from pytube import YouTube
import os

class Downloader():
    def Both(link):
        yt = YouTube(link)
        title = yt.title
        finales = yt.streams.get_highest_resolution()
        return finales.download(output_path=r"C:\Users\chiragpopli\Desktop")

    def audio(self,link):
        self.yt = YouTube(link)
        title = self.yt.title
        finales = self.yt.streams.filter(adaptive=True, only_audio=True).get_audio_only()
        out_file=finales.download(output_path=r"C:\Users\chiragpopli\Desktop")
        base, ext = os.path.splitext(out_file)
        new_file = base + '.mp3'
        os.rename(out_file, new_file)
        print("done")
