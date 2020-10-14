# 第七章 django 验证码功能

### 7.1 生成验证码

```
from random import randint, choice
from PIL import Image, ImageDraw, ImageFont
#from cStringIO import StringIO  #python2的用法
from io import StringIO, BytesIO #python3 的用法

from string import printable

def create_captcha():
    font_path = 'static/font/FreeSans.ttf'
    font_color = (randint(150,200), randint(0,150), randint(0,150))
    line_color = (randint(0,150), randint(0,150), randint(150,200))
    point_color = (randint(0, 150), randint(50, 150), randint(150, 200))
    width, height = 100, 40
    image = Image.new('RGB', (width, height), (200, 200, 200))
    font = ImageFont.truetype(font_path, height-10)
    draw = ImageDraw.Draw(image)
    #生成验证码
    #print (printable)
    text =''.join([choice(printable[:62]) for i in range(4)])
    font_width, font_height = font.getsize(text)
    #把验证码写到画布上
    draw.text((10,10), text, font=font, fill=font_color)
    #绘制线条
    for i in range(0, 5):
        draw.line(((randint(0, width), randint(0, height)),
                   (randint(0, width), randint(0, height))),
                  fill=line_color, width=2)
    #绘制点
    for i in range(randint(100, 1000)):
        draw.point((randint(0, width), randint(0, height)), fill=point_color)
    #输出
    out = BytesIO()
    #验证码路径(自己临时设置的)
    code_path = '/home/pi/django-project/femdom/article/static/image/captcha.png'
    image.save(out, format='jpeg')
    image.save(code_path, format='jpeg')
    content = out.getvalue()
    #print(content)
    out.close()
    return text, content
```

### 7.2  views  返回验证码图片，

并把验证码值传给session， 并设置session 过期时间为60秒

```
def captcha(request):
    text, content = create_captcha()
    request.session['verCode'] = text.lower()
    request.session.set_expiry(60)
    return HttpResponse(content, content_type='image/png')
```

### 7.3  views 登录后，

将前端输入的验证码和后台session设置的验证码进行比较

```

def dologin(request):
    value=request.GET.get("codevalue")
    value2=request.session.get("verCode")
 
 
    if value==value2:
 
        return HttpResponse("success!!")
 
    else:
        return HttpResponse("error!!")
```



### 7.4  django 点击刷新验证码 

与 验证码提交

#### 方法一：

    <div class="col-sm-4 has-success">
                        <img src="/blog/get_captcha/" title="点击更新验证码" id="captcha" onclick="refresh_captcha(this)">
                    </div>


    function refresh_captcha(obj) {
        obj.src = '/blog/get_captcha/?temp='+Math.random()或(new Date()).gettime()
    }

#### 方法二：

```
<div class="input-group-bottom-right">
	<img  style="width: 100px;" id="Captcha_Img" onclick="Refresh_Captcha()"
		src="//hsajax.app/?t=captcha&amp;r=643131">
	<button id="btn" onclick="POST_Data(1);">提交反馈</button>
</div>

function Refresh_Captcha() {
        // $('#Captcha_Img').attr('src', CFG_Url_Ajax + '?t=captcha&r=' + Get_Random(999999));
        $('#Captcha_Img').attr('src', "{% url 'article:captcha' %}"+'?stamp='+Math.random());
        $('#Captcha').val('');
    }

function POST_Data(Type) {
        if (Type == 1) {
            if ($('#Captcha').val() == '') {
                Show_Prompt_Box(3, '请您输入右侧图片中的验证码.');
            } else if ($('#Content').val() == '') {
                Show_Prompt_Box(3, '请您输入需要反馈的内容,感谢您的支持.');
            } else if ($('#Contact').val() == '') {
                Show_Prompt_Box(3, '请输入您的联系方式,否则我们无法与您沟通.');
            } else {
                $.ajax({
                    url: 'http://192.168.43.249:8000/index/advice/',
                    type: 'post',
                    data: {
                        tel: $('[name="tel"]').val(),
                        content: $('[name="content"]').val(),
                        captcha: $('[name="captcha"]').val()
                    },
                    success: function (data) {
                        data = JSON.parse(data)
                        if (data.status) {
                            Show_Prompt_Box(2, '系统已经收到您的反馈,我们将会尽快查看并处理您的反馈!');
                            window.location.href = data.url
                        } else {
                            Show_Prompt_Box(3, '您输入的验证码不正确，请从新输入.');
                        }
                    }
                })
            }
        }
    }

```

为什么要用Math.random()，每次生成的数字不一样，可以防止浏览器使用缓存！
