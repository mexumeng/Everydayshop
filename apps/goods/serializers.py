__author__ = "xumeng"
__date__ = "2018/11/27 16:26"

from rest_framework import serializers
from goods.models import Goods,GoodsCategory


class GoodsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = GoodsCategory
        fields = "__all__"


class GoodsSerializer(serializers.ModelSerializer):
    category = GoodsCategorySerializer()
    class Meta:
        model = Goods
        fields = "__all__"