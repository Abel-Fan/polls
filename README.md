# polls
Django入门案例
## 创建项目
#### 1. 创建Django项目
```
django-admin startprojects polls
```
###### 1.1 目录结构
```
polls
    |__  __init__.py
    |__ settings.py  项目配置文件
    |__ urls.py  总路由文件
    |__ wsgi.py  Web服务器配置信息
manage.py  Django命令文件
```
###### 1.2 设置语言
settings.py 文件中
```
LANGUAGE_CODE = 'zh-hans'
```
###### 1.3 设置时区
settings.py 文件中
```
TIME_ZONE = 'Asia/Shanghai'
```
###### 1.3 设置数据库
settings.py 文件中
```
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'polls',
        'USER':'root',
        'PASSWORD':'123456',
        'PORT':'3306',
        'HOST':'localhost'
    }
}
```
因为python3 是通过pymysql进行数据连接所以需要额外设置

polls/__init__.py
```
import pymysql
pymysql.install_as_MySQLdb()
```

#### 2. 创建应用
```
python manage.py startapp polls1
```
###### 2.1目录结构
```
polls
    |...
polls1
    |__ migrations 迁移文件（将ORM模型转化为SQL语言）的版本信息
    |__ __init__.py
    |__ admin.py polls1应用的后台界面
    |__ apps.py 应用基本信息
    |__ models.py 应用模型信息
    |__ tests.py  测试文件
    |__ views.py  视图文件
...
```
###### 2.2还需创建的文件
```
forms.py  form表单文件（创建表单\表单数据验证）
urls.py  应用路由文件
```
###### 2.3挂载应用
在 polls/settings.py文件中设置
```
INSTALLED_APPS = [
    'django.contrib.admin',
     ...,
     'polls1's,
]
```
###### 2.4设置分路由
在 polls/urls.py文件中设置
```
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('admin/', admin.site.urls),
    path("",include("polls1.urls"))
]
```
###### 2.5 创建第一个视图
在polls1/views.py中设置
```
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return HttpResponse("hello world")
```
###### 2.6 设置应用路由
```
from django.urls import path
from . import views

urlpatterns=[
    path("",views.index)
]
```
##### 3 运行项目
```
python manage.py runserver
python manage.py runserver 8000
python manage.py runserver 127.0.0.1:8000
```
## 项目需求
#### 1 数据字典

###### 1.1 questions

字段|类型|默认值|备注
---|---|---|---
id| int| |主键
question_text| varchar| |问题题目
pub_date|datetime| |时间

###### 1.2 choices

字段|类型|默认值|备注
---|---|---|---
id| int| |主键
choice_text| varchar| |选项
votes|int| |投票数

#### 2 创建models
###### 2.1 创建模型
/polls1/models.py
```
from django.db import models

# Create your models here.

class Questions(models.Model):
    # id可以省略
    class meta:  # 元类
        db_table = "questions"
    question_text = models.CharField(max_length=200,verbose_name="问题")
    pub_date = models.DateTimeField(verbose_name="问题")

    def __str__(self):
        return self.question_text

class Choices(models.Model):
    class meta:  # 元类
        db_table = "choices"
    question = models.ForeignKey(Questions,on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=200,verbose_name="选项")
    votes = models.IntegerField(default=0,verbose_name="熟练")

    def __str__(self):
        return  self.choice_text
```
###### 2.2 创建迁移文件
```
python manage.py makemigrations polls1
```
###### 2.3 执行迁移
**mysql中需要提前创建好数据库**
```
python manage.py migrate
```
**完成以后会创建出很多除了 questions choices 意外的 Django 必备数据表**

#### 3 创建admin
###### 3.1 创建超级用户
```
python manage.py createsuperuser
```
- 根据命令提示完成创建
- 通过 /admin访问后台
###### 3.2 创建polls1应用的后台界面
/polls1/admin.py










