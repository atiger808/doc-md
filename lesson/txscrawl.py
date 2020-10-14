# _*_ coding: utf-8 _*_
# @Time     : 2018/11/2 22:15
# @Author   : Ole211
# @Site     : 
# @File     : txscrawl.py    
# @Software : PyCharm


import requests
import random



url = 'http://39.108.169.215/main.aspx'
url_1 = 'http://39.108.169.215/login.aspx'

from selenium import webdriver
from PIL import Image
import sys
import os
from pytesseract import *
import time
from aip import AipOcr
import os
url_1 = 'http://39.108.169.215/login.aspx'


os.chdir('d:/img/')
APP_ID = '14661593'
API_KEY = 'a1oiSUfK3pmnUkay7zP5cbIy'
SECRET_KEY = 'yp6ogvjeZkoYBqLiB5UkWAyEpKKcgBdI'

client = AipOcr(APP_ID, API_KEY, SECRET_KEY)

def get_file_content(filePath):
    """
    读取图片
    :param filePath:
    :return:
    """
    with open(filePath, 'rb') as fp:
        img = fp.read()
    return client.basicAccurate(img)

def auto_login():
    while True:
        driver.save_screenshot('code.png')
        print('保存整个网页截图成功')
        vcode = get_file_content('code.png')
        driver.find_element_by_id("UserName").clear()
        driver.find_element_by_id("UserName").send_keys("linyi")
        driver.find_element_by_id("UserPassWord").clear()
        driver.find_element_by_id("UserPassWord").send_keys("123456")
        driver.find_element_by_id("CodeKey").clear()
        driver.find_element_by_id("CodeKey").send_keys(vcode['words_result'][4]['words'])
        driver.find_element_by_id("ImageButton1").click()
        print(vcode['words_result'])
        print(vcode['words_result'][4]['words'])
        driver.save_screenshot('code1.png')
        vcode = get_file_content('code1.png')
        if len(vcode['words_result']) < 10:
            # driver.close()
            continue
        else:
            print('登录成功')
            print(vcode)
            break

def login():
    import requests
    from bs4 import BeautifulSoup as bs
    url_1 = 'http://39.108.169.215/login.aspx'
    headers = {
    'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
    'upgrade-insecure-requests':'1',
    }
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
    time.sleep(3)
    # 将浏览器最大化, 下面两种方法
    driver.maximize_window()
    driver.get(url_1)
    driver.save_screenshot('code.png')
    print('保存整个网页截图成功')
    vcode = get_file_content('code.png')['words_result'][4]['words']
    data = {
    '__VIEWSTATE': '/wEPDwUJMjYwODQyMjY5D2QWAgIDD2QWBAIBDw8WAh4EVGV4dAUM5aSp5LiL55S15ZWGZGQCCw8PFgIfAAUV6aqM6K+B56CB5LiN5q2j56Gu77yBZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFDEltYWdlQnV0dG9uMQ==',
    '__EVENTVALIDATION': '/wEdAAV4I2FowUAtJXfENOb1VT6RR1LBKX1P1xh290RQyTesRS5q4GKY7RdqUJMI8eaQmlFr9o978j9KrO2dZTQeZUFA6ZACrx5RZnllKSerU+IuKg==',
    'UserName': 'linyi',
    'UserPassWord': '12346',
    'CodeKey': vcode,
    'ImageButton1.x': '26',
    'ImageButton1.y': '13',
    }
    res = requests.post(url_1, headers=headers, data=data, verify=False)
    soup = bs(res.text, 'html.parser')


