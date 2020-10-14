# _*_ coding: utf-8 _*_
# @Time     : 2018/11/3 12:17
# @Author   : Ole211
# @Site     : 
# @File     : baidu_OCR.py    
# @Software : PyCharm

from aip import AipOcr
import os
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
    return client.basicAccurate(img)['words_result'][4]['words']

""" 调用通用文字识别， 图片参数为本地图片"""
result = get_file_content('code1.png')
print(result)

"""如果有可选参数"""
options = {}
options['language_type'] = "CHN_ENG"
options["detect_direction"] = "true"
options["probability"] = "true"

# print(client.basicGeneral(img))