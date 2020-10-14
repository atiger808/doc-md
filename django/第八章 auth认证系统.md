# 第八章 auth认证系统

### 1  session

```
# 写入 session 
rerquest.session['user'] = user

# 读取 session
request.session.get('user')

# 删除 session
request.session.flush()
```
##### 1   写入session

```
rerquest.session['user'] = user
```

##### 2  读取 session

```
request.session.get('user')
```

##### 3  删除 session

```
request.session.flush()
```

### 2  auth

##### 1  引入 auth

```
from django.contrib import auth
from django.contrib.auth.models import User
```

##### 2  auth 操作

```
# 验证成功， 返回user对象，否则返回None
user = auth.authenticate(username=user_val, password=pwd_val)

# 类似session写操作 request.session['user'] = user
auth.login(request, user)

# 类似session 删除， request.session.flush()
auth.logout(request)

# 校验当前用户是否是登陆状态
request.user.is_authenticated 

# 校验密码
old_pwd = '123'
new_pwd = 'qwe'
request.user.check_password(old_pwd)

# 修改密码
request.user.set_password(new_pwd)
```

##### 3  urls

```
from django.urls import path
from . import views

app_name = 'app01'

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login/', views.log_in, name='login'),
    path('logout/', views.log_out, name='logout'),
    path('reg/', views.reg, name='reg'),
]
```

##### 4  forms

###### 引入forms

```
from django import forms
from django.forms import widgets
from django.core import validators
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
```



###### 登陆form

```
# 登陆表单
class LoginForm(forms.Form):
    user = forms.CharField(
        error_messages={
            'required': '不能为空'
        },
        widget=widgets.TextInput()
    )

    pwd = forms.CharField(
        error_messages={
            'required':'不能为空'
        },
        widget=widgets.PasswordInput(attrs={'class':'active'})
    )
```

###### 注册form

```
# 注册表单
class RegisterForm(forms.Form):
    user = forms.CharField(
        max_length=12,
        min_length=4,
        error_messages={
            'required': '不能为空',
            'min_length':'长度最小为4'
        },
        widget=widgets.TextInput()
    )

    pwd = forms.CharField(
        error_messages={
            'required':'不能为空',
        },
        widget=widgets.PasswordInput()
    )

    pwd2 = forms.CharField(
        error_messages={
            'required': '不能为空',
        },
        widget=widgets.PasswordInput()
    )

    def clean_user(self):
        user_val = self.cleaned_data.get('user')
        exists = User.objects.filter(username=user_val).exists()
        print('exists：', exists)
        if exists:
            raise ValidationError('该账户已经注册！')
        if not user_val.isdigit():
            return user_val
        else:
            raise ValidationError('不能全为数字')

    def clean_pwd(self):
        pwd_val = self.cleaned_data.get('pwd')
        if pwd_val.isdigit():
            raise ValidationError('不能为纯数字')
        else:
            return pwd_val

    def clean(self):
        pwd_val = self.cleaned_data.get('pwd')
        pwd_val2 = self.cleaned_data.get('pwd2')
        print('pwd: ', pwd_val)
        print('pwd2: ', pwd_val2)
        if pwd_val == pwd_val2:
            return self.cleaned_data
        else:
            raise  ValidationError('两次输入的密码不一致')
```

###### 修改密码fom

```
# 修改密码表单
class ModifyForm(forms.Form):
    pwd_old = forms.CharField(
        error_messages={
            'required': '不能为空'
        },
        widget = widgets.PasswordInput()
    )
    pwd_new = forms.CharField(
        error_messages={
            'required': '不能为空'
        },
        widget=widgets.PasswordInput()
    )
```





##### 5 views

```
from django.shortcuts import render, redirect, reverse, HttpResponse
from django.contrib import auth
from django.contrib.auth.models import User
from .froms import LoginForm
```



   ###### 主页view

    def index(request):
        print(request.user)
        print(type(request.user))
        return render(request, 'app01/index.html', locals())



   ###### 登陆view

    def log_in(request):
        form = LoginForm()
        if request.method == 'POST':
            form = LoginForm(request.POST)
            if form.is_valid():
                user_val = form.cleaned_data.get('user')
                pwd_val = form.cleaned_data.get('pwd')
                # 验证成功， 返回user对象，否则返回None
                user = auth.authenticate(username=user_val, password=pwd_val)
                if user:
                    # 类似session写操作 session['user'] = user
                    auth.login(request, user)
                    return redirect(reverse('app01:index'))
            else:
                all_error = form.errors.get('__all__')
                return render(request, 'app01/login.html', locals())
        return render(request, 'app01/login.html', locals())



   ###### 注销view

    def log_out(request):
        auth.logout(request)
        return redirect(reverse('app01:login'))



   ###### 注册view

    def reg(request):
        User.objects.create_user(username='qwe123', password='1234')
        return redirect(reverse('app01:login'))



