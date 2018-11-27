__author__ = "xumeng"
__date__ = "2018/11/27 16:26"

from rest_framework import serializers


class GoodsSerializer(serializers.Serializer):
    name = serializers.CharField(required=True,max_length=100)
    click_num = serializers.IntegerField(default=0)
    goods_front_image = serializers.ImageField()