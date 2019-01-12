from django.db import models
from django.core.validators import URLValidator
from django.db import models
from django.contrib.auth.models import User
# from ckeditor_uploader.fields import RichTextUploadingField
from mdeditor.fields import MDTextField
from PIL import Image
from django.utils.timezone import now
from django.conf import settings
import os
from PIL import Image


#  首页轮播图
class IndexPicture(models.Model):
    name = models.CharField('名称',max_length=100, null=True, blank=True)
    picture = models.ImageField('图片',upload_to="picture", null=True, blank=True)

    def __str__(self):
        return self.name


# 项目简绍
class Project(models.Model):
    title = models.CharField('标题',max_length=20, null=True, blank=True)
    description = models.CharField('简介',max_length=50, null=True, blank=True)
    picture = models.ImageField('图片',upload_to="project", null=True, blank=True)
    time = models.DateTimeField('创建时间', null=True, blank=True, default=now)
    content = MDTextField('内容')


    def __str__(self):
        return self.title


# 新闻或党建工作
class News(models.Model):
    title = models.CharField('标题',max_length=20, null=True, blank=True)
    description = models.CharField('简介',max_length=50, null=True, blank=True)
    time = models.DateTimeField('创建时间', null=True, blank=True, default=now)
    content = MDTextField('内容')

    def __str__(self):
        return self.title