###### 修改密码view

```
# 修改密码
def modify(request):
    form = ModifyForm()
    if request.method == 'POST':
        form = ModifyForm(request.POST)
        if form.is_valid():
            pwd_old = form.cleaned_data.get('pwd_old')
            # 密码校验， 返回一个布尔值（True/False）
            res = request.user.check_password(pwd_old)
            print('old_pwd', pwd_old)
            print(res)
            if res:
                pwd_new = form.cleaned_data.get('pwd_new')
                # 设置新密码
                request.user.set_password(pwd_new)
                # 保存到数据库
                request.user.save()
                # 校验， 并写入cookie,session
                user = auth.authenticate(username=request.user, password=pwd_new)
                auth.login(request, user)
                # 校验当前用户是否是登陆状态
                status = request.user.is_authenticated
                print('user status: ', status)
                return redirect(reverse('app01:index'))
            else:
                error = '密码错误'
                return render(request, 'app01/modify.html', locals())
        else:
            all_error = form.errors.get('__all__')
            render(request, 'app01/modify.html', locals())
    return render(request, 'app01/modify.html', locals())
```




##### 6  templates

###### index.html

   ```
<p>Index页面</p>
<p> hello, {{ user }}</p>

<hr>
{% if request.user.is_authenticated %}
    <a href="{% url 'app01:logout' %}">注销</a>
    <a href="">修改密码</a>
    <p>helllo, {{ request.user.username }}</p>
{% else %}
    <a href="{% url 'app01:login' %}">登陆</a>
    <a href="{% url 'app01:reg' %}">注册</a>
{% endif %}
   ```
######   login.html

   ```
<style>
    span{
        color: red;
        font-size: small;
    }
</style>

<form action="" method="post" novalidate>
    {% csrf_token %}
    <table>
        <tr>
            <td>账户：</td>
            <td>{{ form.user }}</td>
            <td><span>{{ form.errors.user.0 }}</span></td>
        </tr>
        <tr>
            <td>密码：</td>
            <td>{{ form.pwd }}</td>
            <td><span>{{ from.errors.pwd.0 }}</span></td>
        </tr>
        <tr>
            <td></td>
            <td><input type="submit" value="提交"></td>
            <td><span>{{ all_error.0 }}</span></td>
        </tr>
    </table>
</form>
   ```


###### register.html

```
<style>
    span{
        color: red;
        font-size: small;
    }
</style>

<form action="" method="post" novalidate>
    {% csrf_token %}
    <table>
        <tr>
            <td>账户：</td>
            <td>{{ form.user }}</td>
            <td><span>{{ form.errors.user.0 }}</span></td>
        </tr>
        <tr>
            <td>密码：</td>
            <td>{{ form.pwd }}</td>
            <td><span>{{ form.errors.pwd.0 }}</span></td>
        </tr>
        <tr>
            <td>确认密码：</td>
            <td>{{ form.pwd2 }}</td>
            <td><span>{{ form.errors.pwd2.0 }}</span></td>
        </tr>
        <tr>
            <td></td>
            <td><input type="submit" value="提交"></td>
            <td><span>{{ all_error.0 }}</span></td>
        </tr>
    </table>
</form>
```



###### modify.html

```
<p>hello, {{ user }} </p>
<style>
    span {
        color: red;
        font-size: small;
    }
</style>
{% if request.user.is_authenticated %}
    <form action="" method="post" novalidate>
    {% csrf_token %}
    <table>
        <tr>
            <td>旧密码：</td>
            <td>{{ form.pwd_old }}</td>
            <td><span>{{ form.errors.pwd_old.0 }} {{ error }}</span></td>
        </tr>
        <tr>
            <td>新密码：</td>
            <td>{{ form.pwd_new }}</td>
            <td><span>{{ form.errors.pwd_new.0 }}</span></td>
        </tr>
        <tr>
            <td></td>
            <td><input type="submit" value="提交"></td>
            <td><span>{{ all_error.0 }}</span></td>
        </tr>
    </table>
</form>
{% else %}
{% endif %}
    <a href="{% url 'app01:login' %}">登陆</a>
    <a href="{% url 'app01:reg' %}">注册</a>
```

