# Generated by Django 2.2.5 on 2019-11-20 15:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0008_userinfo_limit'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='comment',
            field=models.CharField(blank=True, max_length=128, null=True, verbose_name='User Comment'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='login_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Login By'),
        ),
        migrations.AddField(
            model_name='userinfo',
            name='valid_date',
            field=models.DateTimeField(blank=True, null=True, verbose_name='Valid Date'),
        ),
    ]
