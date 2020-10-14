# PyQT5速成教程-2 Qt Designer介绍与入门



### Qt Designer的介绍

在PyQt中编写UI界面可以直接通过代码来实现，也可以通过Qt Designer来完成。Qt Designer的设计符合MVC的架构，其实现了视图和逻辑的分离，从而实现了开发的便捷。Qt Designer中的操作方式十分灵活，其通过拖拽的方式放置控件可以随时查看控件效果。Qt Designer生成的.ui文件（实质上是XML格式的文件）也可以通过pyuic5工具转换成.py文件。
Qt Designer随PyQt5-tools包一起安装，其安装路径在 “Python安装路径\Lib\site-packages\pyqt5-tools”下。
若要启动Qt Designer可以直接到上述目录下，双击designer.exe打开Qt Designer；或将上述路径加入环境变量，在命令行输入designer打开；或在PyCharm中将其配置为外部工具打开。
下面以PyCharm为例，讲述PyCharm中Qt Designer的配置方法。

#### PyCharm中PyQt5工具配置

打开PyCharm，选择Settings -> Tools -> External Tools，点击左上角的绿色加号。

![img](http://upload-images.jianshu.io/upload_images/1794590-a2e78a35e0bb5c7e.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

Create Tool

Name填入QtDesigner（方便后续使用，名称无所谓）。Program选择我们安装的PyQt5-tools下面的designer.exe。Working directory则选择我们的工作目录。然后点击OK，则添加了QtDesigner作为PyCharm的外置工具。
然后添加PyUIC（UI转换工具），PyUIC的Program为Python.exe，在Python的安装目录下面的Scripts目录下，Working directory同理设为我们的工作目录，Arguments则填入如下代码：

```
-m PyQt5.uic.pyuic  $FileName$ -o $FileNameWithoutExtension$.py

```

最后添加pyrcc用于PyQt5的资源文件转码。具体配置与上述内容相同，Arguments填入：

```
$FileName$ -o $FileNameWithoutExtension$_rc.py

```

退出之前，点击Apply保存配置。配置完成之后，PyCharm中会加入3个工具。

![img](http://upload-images.jianshu.io/upload_images/1794590-362c50ec7d20ee03.png?imageMogr2/auto-orient/strip|imageView2/2/w/543/format/webp)

配置好的工具

点击QtDesigner则打开QtDesigner的界面。

### Qt Designer界面简介

刚打开Qt Designer，则弹出如下图所示的窗口。

![img](http://upload-images.jianshu.io/upload_images/1794590-703b1f9c79b1cb8c.png?imageMogr2/auto-orient/strip|imageView2/2/w/589/format/webp)

模板窗口

创建新的Form给出了5个模板，其中Widget与Main Window最为常用。这里我们选择创建一个Main Window。

![img](http://upload-images.jianshu.io/upload_images/1794590-af201ed93ebb4215.png?imageMogr2/auto-orient/strip|imageView2/2/w/1200/format/webp)

QtDesigner界面

我们拖拽一个Label与Button进入主窗口（Main Window）。

![img](http://upload-images.jianshu.io/upload_images/1794590-6b9a5c77d983bb29.png?imageMogr2/auto-orient/strip|imageView2/2/w/814/format/webp)

主窗口

![img](http://upload-images.jianshu.io/upload_images/1794590-aa03726fe99f2f4c.png?imageMogr2/auto-orient/strip|imageView2/2/w/903/format/webp)

对象查看器

![img](http://upload-images.jianshu.io/upload_images/1794590-13c4bec849c7fa56.png?imageMogr2/auto-orient/strip|imageView2/2/w/902/format/webp)

属性编辑器

| 名称          | 含义       |
| ----------- | -------- |
| objectName  | 控件对象名称   |
| geometry    | 相应宽和高与坐标 |
| sizePolicy  | 控件大小的策略  |
| minimumSize | 最小的宽和高   |
| maximumSize | 最大的宽和高   |
| font        | 字体       |
| cursor      | 光标       |
| ...         | ...      |

PS：将minimumSize和maximumSize设为一样的数值之后，则窗口的大小固定。

最右下角的部分则为Resource Browser（资源浏览器），资源浏览器中可以添加相应地如图片素材，作为Label或Button等控件的背景图片等。

![img](http://upload-images.jianshu.io/upload_images/1794590-6f821f5988c9c9b0.png?imageMogr2/auto-orient/strip|imageView2/2/w/896/format/webp)

资源浏览器

### Qt Designer的UI文件

使用Qt Designer设计保存的文件为.ui格式的文件。
通过保存并使用记事本等软件打开，我们可以看到.ui文件的内容如下：

```
<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>800</width>
    <height>600</height>
   </rect>
  </property>
  <property name="windowTitle">
   <string>MainWindow</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <widget class="QLabel" name="label">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>80</y>
      <width>72</width>
      <height>15</height>
     </rect>
    </property>
    <property name="text">
     <string>TextLabel</string>
    </property>
   </widget>
   <widget class="QPushButton" name="pushButton">
    <property name="geometry">
     <rect>
      <x>240</x>
      <y>120</y>
      <width>93</width>
      <height>28</height>
     </rect>
    </property>
    <property name="text">
     <string>PushButton</string>
    </property>
   </widget>
  </widget>
  <widget class="QMenuBar" name="menubar">
   <property name="geometry">
    <rect>
     <x>0</x>
     <y>0</y>
     <width>800</width>
     <height>26</height>
    </rect>
   </property>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>

```

从.ui文件的第一行我们便能看出，其实质是一个XML文件。ui文件中存放了在主窗口中的一切控件的相关属性。使用XML文件来存储UI文件，具有高可读性和移植性，因此我们可以方便地将.ui文件转换到.py文件，从而使得我们可以使用Python语言在设计的GUI上面编程。

#### 将.ui文件转换为.py文件

将.ui文件转换到.py文件很简单，在前面我们曾设置了pyuic5这个工具。如果你没有在PyCharm中设置这个工具，或者根本没有使用PyCharm，则可以到命令行中使用如下命令实现.ui到.py的转换。

```
pyuic5 - o 目标文件名.py 源文件名.ui

```

或者直接在PyCharm中，找到.ui文件，右键 打开菜单找到External Tools->PyUIC。点击之后，我们在相应工程目录下会产生一个.py文件。（注意，.ui文件必须存放在我们的External Tools中设置的相应项目目录下）

![img](http://upload-images.jianshu.io/upload_images/1794590-d6bdb7969aec8007.png?imageMogr2/auto-orient/strip|imageView2/2/w/613/format/webp)

PyUIC

转换完成之后，打开.py文件。

```
# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.10.1
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(240, 80, 72, 15))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(240, 120, 93, 28))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "TextLabel"))
        self.pushButton.setText(_translate("MainWindow", "PushButton"))

```

观察上述文件，可以看到如果不通过Qt Designer来制作界面的话，我们将会一次次地调试程序，来讲按钮和Label等放在合适的位置，这将是极其痛苦的过程。而通过Qt Designer，我们可以快速地制作UI，并生成Python的代码，从而实现快速地UI的开发。

#### 使用转换的.py文件

然而，此时之间运行这个转换好的Python文件是无法显示任何窗口的。因为这个Python文件只有定义主窗口以及其控件的代码，并没有程序入口的代码。为了秉持视图与逻辑分离的原则，我们再编写一个新的脚本来调用这个文件，并且创建一个窗口。

```
import sys
from PyQt5.QtWidgets import QApplication, QMainWindow
from mainWindow import *


class MyWindow(QMainWindow, Ui_MainWindow):
    def __init__(self, parent=None):
        super(MyWindow, self).__init__(parent)
        self.setupUi(self)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    myWin = MyWindow()
    myWin.show()
    sys.exit(app.exec_())


```

通过上述代码，我们继承了Ui_MainWindow类，使用其构造方法构造主窗口，并定义了程序的入口，通过创建QApplication对象来创建Qt窗口。其运行结果如下：

![img](http://upload-images.jianshu.io/upload_images/1794590-d44875d45ae629ba.png?imageMogr2/auto-orient/strip|imageView2/2/w/802/format/webp)

Qt窗口

通过上述操作，我们熟悉了Qt Designer设计界面，到实现业务逻辑的大致工作流程。通过这个工作流程可以简化工作，实现速度的提升。
通过对视图与业务逻辑的分离，在每次更改Qt Designer的UI设计的时候，也不用重新编写代码，而只需对更改的部分做稍微的修改即可。

在下一讲中，我们将继续讲解Qt Designer的使用。