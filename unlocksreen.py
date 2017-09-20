#!/usr/bin/env python2  
# encoding: utf-8  
"""
-------------------------------------------------
    @version        : v1.0 
    @File Name      : unlocksreen.py  
    @Author         : whyc
    @date           : 17-9-19 下午7:14
    @license        : 
    @contact        : 8720whyc@gmail.com
    @site           : https://github.com/WhyCWen 
    @software       : PyCharm 
    @file           : unlocksreen.py 
-------------------------------------------------
    @Description    : 
  
-------------------------------------------------
    Modifictions    : Change Activity  @Times
    @Description    : 17-9-19 下午7:14
                    :
                    :
-------------------------------------------------

"""
__author__ = 'whyc'
import uiautomator as uia

# 链接指定设备
d = uia.Device('2d973073')
def unlockscreen():
    if d.screen == 'off':
        d.screen.on()
    if d.screen == 'on':
        d(packageName="com.android.keyguard",resourceId="android:id/lock_screen" ).swipe.up(steps=30)
        d(packageName="com.android.keyguard",resourceId="com.android.keyguard:id/lockPattern").swipe.up(steps=30)

        print 'on dump'
        d.dump('lockgesture.xml')
        # d.dump('lock.xml')


#把要运行的发放放在这里面 式逻辑运行
def run():
    unlockscreen()


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":
    run()