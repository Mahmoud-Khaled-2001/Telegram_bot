import re
from urllib import request, error
import requests
from urlextract import URLExtract
from urllib.parse import urlparse, parse_qs
#---------------------------------------------------
def get_video_id (url:str):
	lin_det = urlparse(url)
	if lin_det.hostname == 'youtu.be':
		return lin_det.path[1:]
	if lin_det.hostname in ('www.youtube.com', 'youtube.com'):
		#if lin_det.path == '/watch':
		#	p =parse_qs(lin_det)
		#	return p['v'][0]
		if lin_det.path == '/watch':
			p = parse_qs (lin_det.query)
			return p ['v'][0]
		if lin_det.path[:7]== '/embed/':
			return lin_det.path.split('/')[2]
		if lin_det.path[:3]=='/v/':
			return lin_det.path.split('/')[2]
	return " "
def test_url (id:str):
	url_checker = "https://www.youtube.com/oembed?url="
	video_url = url_checker +id
	req = requests.get(video_url)
	return req.status_code == 200
def get_link_text (text:str):
	urls = URLExtract().find_urls(text)
	lis_urls = []
	for url in urls:
		if test_url(url):
			lis_urls.append(url)
	return lis_urls
#def download_txt (urls:list):
#	url = ""
#	if len(urls)==0:
#		print("url not found")
#	elef len(urls)>1
def sectime(ti_me:str):
	h,m,s= ti_me.split(':')
	return int(h) * 3600 + int(m) * 60 + int(s)
