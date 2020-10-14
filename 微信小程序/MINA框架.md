微信小程序开发

## MINA框架

小程序配置

​	全局配置

​		全局配置保存在app.json文件中。开发者通过使用app.json来配置页面文件(pages)的路径，

​		窗口(window)表现，设定网络超时时间值(networkTimeout)以及配置多个换页(tarBar)

​	项目配置

​	页面配置

​		给每个页面的.json文件进行配置， 但是页面只能配置窗口的表现。 页面的配置比app.json全局配置简单的多，    只是设置app.json中的window配置项的内容， 页面中配置项会覆盖app.json的window中相同的配置

#### tabBar 组件

"position": "top"  如果为top 则图标默认为隐藏，如果为bottom， 图标显示

"list": [{}, {}]  最少两个对象，最多五个对象

#### 4. networkTimeout 配置项

5. debug配置项





## 小程序的逻辑层

生命周期函数

onLaunch  监听小程序初始化

onShow	   监听小程序显示

onHide	 监听页面隐藏

onError

onUnload  监听页面卸载

onPullDownRefresh   监听用户下拉动作

onReachBottom   监听页面上拉触底事件

onShareMessage  用户点击右上角转发

onPageScroll   页面滚动触发事件的处理函数

其他       开发者可以添加任意的函数或数据到object参数中， 在页面的函数中用 this  访问

#### App()注册小程序，程序入口

#### [] 代表数组， {}代表对象

对象(属性， 方法)



### Page()页面入口

微信团队为开发者提供了getCurrentPage() 函数， 用来获取当前页面的实例

小提示： 不要在App()中进行onLaunch操作时调用getCurrentPage(), 此时page还没有生成

##### 1， 初始化数据

初始化数据作为页面的第一次渲染， 对象data将会以JSON的形式有逻辑层传至视图层， 所以其数据必须

是可以转成JSON的格式： 字符串， 数字， 布尔值，对象， 数组。

视图层，可以通过WXML对数据进行绑定

实例代码：

<view> {{text}}</view>

<view>{{array[0].msg}}</view>



Page({	

​	data: {

​		text:  "init data",

​		array: [{msg: "1"}, {msg: "2"}]

​	}

})



#### 2.生命周期函数包括 onLoad, onShow, onReady, onHide, onUnload

##### onLoad: 页面加载

一个页面只会调用一次

参数可以获取 wx.navigateTo 和 wx.redirectTo 及<navigator/> 中的query

##### onShow: 页面显示

每次打开页面都会调用一次

##### onReady: 页面初次渲染完成

一个页面只会调用一次，代表页面已经准备妥当， 可和视图曾进行交互

对界面的设置和 wx.setNavigationBarTitle 请在onReady之后设置， 详见生命周期

##### onHide: 页面隐藏

当navigateTo 或底部tab 切换时调用

##### onUnload: 页面卸载

当redirectTo 或 navigateBack 的时候调用

#### 3.页面相关事件处理函数

##### onPullDownRefresh: 下拉刷新时实行的操作

监听用户下拉刷新事件

需要在app.json的window选项中或页面配置中开启enablePullDownRefresh

当处理完数据刷新后， wx.stopPullDownRefresh可以停止当前页面的下拉刷新

##### onReachBottom: 上拉触底时执行的事件

监听用户上拉触底事件

可以在app.json的window 选项中或页面配置中设置触发距离

##### onReachBottomDistance

在触发距离内滑动期间， 本事件只会被触发一次

##### onPageScroll: 页面滚动

监听用户滑动页面事件

参数为object, 包含以下字段：

字段                类型               说明

scrollTop       Number         页面在垂直方向已滚动的距离(单位px)

##### onShareAppMessage： 用户转发

只有定义了此事件处理函数， 右上角菜单才会显示 “转发”按钮

用户点击转发按钮的时候会调用

此事件需要 return 一个 Object, 用与定义转发内容

自定义转发字段

字段                说明                 默 认值

