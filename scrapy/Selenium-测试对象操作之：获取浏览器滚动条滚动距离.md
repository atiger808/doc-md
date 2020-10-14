# [Selenium-测试对象操作之：获取浏览器滚动条滚动距离](https://www.cnblogs.com/yan-xiang/p/6619062.html)

\#encoding=utf-8
from selenium import webdriver
import time,os

driver = webdriver.Chrome()
\#打开网页
driver.get('https://www.baidu.com/')
driver.maximize_window()
\#网页可视区高
js = "var q=document.body.clientHeight;return(q)"
Visual_area_height=driver.execute_script(js)
print '网页可视区的高:',Visual_area_height
\#网页可视区宽
js = "var q=document.body.clientWidth;return(q)"
Visual_area_width=driver.execute_script(js)
print '网页可视区的宽:',Visual_area_width

\#网页可视区高（包含边线的宽）
js = "var q=document.body.offsetHeight ;return(q)"
Visual_area_height_border=driver.execute_script(js)
print '网页可视区的高(包含边线的宽):',Visual_area_height_border
\#网页可视区宽（包含边线的宽）
js = "var q=document.body.offsetWidth;return(q)"
Visual_area_width_border=driver.execute_script(js)
print '网页可视区的宽(包含边线的宽):',Visual_area_width_border

\#网页正文全文高
js = "var q=document.body.scrollHeight ;return(q)"
Text_height=driver.execute_script(js)
print '网页正文全文宽:',Text_height
\#网页正文全文宽
js = "var q=document.body.scrollWidth;return(q)"
Text_width=driver.execute_script(js)
print '网页正文全文宽:',Text_width

\#屏幕辨别率的高
js = "var q=window.screen.height;return(q)"
Resolution_height=driver.execute_script(js)
print '屏幕辨别率的高:',Resolution_height
\#屏幕辨别率的宽
js = "var q=window.screen.width;;return(q)"
Resolution_width=driver.execute_script(js)
print '屏幕辨别率的高:',Resolution_width

'''
当浏览器滚动条发生变化的时候，下面网页被卷去的高和宽会发生变化

'''
driver.find_element_by_id("kw").send_keys('selenium')
driver.find_element_by_id("su").click()
time.sleep(3)
\# 将页面滚动条拖到底部
js = "var q=document.body.scrollTop=515"
driver.execute_script(js)
time.sleep(3)

\#网页被卷去的高
js = "var q=document.body.scrollTop ;return(q)"
Roll_height=driver.execute_script(js)
print '网页被卷去的高:',Roll_height
\#网页被卷去的左
js = "var q=document.body.scrollLeft;return(q)"
Roll_Left=driver.execute_script(js)
print '网页被卷去的左:',Roll_Left