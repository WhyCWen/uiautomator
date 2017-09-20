#!/usr/bin/env python2  
# encoding: utf-8  
"""
-------------------------------------------------
    @version        : v1.0 
    @File Name      : monkerunnertest.py  
    @Author         : whyc
    @date           : 17-9-14 下午6:13
    @license        : 
    @contact        : 8720whyc@gmail.com
    @site           : https://github.com/WhyCWen 
    @software       : PyCharm 
    @file           : monkerunnertest.py 
-------------------------------------------------
    @Description    : 
  
-------------------------------------------------
    Modifictions    : Change Activity  @Times
    @Description    : 17-9-14 下午6:13
                    :
                    :
-------------------------------------------------

"""
__author__ = 'whyc'

import sys
from com.android.monkeyrunner import MonkeyRunner as mr
from com.android.monkeyrunner import MonkeyDevice as md
from com.android.monkeyrunner import MonkeyImage as mi

# connect device 连接设备
# 第一个参数为等待连接设备时间
# 第二个参数为具体连接的设备
device = mr.waitForConnection()
if not device:
    print >> sys.stderr, "fail"
    sys.exit(1)
# 定义要启动的Activity
componentName = 'com.example.simulate/.ShellActivity'
# 启动特定的Activity
device.startActivity(component=componentName)
mr.sleep(3.0)
# do someting 进行我们的操作
# 输入 helloworld
device.type('helloworld')
# 输入回车
device.press('KEYCODE_ENTER')
# return keyboard
# device.press('KEYCODE_BACK')
# ------
# takeSnapshot截图
mr.sleep(3.0)
result = device.takeSnapshot()

# save to file 保存到文件
result.writeToFile('./shot1.png', 'png');