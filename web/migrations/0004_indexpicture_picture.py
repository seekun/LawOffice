# Generated by Django 2.1.5 on 2019-01-22 17:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_auto_20190122_1720'),
    ]

    operations = [
        migrations.AddField(
            model_name='indexpicture',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='picture'),
        ),
    ]
