#encoding:UTF-8 python2.7 爬虫糗事百科
import urllib
import urllib2
import re
import os

class CrawlerImg:
	def __init__(self):
		self.url = 'http://pic.qiushibaike.com/system/avtnew/3504/35042196/thumb/20171029101448.JPEG?imageView2/1/w/90/h/90' 
		self.user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
		self.headers = { 'User-Agent' : self.user_agent }

	def getPage(self):
		request = urllib2.Request(self.url,headers=self.headers)
		response= urllib2.urlopen(request)
		content = response.read()
		# python 2中打开文件用file python3 中打开文件用 open
		f = file('/Users/yangyibo/Desktop/1.jpg','wb+')
		f.write(content)
		f.close()

crawlerImg = CrawlerImg()
crawlerImg.getPage()



