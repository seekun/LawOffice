# Generated by Django 2.1.5 on 2019-01-12 19:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0006_auto_20190112_1939'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='projectType',
            field=models.CharField(choices=[('办公楼', '办公楼'), ('教育及研究', '教育及研究 '), ('住宅', '住宅 '), ('基础设施', '基础设施 ')], default='办公楼', max_length=50, verbose_name='项目类型'),
        ),
    ]
