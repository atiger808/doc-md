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
# url_ = 'http://39.108.169.215/login.aspx/inc/VerifyCode.aspx?id='+str(random.random())+';return true;'
# headers = {
# 'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36',
# 'upgrade-insecure-requests':'1',
# }
# data = {
# '__VIEWSTATE': '/wEPDwUJMjYwODQyMjY5D2QWAgIDD2QWBAIBDw8WAh4EVGV4dAUM5aSp5LiL55S15ZWGZGQCCw8PFgIfAAUV6aqM6K+B56CB5LiN5q2j56Gu77yBZGQYAQUeX19Db250cm9sc1JlcXVpcmVQb3N0QmFja0tleV9fFgEFDEltYWdlQnV0dG9uMQ==',
# '__EVENTVALIDATION': '/wEdAAV4I2FowUAtJXfENOb1VT6RR1LBKX1P1xh290RQyTesRS5q4GKY7RdqUJMI8eaQmlFr9o978j9KrO2dZTQeZUFA6ZACrx5RZnllKSerU+IuKg==',
# 'UserName': 'yusaimei',
# 'UserPassWord': '12346',
# # 'CodeKey': '',
# 'ImageButton1.x': '26',
# 'ImageButton1.y': '13',
# }
# res = requests.post(url_1, headers=headers, data=data, verify=False)
# print(res.text)
# print(res.status_code)
# print(random.random())

from selenium import webdriver
from PIL import Image
import sys
import os
from pytesseract import *
import time
import sys

url_1 = 'https://www.baidu.com/'
tessdata_dir_config = '--tessdata-dir "C:\\Users\\Administrator\\AppData\Local\\Tesseract-OCR\\tessdata"'

driver = webdriver.Chrome('C:\Program Files (x86)\Google\Chrome\chromedriver.exe')

time.sleep(3)
driver.get(url_1)

time.sleep(3)
driver.find_element_by_xpath('//*[@id="kw"]').send_keys("手机")
driver.find_element_by_xpath('//*[@id="su"]').click()

# driver.find_element_by_name('UserName').clear()
# driver.find_element_by_name('UserName').value.send_keys('chengqiaoqiao')
# driver.find_element_by_name('UserPassWord').clear()
# driver.find_element_by_name('UserPassWord').send_keys('123456')
# driver.find_element_by_name('ImageButton1').submit()
# print(size)



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
    frame4 = aa.crop((1015, 400, 1085, 435))
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


    # 开始识别
    text = pytesseract.image_to_string(clean_img, config=tessdata_dir_config, lang='eng')
    text = text.strip()
    print(text)
    text = pytesseract.image_to_string(Image.open('d:/img/code4.png'),  config=tessdata_dir_config, lang='eng')
    print(text)

# recognition(url_1)

# text = pytesseract.image_to_string(Image.open('d:/img/timg.jpg'),  config=tessdata_dir_config, lang='eng')
# if text:
#     print('ok', text)
# else:
#     print('None')

