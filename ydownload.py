import pafy
import requests
import os
import test
#---------------------------------------
limt = 50000000

class file_size_ex(Exception):
	def __str__(self):
		return "Max size is 50MB"

class erroe_download(Exception):
	def __str__(self):
		return "Unaple to download this file"
class YTADL:
    """YoutubeAudioDl object to carry out download operation"""
    def __init__(self, url: str, url_only=False):
        self.vid_id = test.get_video_id(url)
        if self.vid_id == "":
            raise ValueError("Invalid YouTube URL")
        self.url = "https://www.youtube.com/watch?v=" + self.vid_id
        self.pafy_obj = None
        self.audio_stream = None
        self.size = None
        self.downloadable = None
        self.file_title = None
        self.file_ext = None
        self.filename = None
        self.audio_file = None
        self.thumbnail = None
   
class YTDOWNLOAD:
	def __init__ (self, url:str, url_only=False):
		self.video_ID = test.get_video_id(url)
		if self.video_ID ==" ":
			raise ValueError("Invalid YouTube URL")
		self.URL = "https://www.youtube.com/watch?v="+self.video_ID
		if not test.test_url(self.URL):
			raise ValueError("Invalid Youtube URL")
		self.pafy_obj = None
		self.audio_stream =None
		self.size = None
		self.candown = None
		self.title =None
		self.name =None
		self.ext=None
		self.audio_file = None
		self.TBM=None
		if not url_only:
			self.make_audio_stream()
			#self.processor_url()
	#--------------------------------------------------------
	def processor_url(self):
		"""Starts processing link and gather meta infos"""
		self.pafy_obj = pafy.new(self.video_ID, size=True)
	#	self.audio_stream = self.pafy_obj.getbestaudio(preftype='m4a')
		#self.size = self.audio_stream.get_filesize()
		#self.candown = False
		#if self.size > limt:
		#    print("Bot will not be able to send file above 50MB!")
		 #   raise file_size_ex
		#self.candown = True
		#self.title = self.pafy_obj.title.replace('/', '_').replace('<', '_').replace('>', '_')
		#self.ext = self.audio_stream.extension
		#self.name = ''
		#self.audio_file = None
		#self.TBM = requests.get(self.pafy_obj.getbestthumb()).content



	def make_audio_stream(self):
		self.pafy_obj = pafy.new(self.video_ID,size=True)
		self.audio_stream = self.pafy_obj.getbestaudio(preftype='m4a')
		self.size = self.audio_stream.get_filesize()
		self.candown = False
		if self.size >  limt:
			print("Max size 50MB!")
			raise file_size_ex
		self.candown=True
		self.title = self.pafy_obj.title.replace('/', '_').replace('<', '_').replace('>', '_')
		self.ext   =self.audio_stream.extension
		self.name = ' '
		self.audio_file=None
		self.TBM = requests.get(self.pafy_obj.getbestthumb()).content

	def download (self):
		self.name =self.audio_stream.download(quiet= True)
		if self.name is None:
			self.name = self.title + "."+self.ext
		try:
			self.audio_file = open(self.name,'rb')
		except erroe_download:
			print ("can't download this video")
			raise erroe_download

def pretty_url_string(urls: list) -> str:
    pretty_url = ""
    if len(urls) == 0:
        return "No valid url found"
    elif len(urls) > 1:
        pretty_url += f"Received {len(urls)} links\n"
        i = 1
        for url in urls:
            pretty_url += f"{i}. {url}\n"
            i += 1
    pretty_url += "Downloading ..."

    return pretty_url[:4096]


#------------------------------------------------------
