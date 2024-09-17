import yt_dlp
import asyncio
import datetime 



class Downloader:
    def __init__(self, res=None):
        self.ydl_opts = {  
            "format" : 'best',
            'outtmpl': 'bot/videos/%(id)s.%(ext)s',
            "simulate": True,
            "forceurl": True,
            'quiet': True,
        }
        
    def get_direct_link(video_url) -> str:
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            'no_warnings': True,
            'outtmpl': '%(id)s.%(ext)s',
            'merge_output_format': 'mp4'
            }
        with yt_dlp.YoutubeDL(ydl_opts) as ytdl:
            info = ytdl.extract_info("https://twitter.com/MissMikkaa/status/1568324392953827328", download=False)
            url = info["url"]
        print(url)
        return url
    
    def get_direct_link1(video_url):
        ydl_opts = {
            'format': 'bestvideo[height<=720]+bestaudio/best[height<=720]',
            'quiet': True,
            'no_warnings': True,
            'outtmpl': '%(id)s.%(ext)s',
            'merge_output_format': 'mp4'
            }
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            info_dict = ydl.extract_info(video_url, download=False)
        L = info_dict['formats']
        for x in range(len(L)):
            if L[x].get('height', 0) == 1280:
                direct_link = L[x]['url']
                print(direct_link)
                return direct_link


    async def download_video(self, url, fsipath: str) -> str:
        with yt_dlp.YoutubeDL({'outtmpl': fsipath+"/%(id)s.%(ext)s", 'quiet': True,}) as ydl:
            await asyncio.get_event_loop().run_in_executor(None, ydl.download, url)

        return self.ydl_opts['outtmpl']
    



    
