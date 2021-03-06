__author__ = "xumeng"
__date__ = "2018/12/1 17:03"
import time
from rest_framework import serializers


from .models import ShoppingCart,OrderInfo,OrderGoods
from goods.models import Goods
from goods.serializers import GoodsSerializer

class ShopDirectSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)
    class Meta:
        model = ShoppingCart
        fields = '__all__'


class ShopCartSerializer(serializers.Serializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), help_text='用户')
    add_time = serializers.DateTimeField(read_only=True,format="%Y-%m-%d %H:%M", help_text="添加时间")
    nums = serializers.IntegerField(required=True, min_value=1, error_messages={"min_value": "商品数量不能小于1",
                                                                               "required": "请输入商品数量"}
                                    )
    goods = serializers.PrimaryKeyRelatedField(required=True, queryset=Goods.objects.all(), help_text="商品")

    def create(self, validated_data):
        user = self.context['request'].user
        nums = validated_data['nums']
        goods = validated_data['goods']
        existed = ShoppingCart.objects.filter(user=user, goods=goods)
        if existed:
            existed = existed[0]
            existed.nums += nums
            existed.save()
        else:
            existed = ShoppingCart.objects.create(**validated_data)
        return existed

    def update(self, instance, validated_data):
        # 修改商品数量
        instance.nums = validated_data["nums"]
        instance.save()
        return instance


class OrderSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(), help_text='用户')
    pay_status = serializers.CharField(read_only=True)
    trade_no = serializers.CharField(read_only=True)
    order_sn = serializers.CharField(read_only=True)
    pay_time = serializers.DateTimeField(read_only=True)
    nonce_str = serializers.DateTimeField(read_only=True)

    def generate_order_sn(self):
        # 当前时间+userid+随机数
        from random import Random
        random_ins = Random()
        order_sn = "{time_str}{userid}{ranstr}".format(time_str=time.strftime("%Y%m%d%H%M%S"),
                                                       userid=self.context["request"].user.id, ranstr=random_ins.randint(10, 99))
        return order_sn

    def validate(self, attrs):
        attrs["order_sn"] = self.generate_order_sn()
        return attrs

    class Meta:
            model = OrderInfo
            fields = '__all__'


class OrderGoodsSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer(many=False)

    class Meta:
        model = OrderGoods
        fields = "__all__"


class OrderDetailSerializer(serializers.ModelSerializer):
    goods = OrderGoodsSerializer(many=True)

    class Meta:
        model = OrderInfo
        fields = "__all__"
