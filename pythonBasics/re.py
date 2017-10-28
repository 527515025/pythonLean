# -*- coding: utf-8 -*-
#正则表达式
#导入re模块
import re

# 将正则表达式编译成Pattern对象，注意hello前面的r的意思是“原生字符串”
pattern = re.compile(r'.*el.')

#返回pattern对象
# re.compile(string[,flag])  
# #以下为匹配所用函数
# re.match(pattern, string[, flags])
# re.search(pattern, string[, flags])
# re.split(pattern, string[, maxsplit])
# re.findall(pattern, string[, flags])
# re.finditer(pattern, string[, flags])
# re.sub(pattern, repl, string[, count])
# re.subn(pattern, repl, string[, count])

result1 = re.match(pattern,'hellox')

result2 = re.match(pattern,'helxcp')

if result1:
	print(result1.group(0))
	#匹配时使用的文本。
	print(result1.string)
	#匹配时使用的Pattern对象。
	print(result1.re)
	#文本中正则表达式开始搜索的索引
	print(result1.pos)
	#文本中正则表达式结束搜索的索引
	print(result1.endpos)
	#最后一个被捕获的分组在文本中的索引,如果没有被捕获的分组，将为None
	print(result1.lastindex)
	#最后一个被捕获的分组的别名。如果这个分组没有别名或者没有被捕获的分组，将为None。
	print(result1.lastgroup)

else:
	print("result1 匹配失败")


print("------------------------2-----------------------------")

if result2:
	print(result2.group(0))
else:
	print("result2 匹配失败")

print("------------------------3----------------------------")

pattern2 = re.compile(r'\d+')

#search()会扫描整个string查找匹配,match（）只有在0位置匹配成功的话才有返回
result3 = re.search(pattern2,'helx5cphelq2qq3')
if result3:
	print(result3.group(0))


#以列表形式返回全部能匹配的子串
print(re.findall(pattern2,'helx1cphelq2qq3'))
#按照能够匹配的子串将string分割后返回列表。maxsplit用于指定最大分割次数，不指定将全部分割
print(re.split(pattern2,'one1two2three3four4'))
print(re.split(pattern2,'one1two2three3four4',2))


#返回一个顺序访问每一个匹配结果（Match对象）的迭代器
for m in re.finditer(pattern2,'one1two2three3four4'):
	print(m.group())




