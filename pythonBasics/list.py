#!/usr/bin/env python3
# -*- coding: utf-8 -*-

list=['abel',234,'bo','hui','yi','xiao']
print(len(list)) #取出list的长度
print(list[0])  #取出第一个元素
print(list[1:3]) #取出第二和第三个元素 (包头不包尾)
print(list[-1]) #取出倒数第一个元素
print(list[-2:]) ##取出倒数第二个元素
print(list[-3:-1])##取出倒数第第三和第二个元素 (包头不包尾)
# print(list(4))  #数组越界

#元祖
print('---------------------tuple---------------------------')
tuple=(123,'yang','bo',1098,34,'an')
print(tuple[3:])
print(tuple[-2])

# tuple[2]='an'
#字典,类似map
print('------------------dictionary---------------------')
an = {}
an['one'] = "This is one"
an[2] = "This is two"

tinydict = {'name': 'john','code':6734, 'dept': 'sales'}
 
print an['one']          # 输出键为'one' 的值
print an[2]              # 输出键为 2 的值
print tinydict             # 输出完整的字典
print tinydict.keys()      # 输出所有键 按照a－z 顺序
print tinydict.values()    # 输出所有值