title                 转发标题          当前小程序名称

path                 转发路径        当前页面path,  必须是以/开头的完整路径

实例代码：

Page({

​	onShareAppMessage: function(){

​		return {

​			title: "自定义转发标题",

​			path: "/page/user?id=123"

​		}

​	}

})

#### 4.事件处理函数

除了初始化数据和生命周期函数，  Page 中还可以定义一些特殊的函数：事件处理函数。 在

渲染层可以在组件中加入事件绑定， 当达到触发事件时，就会执行Page中定义的事件处理寒素

实例代码：

<view bindtap="viewTap"> click me </view>



Page({

​	viewTap: function() {

​		console.log("view tap")

​	}

})

#### 5, Page的原型函数

route (Page.prototype.route): 属于Page方法中的原型对象字段（属性）

setData()(Page.prototype.setData()): 属于Page方法中的原型对象的方法， 用与将数据从逻辑层

发送到视图层（异步）， 同时改变对应的this.data的值（同步）

setData() 参数个格式

字段                           类型                        必填             描述                                最低版本

data                           Object                    是                这次要改变的数据

callback                    Function                 否                回调函数                           1.5.0

参数说明

object  以 key, value  的形式表示将this,data中的key 对应的值改变成 value.

callback  是一个回调函数，   在这次setData对界面渲染完毕后调用

其中key 可以非常灵活， 以数据的路径的形式给出，  如array[2].message,   a, b, c, d, 并且

不需要在中预先定义

小提示：

直接修该this.data 而不调用this.setData 是无法改变页面的状态的， 还会造成数据不一致

单次设置的数据不能超过1024kb,   请尽量避免一次设置过多的数据

实例代码：

<view> {{text}}</view>

<button bindtap="changeText"> change normal data </button>

<view>{{num}}</view>

< button bindtap=“changeNum”> change normal num </button>

<view>{{array[0].text}}</view>

<button bindtap="changeItemInArray"> change Array data </view>

<view>{{object.text}}</view>

<button bindtap="changeItemInObject"> change Object data </button>

<view>{{newField.text}}</view>

<button bindtap="addNewField"> Add new data </button>

Page({	

​	data: {

​		text: "init data",

​		num: 0,

​		array: [{text: "init data"}],

​		object: {

​			text: "init data"

​		}

​	},

​	changeText: function(){

​		this.setData({

​			num: this.data.num

​		})

​	},

​	changeItemInArray: function(){

​		this.setData({

​			"array[0].text": "change data"

​		})		

​	},

​	changeItemObject: function(){

​		this.setData({

​			"object.text": "change data"

​		})

​	},

​	addNewField: function(){

​		this.setData({

​			"newField.text": "new data"

​		})

​	}

})





### 文件的作用域和模块化使用

8。模块化

可以将一些公共的代码抽离成为一个单独的js文件， 作为一个模块。模块只有通过

module.exports 或者exports才能对外暴露接口

需要注意的是：

exports 是module.exports的一个引用， 因此在模块里边随意更改exports的指向

会造成未知的错误。 所以更推荐开发者采用module.exports 来暴露模块接口， 除非

你已经清晰知道这两者的关系

小程序目前不支持直接引用node_modules， 开发者需要使用node_modules时候建议

拷贝出相关的代码到小程序的目录中



### 了解JSON数据格式

概念：JavaScript Object Notation的缩写，中文翻译：Javascript对象表示法

特点：它是Javascript语言提供的一种轻量级的数据交换格式，基于文本， 它的作用非常类似XML

语言， 基于“键值对”

价值：JSON可以把复杂的定义对象的方法转换成简单的字符串形式

使用实例：

实例1： {"Stuname": "李四"}  等价形式->  StuName=李四

实例2： {"StuName": "李四", "ClassName": "VIP-1班", "Age": 26}  数据增大时 这种格式可读性非常好

语法结构总结

1. 基于“key-value”
2. key和value之间用冒号(:)分割
3. JSON语句之间用逗号(,)分割