'''
{'log_id': 6952381645572463043, 'words_result_num': 44, 'words_result': [{'words': '天下电商'}, {'words': '欢迎临沂分站登陆系统,您的角色管理员,权限组:管理组我的信息免责声明退出系统'}, {'words': '任务分配管理系统'}, {'words': '《后台首页'}, {'words': '任务管理'}, {'words': '特别声明本软件为Web版的业务管理软件,购买与使用本软件所管的业务由软件购买者自己负责,因管理业务关系所产生的一切法律影响与软件作者无关。'}, {'words': '任务信息发布'}, {'words': '欢迎登入系统'}, {'words': '自任务信息管理'}, {'words': '今天是:2018年11月03日欢迎 linyi进入系统,以下为系统相关数据简要统计。'}, {'words': '自任务接单管理'}, {'words': '接单完成评价查询'}, {'words': '接单信息统计'}, {'words': '目接单快递管理'}, {'words': '今日接单总数:1820'}, {'words': '今日已完成单数:1787'}, {'words': '自邮寄地址配对'}, {'words': '今日未完成单数:35'}, {'words': '今日已退单数:0'}, {'words': '接单统计(按客户)'}, {'words': '系统总单数:447907'}, {'words': '系统总完成单数:447861'}, {'words': '接单统计(按接单员)'}, {'words': '系统总未完成单数:35'}, {'words': '系统总退单单数:11'}, {'words': '接单统计(按小号)'}, {'words': '系统总客户数:871'}, {'words': '系统总任务数:106881'}, {'words': '小号信息导入'}, {'words': '小号信息管理'}, {'words': '系统小号总数:200000'}, {'words': '系统总商品数:9904'}, {'words': '快递运单导入'}, {'words': '任务单数信息统计(未发布不统计)'}, {'words': '自快递运单库管理'}, {'words': '任务总单数:448268'}, {'words': '任务已接单数:447778'}, {'words': '自文本工具'}, {'words': '任务可接单数:318'}, {'words': '自号码提取管理'}, {'words': '客户管理'}, {'words': '米财务与统计'}, {'words': '米系统配置'}, {'words': '天下电商欢迎临沂分站登陆系统,您共登入系统237次,本次登陆的IP地址183.158.4.149登入时间:2018/11/313:27:02'}]}
{'log_id': 8865904497096325859, 'words_result_num': 8, 'words_result': [{'words': '天下电商'}, {'words': '用户名:linyi'}, {'words': '密码'}, {'words': '验证码:'}, {'words': '登录'}, {'words': '验证'}, {'words': '证码不正确!'}, {'words': '为了取得最佳使用效果,建议使用IE8.0或以上版本使用本系统'}]}

'''

def recognition(pageurl):
    driver = webdriver.Chrome('C:\\Program Files (x86)\\Google\\Chrome\\Application\\chromedriver.exe')
    # 将浏览器最大化, 下面两种方法
    driver.maximize_window()
    # driver.set_window_size(1920, 1080, driver.window_handles[0])
    # 打开目标网页
    driver.get(pageurl)
    #定位验证码
    imgelement = driver.find_element_by_xpath('//*[@id="valiCode"]')
    #获取验证码的x, y坐标轴
    location = imgelement.location
    print('验证码的x, y 坐标{}'.format(location))
    # 获取验证码的长宽
    size = imgelement.size
    print('验证码的长宽:{}'.format(size))
    # 获取我们需要截取的位置坐标
    rangle = (int(location['x']), int(location['y']), int(location['x'] + size['width']), int(location['y'] + size['height']))
    print(rangle)
    name1 = 'd:/img/code1.png'
    # driver.find_element_by_xpath('//*[@id="form1"]/table/tbody/tr/td/table/tbody/tr[4]/td/table/tbody/tr/td[2]/table/tbody/tr[4]/td[3]/table/tbody/tr/td[2]/a')
    # 截取当前网页
    driver.save_screenshot(name1)
    print('保存整个网页截图成功')
    # 打开网页截图
    aa = Image.open(name1)
    # 使用Image的crop函数， 从截图中再次截取我能需要的区域
    frame4 = aa.crop((1015, 400, 1085, 435)).rotate(-10, expand=True)
    frame4.save('d:/img/code2.png')
    print('第二次保存验证码截图成功')
    #打开验证码截图
    img = Image.open('d:/img/code2.png')
    # 转换到灰度图
    imgry = img.convert('L')
    # 保存为灰度图
    imgry.save('d:/img/code3.png')
    print('第三次,保存灰度图成功')
    # 图片二值化， 采用阈值分割法
    clean_img = imgry.point(lambda x: 0 if x <143 else 255)
    clean_img.save('d:/img/code4.png')
    print('第四次保存， 二值化保存成功')
    im = Image.open('d:/img/code4.png')
    w, h = im.size
    print(w, h)

    tessdata_dir_config = '--tessdata-dir "C:\\Users\\Administrator\\AppData\Local\\Tesseract-OCR\\tessdata"'
    # 开始识别
    text = pytesseract.image_to_string(clean_img, config=tessdata_dir_config, lang='eng')
    text = text.strip()
    print(text)
    text = pytesseract.image_to_string(Image.open('d:/img/code2.png'),  config=tessdata_dir_config, lang='eng')
    print(text)

if __name__ == '__main__':
    driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')
    time.sleep(3)
    # 将浏览器最大化, 下面两种方法
    driver.maximize_window()
    driver.get(url_1)
    auto_login()

