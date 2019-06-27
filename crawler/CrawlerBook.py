import urllib.request
import os
import re

def writeFile(file,content):
    file.write(content)

def getContent(data):
	pattern = re.compile('查找最新章节！<br />(.*)<p>大唐兴亡三百年最新章节地址：',re.S)
	for m in re.finditer(pattern,data):
		content=m.group(1).replace("<br /><br />","\n").replace("&nbsp;&nbsp;&nbsp;&nbsp;","    ")
		return content
	return

try:
	fo = open("/Users/yangyibo/Desktop/data.txt","a+",encoding="utf-8")
	for num in range(34,82):
		url = "https://www.shuhaige.com/55321/4211"+str(num)+".html"
		print (url)
		webPage=urllib.request.urlopen(url)
		data = webPage.read().decode('utf-8')
		data = data.replace("\n","")
		# print(data)
		content=getContent(data)
		writeFile(fo,"\n第"+str(num-16)+"章节\n")
		print("\n第"+str(num-16)+"章节\n")
		writeFile(fo,content)
except Exception as e:
	print (e)
