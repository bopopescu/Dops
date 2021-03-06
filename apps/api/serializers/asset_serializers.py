# -*- coding: utf-8 -*-
# @Time    : 2019-07-30 14:24
# @Author  : kbsonlong
# @Email   : kbsonlong@gmail.com
# @Blog    : www.alongparty.cn
# @File    : asset_serializers.py
# @Software: PyCharm
from rest_framework import serializers

from cmdb import models

class AssetSerializer(serializers.ModelSerializer):
    """
    资产列表
    """
    class Meta:
        model = models.Asset
        fields = '__all__'



class ServerSerializer(serializers.ModelSerializer):
    """
    服务器管理
    """
    asset = AssetSerializer(many=False, required=False)
    class Meta:
        model = models.Server
        fields = '__all__'


    def create(self, validated_data):
        if validated_data.get('asset'):
            assets_data = validated_data.pop('asset')
            assets = models.Asset.objects.create(**assets_data)
        else:
            assets = models.Asset()
        validated_data['asset'] = assets
        server = models.Server.objects.create(**validated_data)
        return server

class EnvSerializer(serializers.ModelSerializer):
    """
    运行环境管理
    """
    class Meta:
        model = models.Env
        fields = '__all__'


class IdcSerializer(serializers.ModelSerializer):
    """
    机房序列化
    """
    class Meta:
        model = models.IDC
        fields = '__all__'

class ProductSerializer(serializers.ModelSerializer):
    """
    业务线
    """
    class Meta:
        model = models.Product
        fields = '__all__'

class AppSerializer(serializers.ModelSerializer):
    """
    I应用管理
    """
    class Meta:
        model = models.App
        fields = '__all__'


# class ResourceSerializer(serializers.ModelSerializer):
#     """
#     资源申请管理
#     """
#     class Meta:
#         model = models.Resource
#         fields = ['user','approver','resource_type','resource_detail',]