# Generated by Django 2.1.5 on 2019-01-22 08:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Post', '0002_auto_20190122_1108'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='content',
            field=models.TextField(default=' '),
        ),
        migrations.AlterField(
            model_name='post',
            name='img',
            field=models.ImageField(upload_to='post_img/'),
        ),
    ]
