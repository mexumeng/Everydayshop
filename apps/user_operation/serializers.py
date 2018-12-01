
__author__ = "xumeng"
__date__ = "2018/11/29 17:21"

from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator


from .models import UserFav, UserLeavingMessage, UserAddress
from goods.serializers import GoodsSerializer


class UserFavDetailSerializer(serializers.ModelSerializer):
    goods = GoodsSerializer()

    class Meta:
        model = UserFav
        fields = ("goods", "id")


class UserFavSerializer(serializers.ModelSerializer):

    user = serializers.HiddenField(
        default=serializers.CurrentUserDefault(), help_text="用户"
    )

    class Meta:
        model = UserFav
        fields = ("user", "goods", "id")
        # 使用validate方式实现唯一联合
        validators = [
            UniqueTogetherValidator(
                queryset=UserFav.objects.all(),
                fields=('user', 'goods'),
                message="已经收藏"
            )
        ]


class UserLeavingMessageSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(),help_text="用户")
    add_time =serializers.DateTimeField(read_only=True,help_text="创建日期")

    class Meta:
        model = UserLeavingMessage
        fields = ("user", "msg_type", "subject", "message", "file", "id", "add_time")


class UserAddressSerializer(serializers.ModelSerializer):
    user = serializers.HiddenField(default=serializers.CurrentUserDefault(),help_text=u"用户")
    add_time = serializers.DateTimeField(read_only=True, help_text=u'添加日期')

    class Meta:
        model = UserAddress
        fields = ("user","province", "city", "address", "signer_name", "signer_mobile","add_time", "id")
