import urllib.request
import os
import re
import gzip
from io import BytesIO



def writeFile(file,content):
    file.write(content)

def getContent(data):
	pattern = re.compile('查找最新章节！<br />(.*)<p>大唐兴亡三百年最新章节地址：',re.S)
	for m in re.finditer(pattern,data):
		content=m.group(1).replace("<br /><br />","\n").replace("&nbsp;&nbsp;&nbsp;&nbsp;","    ")
		return content
	return

def noGzipBook():
	try:
		fo = open("/Users/yangyibo/Desktop/data.txt","a+",encoding="utf-8")
		for num in range(34,82):
			# url = "https://www.shuhaige.com/55321/4211"+str(num)+".html"
			url = "http://book.sbkk8.com/waiguo/feidu/164069.html"
			webPage=urllib.request.urlopen(url)
			print(webPage)
			# data = webPage.read().decode('utf-8')
			# data = data.replace("\n","")
			# print(data)
			# content=getContent(data)
			# writeFile(fo,"\n第"+str(num-16)+"章节\n")
			# print("\n第"+str(num-16)+"章节\n")
			# writeFile(fo,content)
	except Exception as e:
		print (e)


def getContentQiSu(data):
	pattern = re.compile('<a href="/bookcase.php" >我的书架</a>(.*)投推荐票</a>',re.S)
	for m in re.finditer(pattern,data):
		content=m.group(1).replace("<br />","\n").replace("&nbsp;&nbsp;&nbsp;&nbsp;","    ")
		return content
	return


def haveGzipBook(fo):
	try:
		for num in range(34,35):
			url = "https://www.qisuu.la/du/5/5203/8508115.html"
			webPage=urllib.request.urlopen(url)
			html = webPage.read()
			buff = BytesIO(html)
			f = gzip.GzipFile(fileobj=buff)
			data = f.read().decode('utf-8')
			data = data.replace('\n','')
			print(data)
			# content=getContent(res)
			# print(content)
	except Exception as e:
		print (e)



if __name__ == "__main__":
	# fo = open("/Users/yangyibo/Desktop/1.txt","a+",encoding="utf-8")
	# haveGzipBook(fo)
	noGzipBook()



