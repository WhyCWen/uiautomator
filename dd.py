#!/usr/bin/env python2  
# encoding: utf-8  
"""
-------------------------------------------------
    @version        : v1.0 
    @File Name      : dd.py  
    @Author         : whyc
    @date           : 17-9-14 上午11:40
    @license        : 
    @contact        : 8720whyc@gmail.com
    @site           : https://github.com/WhyCWen 
    @software       : PyCharm 
    @file           : dd.py 
-------------------------------------------------
    @Description    : 
  
-------------------------------------------------
    Modifictions    : Change Activity  @Times
    @Description    : 17-9-14 上午11:40
                    :
                    :
-------------------------------------------------

"""
__author__ = 'whyc'


from uiautomator import device as d
import time
import sys
import random
import unittest
reload(sys)

class My_Test_Suite(unittest.TestCase):
    def setUp(self):
        try:
            d.press.home()
            d(text="***").click()
            time.sleep(2)
            if d(text="我的").exists:
                d(text="我的").click()
                d(text="注销").click()
                d(text="确定").click()
            if d(text="登录").exists:
                d(resourceId="com.isentech.attendance:id/title_back").click()
            else:
                time.sleep(3)
            print u"开启APP"
        except Exception, e:
            print u"Error: 开启APP失败\n", e

    # 测试注册
    def test_reg(self):
        try:
            d(text="注册").click()
            # 测试已注册手机号
            d(text="请输入手机号码").set_text("1313384****")
            d(text="获取验证码").click()
            # 测试注册
            d(text="请输入手机号码").set_text(phone_number)
            d(text="请输入验证码").set_text("8888")
            d(resourceId="com.isentech.attendance:id/regis_pass").set_text("123456")
            d(resourceId="com.isentech.attendance:id/regis_passAgain").set_text("123456")
            d(text="注册").click()
            time.sleep(2)
            if d(text="立刻去登录").exists:
                d(text="立刻去登录").click()
            d(resourceId="com.isentech.attendance:id/txtLoginPassword").set_text("123456")
            d(text="登录").click()
        except Exception, e:
            print u"Error: 注册失败\n", e

    # 测试登陆
    def test_login(self, phone):
        try:
            d(text="登录").click()
            d(resourceId="com.isentech.attendance:id/txtLoginUserName").clear_text()
            d(resourceId="com.isentech.attendance:id/txtLoginUserName").set_text(phone)
            d(resourceId="com.isentech.attendance:id/txtLoginPassword").set_text("123456")
            d(text="登录").click()
            d(text="请输入您的姓名").set_text("123456")
            d(text="完成").click()
            time.sleep(2)
            if d(text="签到").exists:
                print u"登录成功"
        except Exception, e:
            print u"Error: 登录失败\n", e

    # 测试忘记密码
    def test_forget_password(self):
        try:
            pass   # 一些测试步骤
        except Exception, e:
            print u"Error: 重置密码or修改密码失败\n", e

    #......更多的测试模块用例

    def tearDown(self):
        try:
            d.press.home()
            d.press.recent()
            time.sleep(3)
            d.swipe(200, 500, 200, 0, steps=10)
            d.press.home()
            print (u"关闭APP")
        except Exception , e:
            print u"Error: 关闭APP失败\n", e

if __name__ == "__main__":
    phone_number = random.choice(['139', '188', '185', '136', '158', '151'])+"".join(random.choice("0123456789") for i in range(8))
    test_unit = unittest.TestSuite()
    test_unit.addTest(My_Test_Suite("test_reg"))
    filename = './Result_auto_android.html'
    fp = file(filename, 'wb')
    runner = HTMLTestRunner.HTMLTestRunner(stream=fp,title=u"测试报告",description=u"测试结果详情：")
    runner.run(test_unit)