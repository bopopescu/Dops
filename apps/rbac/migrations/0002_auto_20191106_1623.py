# Generated by Django 2.2.5 on 2019-11-06 08:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='role',
            options={'verbose_name': '角色表', 'verbose_name_plural': '角色表'},
        ),
        migrations.AlterModelOptions(
            name='userinfo',
            options={'verbose_name': '用户表', 'verbose_name_plural': '用户表'},
        ),
    ]
