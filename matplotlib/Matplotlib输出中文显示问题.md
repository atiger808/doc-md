# Matplotlib输出中文显示问题

## 解决办法

### 方法一：修改配置文件matplotlibrc

在matplotlib的安装路径：Python36\site-packages\matplotlib\mpl-data\matplotlibrc，文件中有如下内容：

```
#font.family    : sans-serif
#font.sans-serif   : Bitstream Vera Sans, Lucida Grande, Verdana, Geneva, Lucid, Anal, Helvetica, Avant Ga12
```

### 方法二：动态设置参数（推荐方式）

在python脚本中动态设置matplotlibrc，这样就避免了更改配置文件的麻烦，方便灵活，例如:

from pylab import mpl 
mpl.rcParams[‘font.sans-serif] = [‘SimHei’]

由于更改了字体导致显示不出负号，将配署文件中axes.unicode minus : True修改为Falsest就可以了，当然这而可以用代码来完成。

```
from pylab import mpl

mpl.rcParams['font.sans-serif'] = ['FangSong'] # 指定默认字体
mpl.rcParams['axes.unicode_minus'] = False # 解决保存图像是负号'-'显示为方块的问题1234
```

### 方法三：使用字体管理器

python有个字体管理器，font_manager

```
myfont = matplotlib.font_manager.FontProperties(fname='C:/Windows/Fonts/msyh.ttf')  
mpl.rcParams['axes.unicode_minus'] = False  12
```

[下文出处：](http://www.360doc.com/content/14/0713/12/16740871_394080556.shtml)[http://www.360doc.com/content/14/0713/12/16740871_394080556.shtml](http://www.360doc.com/content/14/0713/12/16740871_394080556.shtml) 
这是别人整理的Windows的字体对应名称，根据需要自行更换！

| 黑体        | SimHei             |
| --------- | ------------------ |
| 微软雅黑      | Microsoft YaHei    |
| 微软正黑体     | Microsoft JhengHei |
| 新宋体       | NSimSun            |
| 新细明体      | PMingLiU           |
| 细明体       | MingLiU            |
| 标楷体       | DFKai-SB           |
| 仿宋        | FangSong           |
| 楷体        | KaiTi              |
| 仿宋_GB2312 | FangSong_GB2312    |
| 楷体_GB2312 | KaiTi_GB2312       |

宋体：SimSuncss中中文字体（font-family）的英文名称

Mac OS的一些：

华文细黑：STHeiti Light [STXihei]

华文黑体：STHeiti

华文楷体：STKaiti

华文宋体：STSong

华文仿宋：STFangsong

儷黑 Pro：LiHei Pro Medium

儷宋 Pro：LiSong Pro Light

標楷體：BiauKai

蘋果儷中黑：Apple LiGothic Medium

蘋果儷細宋：Apple LiSung Light

Windows的一些：

新細明體：PMingLiU

細明體：MingLiU

標楷體：DFKai-SB

黑体：SimHei

新宋体：NSimSun

仿宋：FangSong

楷体：KaiTi

仿宋_GB2312：FangSong_GB2312

楷体_GB2312：KaiTi_GB2312

微軟正黑體：Microsoft JhengHei

微软雅黑体：Microsoft YaHei

装Office会生出来的一些：

隶书：LiSu

幼圆：YouYuan

华文细黑：STXihei

华文楷体：STKaiti

华文宋体：STSong

华文中宋：STZhongsong

华文仿宋：STFangsong

方正舒体：FZShuTi

方正姚体：FZYaoti

华文彩云：STCaiyun

华文琥珀：STHupo

华文隶书：STLiti

华文行楷：STXingkai

华文新魏：STXinwei