# 第九章 Django常见问题

[Django 数据导入和导出（数据库的迁移方法）](https://www.cnblogs.com/yoyo008/p/13203517.html)

### 9.1  数据导出

1 数据导出* python manage.py dumpdata*

*不指定 appname 时默认为导出所有的app*

*python manage.py dumpdata [appname] > appname_data.json指定appnamde 导出 指定app 的数据（比如appname为cmdb）python manage.py dumpdata cmdb>cmdb.json2. 数据导入python manage.py loaddata*

*不需要指定 appnamepython manage.py loaddata blog_dump.json优点：可以兼容各种支持的数据库，也就是说，以前用的是 SQLite3，可以导出后，用这种方法导入到 MySQL, PostgreSQL等数据库，反过来也可以。*

缺点：数据量大的时候，速度相对较慢，表的关系比较复杂的时候可能导入不成功。

个人推荐导入数据做法：

1 将APP的migrations目录下，只保留__init__.py文件，其余文件全部清空；
重置文件
python manage.py migrate --fake cmdb zero # cmdb是app的名称
删除migrations的处init.py的其他文件

2 然后分别执行：python manage.py makemigrations 和 python3 manage.py migrate；

### 9.2  数据导入

3 最后导入数据：python manage.py loaddata blog_dump.json

以上做法，能够增加数据导入的成功率。



### 9.3  解决djang DEBUG = False和True

没有css和js

 DEBUG = False的情况
1、在settings.py添加如下

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')
2、运行下面命令把相关文件copy到static这个目录 

python manage.py collectstatic

3、在项目下的总urls.py（不是app的urls.py）中，urlpatterns下面添加：

from django.contrib import admin
from django.urls import path,include,re_path
from . import views
from django.conf import settings
from django.conf.urls.static import serve,static

urlpatterns = [

```
path('admin/', admin.site.urls),
re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
]
```

DEBUG = True的情况 
配置

STATIC_URL = '/static/'
STATICFILES_DIRS = [

```
os.path.join(BASE_DIR, "static"),
```

]


### 