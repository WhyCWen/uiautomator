#!/usr/bin/env python2  
# encoding: utf-8  
"""
-------------------------------------------------
    @version        : v1.0 
    @File Name      : uitest.py  
    @Author         : whyc
    @date           : 17-9-14 上午10:47
    @license        : 
    @contact        : 8720whyc@gmail.com
    @site           : https://github.com/WhyCWen 
    @software       : PyCharm 
    @file           : uitest.py 
-------------------------------------------------
    @Description    : 
  
-------------------------------------------------
    Modifictions    : Change Activity  @Times
    @Description    : 17-9-14 上午10:47
                    :
                    :
-------------------------------------------------

"""
from time import sleep

__author__ = 'whyc'
import uiautomator as uia
from uiautomator import Device

def func():
    d = Device('2d973073')
    if d.screen == 'off':
        print "android sreen is off"
        d.screen.on()
    if d.screen == 'on':
        # d.press("menu")

        # d.press("camera")
        # d.press.home()
        # print d.info
        #d.screenshot("home.png")
        # d(index='2',className='android.widget.FrameLayout').click()
        # d.orientation = 'r'
        # d.orientation = 'u'
        # d.orientation = 'n'
        print "orientation: ",d.orientation
        # d.freeze_rotation(False)
        # d.open.notification()
        # d.open.quick_settings()
        # d.wait.idle()
        # d.wait.update()
        # print d.watchers
        # d.dump('heh.xml')
        # d(className='android.widget.FrameLayout')\
        #     .child(text='天气').right(text='小米钱包').click()

        if d(text='Settings').exists :
            print 'Settings'
            info = d(text='Settings').info
            print info
            with open('bb.log','w+',) as bb:
                bb.write(str(info))
        elif d(text='设置').exists:
            print "设置"
            setting = d(text='设置')
            info = setting.info
            # setting.swipe.right() #滑动屏幕
            d(className='android.widget.FrameLayout').swipe.down(steps=20)
            print info
            with open('bb.log','w+') as bb:
                bb.write(str(info))
        # d.open.notification()
        # d(text='TP-LINK_584E',className='android.widget.TextView').click()
#把要运行的发放放在这里面 式逻辑运行

def run():
    func()


class Main():
    def __init__(self):
        pass


if __name__ == "__main__":

    run()