#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def tellFile(file):
    position = file.tell();
    print ("当前文件位置 : "+ str(position))

def seekFile(file):
    position = fo.seek(0,0);
    print "从开头开始读取: ";
    readFile(file);

def readFile(file):
    print(file.read(100))
    

def writeFile(file):
    file.write("此情永流转，千载永不渝!")
    

def closeFile(file):
    file.close();
	
def renameFile(oldName,newName):
    os.rename(oldName,newName);
    return newName;

import os

try:
    fo = open("testFile.txt","rb+")
    print "文件名: ", fo.name
    print "是否已关闭 : ", fo.closed
    print "访问模式 : ", fo.mode
    print "末尾是否强制加空格 : ", fo.softspace
    tellFile(fo);
    writeFile(fo);
    seekFile(fo);     
except IOError:
    print "Error: 没有找到文件或读取文件失败"
else:
    print "内容写入文件成功"
    closeFile(fo);

print os.getcwd() #显示当前的工作目录
# renameFile("testFile.txt","testFile.log")
os.mkdir("ML")
# os.rmdir('newdir') #删除目录,在删除这个目录之前，它的所有内容应该先被清除。
# os.remove("testFile.txt");






