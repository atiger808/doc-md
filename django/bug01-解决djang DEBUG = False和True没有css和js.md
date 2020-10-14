### 解决djang DEBUG = False和True没有css和js



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
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    ]
DEBUG = True的情况 
配置

STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, "static"),
]
————————————————
版权声明：本文为CSDN博主「a599174211」的原创文章，遵循CC 4.0 BY-SA版权协议，转载请附上原文出处链接及本声明。
原文链接：https://blog.csdn.net/a599174211/article/details/82709634