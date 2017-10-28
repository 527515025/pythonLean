#encoding:UTF-8 python2.7 爬虫糗事百科
import urllib
import urllib2
import re

page=1
url = 'https://www.qiushibaike.com/hot/page/'+str(page) 
user_agent= 'Mozilla/4.0 (compatible; MSIE 5.5; Windows NT)'
headers = { 'User-Agent' : user_agent }

try:
	request = urllib2.Request(url,headers=headers)
	response= urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	#(.*?)代表一个分组，在这个正则表达式中我们匹配了五个分组 item[0] 就代表第一个(.*?)所指代的内容
	# pattern = re.compile('<div.*?class="author.*?>.*?<a.*?</a>.*?<a.*?>(.*?)</a>.*?<div.*?class'+'="content".*?title="(.*?)">(.*?)</div>(.*?)<div class="stats.*?class="number">(.*?)</i>',re.S)
	# items = re.findall(pattern,content)
	# for item in items:
	# 	print item[0],item[1],item[2],item[3],item[4]
	pattern = re.compile('<div class="content">\n*<span>\n*(.*?)\n*</span>',re.S)
	for m in re.finditer(pattern,content):
		print "------------------------------------ 分割线 ------------------------------------"
		print m.group(1).replace("<br/>","")
except urllib2.URLError, e:
	#hasattr(object, name) 判断一个对象里面是否有name属性或者name方法，返回BOOL值  
	#getattr(object, name[,default])获取对象object的属性或者方法
	#setattr(object, name, values) 给对象的属性赋值，若属性不存在，先创建再赋值
	if hasattr(e,'code'):
		print e.code
	if hasattr(e, 'reason'):
		print e.reason



