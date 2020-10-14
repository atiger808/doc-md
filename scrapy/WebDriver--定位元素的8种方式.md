# [WebDriver--定位元素的8种方式](https://www.cnblogs.com/minieye/p/5803640.html)

在UI层面的自动化测试开发中，元素的定位与操作是基础，也是经常遇到的困难所在。webdriver提供了8种定位：

\1. id定位：find_element_by_id("id值")；id属性是唯一的

```
1 driver.find_element_by_id("loginName").clear()#用户名输入框的id属性
2 driver.find_element_by_id("loginName").send_keys("admin")
3 driver.find_element_by_id("pwdTip").send_keys(Keys.TAB)#密码输入框的id属性
4 driver.find_element_by_id("pwdTip").send_keys("111111")
```

\2. name定位：元素的名称，find_element_by_name("name值")；name属性值在当前页面可以不唯一

```
1 driver.find_elements_by_name("PeriodName")[1].click()#选择学段：初中
2 driver.find_elements_by_name("SubjectName")[0].click()#选择学科：语文

```

  find_elements_by_name("PeriodName")是因为当前页面有一组radiobutton的name值是PeriodName，所以可以用定位一组元素的方法findElements，定位出来的是结果一个list

\3. class定位：元素的类名，find_element_by_class_name("class值")

```
driver.find_elements_by_class_name("u-btn-levred")[0].click()#选择年级：七年级
```

\4. tag定位：页面html文档下的各种标签，find_element_by_tag_name("input")；

tag往往用来定义一类功能，所以通过tag识别某个元素的概率很低。任意打开一个页面，都会发现大量的<div>、<input>、<a>等tag，所以tag name定位很少用

\5. link定位：专门用来定位文本链接，find_element_by_link_name("text")；

```
driver.find_element_by_link_text(u"退出").click()#页面右上方的一些个人操作，比如退出、个人中心、消息通知等
```

\6. partial link定位：是对link定位的一种补充，当链接上的文本内容比较长的时候，可以取文本的一部分进行定位，当然这部分可以唯一地标识这个链接

※注：以上的方式稍有局限，且经常页面没有id，name这些属性值，class name重复性较高，link定位有针对性，所以Xpath与Css定位更灵活些。

\7. XPath定位：find_element_by_xpath("")；有多种定位策略，用FirePath插件自动生成的涵盖以下几种方式

  1）绝对路径定位：对于没有id，name、classname不好定位的，这也是我最常用的，因为可以通过Firefox的FirePath插件可以方便的获取到xpath值

  2）利用元素属性定位：

　　find_element_by_xpath(".//*[@id='Title']")，这里是用的id，也可以用元素其他能够唯一标识的属性，不局限于id、name、class这些；*代表的是标签名，不指定时就可以用*代替

  3）层级与属性结合：下图中就是这种

  4）使用逻辑运算符

```
1 driver.find_element_by_xpath(".//*[@id='divword']/input[7]").click()#登录
2 driver.find_element_by_xpath("html/body/div[4]/div/div[2]/div/div[3]/a[1]").click()#个人页面的发布课程操作
```

\8. CSS定位（薄弱，用的很少，但很强大，比xpath简洁灵活）：使用选择器来为页面元素绑定属性，可以灵活地选择控件的任意属性；find_element_by_css_selector("")；同样也可以用FirePATH生成css哟！

  1）通过class属性定位：点号（"."）表示通过class属性定位

```
1 <input class="u-btn mart5" type="submit" onclick="return User.check()" value="登录">
2 driver.find_element_by_css_selector(".u-btn.mart5").click()
```

  2）通过id属性定位：（"#"）表示通过id定位元素

```
driver.find_element_by_css_selector("#loginName")
```

  3）通过其他属性定位：（"[]"），中括号里的属性可以唯一标识这个元素就可以；属性的值可以加引号，也可以不加

```
1 <input class="u-btn mart5" type="submit" onclick="return User.check()" value="登录">
2 driver.find_element_by_css_selector("[type=submit]").click()
```

  4）组合定位

 

平时使用生成的xpath，id，name，classname这些比较多，今天根据最近这段时间的实践，并参照书上整理了下，发现原来XPath和Css下还有这么多方式，顺便拿最近一些代码试验了下，有些简单的css定位能够成功，有的Firepath生成的并不可用，一些组合定位还需要再研究，是有些难度的。最后记录一种定位方式，更接近底层实现方式的定位，But书上说webdriver更推荐前面那些写法，为毛捏？

\9. 用By定位元素

　　除find_element_by_***这种方式，还有另一套写法，也就是统一调用find_element()方法，两个参数，第一个参数是定位的类型，由By提供；第二个参数是定位的具体值

[![复制代码](https://common.cnblogs.com/images/copycode.gif)](javascript:void(0);)

```
from selenium.webdriver.common.by import By     #使用By这种定位前要将By类导入

find_element(By.ID,"loginName")
find_element(By.NAME,"SubjectName")
find_element(By.CLASS_NAME,"u-btn-levred")
find_element(By.TAG_NAME,"input")
find_element(By.LINK_TEXT,"退出")
find_element(By.PARTIAL_LINK_TEXT,"退")
find_element(By.XPATH,".//*[@id='Title")
find_element(By.CSS_SELECTOR,"[type=submit]")
```