# 第六章  [AJAX提交数据](https://www.cnblogs.com/maple-shaw/articles/9334882.html)



## 6.1 ajax登录示例

urls.py

```
from django.conf.urls import url
from django.contrib import admin
from app01 import views
 
urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^login_ajax/$', views.login_ajax, name='login_ajax'),
    url(r'^index/$', views.index, name='index'),
]
```

views.py

```
from django.shortcuts import render, HttpResponse, redirect
import json
 
 
def index(request):
    return HttpResponse('this is index')
 
 
def login_ajax(request):
    if request.method == "POST":
        user = request.POST.get("user")
        pwd = request.POST.get("pwd")
        ret = {"status": 0, 'url': ''}
        if user == "alex" and pwd == "123":
            ret['status'] = 1
            ret['url'] = '/index/'
        return HttpResponse(json.dumps(ret))
 
    return render(request, "login_ajax.html")
```

login_ajax.html

```
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="x-ua-compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>登录</title>
    <link rel="stylesheet" href="/static/plugins/bootstrap-3.3.7-dist/css/bootstrap.css">
    <link rel="stylesheet" href="/static/css/signin.css">
</head>
<body>
 
<div class="container">
 
    <form class="form-signin" action="{% url 'login' %}" method="post">
        {% csrf_token %}
        <h2 class="form-signin-heading">请登录</h2>
        <label for="inputUser" class="sr-only">用户名</label>
        <input type="text" id="inputUser" class="form-control" placeholder="用户名" required="" autofocus="" name="user">
        <label for="inputPassword" class="sr-only">密码</label>
        <input type="password" id="inputPassword" class="form-control" placeholder="密码" required="" name="pwd">
        <div class="checkbox">
            <label>
                <input type="checkbox" value="remember-me"> 记住我
            </label>
        </div>
        <input class="btn btn-lg btn-primary btn-block" id="login" value="登陆">
    </form>
 
</div> <!-- /container -->
 
 
<script src="/static/jquery-3.3.1.min.js"></script>
<script>
 
    $('#login').click(function () {
        $.ajax({
            url: '/login_ajax/',
            type: 'post',
            data: {
                csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
                user: $('[name="user"]').val(),
                pwd: $('[name="pwd"]').val()
            },
            success: function (data) {
                data = JSON.parse(data);
                if (data.status) {
                    window.location = data.url
                }
                else {
                    alert('登陆失败')
                }
            }
        })
    })
</script>
 
</body>
</html>
```

静态文件需要配置，使用了jQuery和Bootstrap。



## 6.2  CSRF跨站请求伪造

### 方式一

将

```
csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val()
```

 放在POST的请求体中。

示例中就是使用的这种方式。

### 方式二

给ajax的请增加X-CSRFToken的请求头，对应的值只能是cookie中的csrftoken的值。

所以我们要从cookie中提取csrftoken的值，jQuery不能去cookie，我们使用jquery.cookie的插件。[点击下载jquer.cookie插件](http://github.com/carhartl/jquery-cookie/zipball/v1.4.0)。

HTML中导入jquery.cookie.js。

```
<script src="/static/jquery-3.3.1.min.js"></script>
<script src="/static/jquery.cookie.js"></script>
<script>
 
    $('#login').click(function () {
        $.ajax({
            url: '/login_ajax/',
            type: 'post',
            headers:{ "X-CSRFToken":$.cookie('csrftoken') },
            data: {
                user: $('[name="user"]').val(),
                pwd: $('[name="pwd"]').val()
            },
            success: function (data) {
                data = JSON.parse(data);
                if (data.status) {
                    window.location = data.url
                }
                else {
                    alert('登陆失败')
                }
            }
        })
    })
</script>
```

### 方式三

使用$.ajaxSetup()给全局的ajax添加默认参数。

可以按照方式一设置data，也可以按照方式二设置请求头。

```
$.ajaxSetup({
    data: {
        csrfmiddlewaretoken: $("[name='csrfmiddlewaretoken']").val(),
    }
});

$.ajaxSetup({
    headers: {"X-CSRFToken": $.cookie('csrftoken')},
});
```

### 方式四

官方推荐方法（用到jquery.cookie插件）：

```
function csrfSafeMethod(method) {
    // these HTTP methods do not require CSRF protection
    return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
}
 
$.ajaxSetup({
    beforeSend: function (xhr, settings) {
        if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
            xhr.setRequestHeader("X-CSRFToken", $.cookie('csrftoken'));
        }
    }
});
```