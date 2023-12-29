# Generated by Django 3.0.6 on 2020-06-06 03:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='desc',
            field=models.TextField(blank=True, default='', max_length=200, verbose_name='个人简介'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gexing',
            field=models.CharField(blank=True, default='', max_length=100, verbose_name='个性签名'),
        ),
    ]