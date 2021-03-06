from django.db import models
from django.core.validators import URLValidator
from django.db import models
from django.contrib.auth.models import User
# from ckeditor_uploader.fields import RichTextUploadingField
from mdeditor.fields import MDTextField
from django.utils.timezone import now




#  首页轮播图
class IndexPicture(models.Model):
    name = models.CharField('名称', max_length=100, null=True, blank=True)
    picture = models.ImageField(upload_to="picture", null=True, blank=True)


    def __str__(self):
        return self.name


# 项目简绍
class Project(models.Model):
    choiceType = (
        ('办公楼', '办公楼'),
        ('教育及研究', '教育及研究 '),
        ('住宅', '住宅 '),
        ('基础设施', '基础设施 ')
    )
    title = models.CharField('标题', max_length=50, null=True, blank=True)
    description = models.TextField('简介', max_length=500, null=True, blank=True)
    projectType = models.CharField('项目类型', max_length=50, choices=choiceType, default='办公楼')
    projectTime = models.DateField('项目时间', max_length=50, null=True, blank=True)
    picture = models.ImageField(upload_to="project", null=True, blank=True)

    # picture = ProcessedImageField(upload_to="project", null=True, blank=True,
    #                               processors=[ResizeToFill(1540, 1100)],
    #                               format='JPEG',
    #                               options={'quality': 95},
    #                               )

    time = models.DateTimeField('创建时间', null=True, blank=True, default=now)
    content = MDTextField('内容')

    def __str__(self):
        return self.title


# 新闻或党建工作
class News(models.Model):
    title = models.CharField('标题', max_length=50, null=True, blank=True)
    description = models.TextField('简介', max_length=500, null=True, blank=True)
    time = models.DateTimeField('创建时间', null=True, blank=True, default=now)
    content = MDTextField('内容',null=True, blank=True,)

    def __str__(self):
        return self.title
