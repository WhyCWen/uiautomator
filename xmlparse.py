#!/usr/bin/env python2  
# encoding: utf-8  
"""
-------------------------------------------------
    @version        : v1.0 
    @File Name      : xmlparse.py  
    @Author         : whyc
    @date           : 17-9-14 下午9:47
    @license        : 
    @contact        : 8720whyc@gmail.com
    @site           : https://github.com/WhyCWen 
    @software       : PyCharm 
    @file           : xmlparse.py 
-------------------------------------------------
    @Description    : 
  
-------------------------------------------------
    Modifictions    : Change Activity  @Times
    @Description    : 17-9-14 下午9:47
                    :]
                    :
-------------------------------------------------

"""
__author__ = 'whyc'

import  xml.sax

class Hierarchy(xml.sax.ContentHandler):

    def __init__(self):
       pass

bounds="[609,0][780,55]"
import re
ad = re.findall(r"(\d+)",bounds,re.M)
if ad:
    aa = [int(i) for i in ad]
    print aa


# print ad
# al = bounds.replace('][',',').lstrip('[').strip(']').split(',')
#
# print al

import re
line = "Cats are smarter than dogs"
matchObj = re.match( r'(.*) are (.*?) .*', line, re.M|re.I)
if matchObj:
    print "matchObj.group() : ", matchObj.group()
    print "matchObj.group(1) : ", matchObj.group(1)
    print "matchObj.group(2) : ", matchObj.group(2)
else:
    print "No match!!"

def func():
    pass


#把要运行的发放放在这里面 式逻辑运行
def run():
    func()


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    run()