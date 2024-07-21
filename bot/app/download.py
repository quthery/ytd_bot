import yt_dlp
import asyncio
import datetime 



class Downloader:
    def __init__(self, res=None):
        self.ydl_opts = {  
            "format" : 'best',
            'outtmpl': 'bot/videos/%(id)s.%(ext)s',
            'quiet': True,
        }
        
    
    async def download_video(self, url, fsipath: str) -> str:
        with yt_dlp.YoutubeDL({'outtmpl': fsipath+"/%(id)s.%(ext)s", 'quiet': True,}) as ydl:
            await asyncio.get_event_loop().run_in_executor(None, ydl.download, url)

        return self.ydl_opts['outtmpl']
    

ytd = Downloader()


    
