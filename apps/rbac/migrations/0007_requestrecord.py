# Generated by Django 2.2.5 on 2019-11-20 14:47

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('rbac', '0006_auto_20191108_1058'),
    ]

    operations = [
        migrations.CreateModel(
            name='RequestRecord',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ipaddr', models.GenericIPAddressField(verbose_name='Client Address')),
                ('datetime', models.DateTimeField(auto_now_add=True, verbose_name='Request Date Time')),
                ('type', models.IntegerField(choices=[(0, 'GET'), (1, 'POST')], verbose_name='Request Type')),
                ('get_full_path', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Request Full Path')),
                ('post_body', models.CharField(blank=True, max_length=1024, null=True, verbose_name='Request Post Body')),
                ('username', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL, verbose_name='UserName')),
            ],
            options={
                'verbose_name': 'Request Record',
                'verbose_name_plural': 'Request Record',
                'db_table': 'requestrecord',
            },
        ),
    ]
