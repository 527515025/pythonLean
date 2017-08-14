#!/usr/bin/env 
# -*- coding: utf-8 -*-

import support
import Networkerror

support.print_func("Runoob")
support.sum(10,5)

def inputTest():
    str = raw_input("raw_input请输入：");
    print "你输入的内容是: ", str
    str = input("input请输入：");
    print "你输入的内容是: ", str


# try:
#     raise Networkerror("Bad hostname")
# except Networkerror,e:
#     print e.args






