from django.shortcuts import render
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework.permissions import IsAuthenticated
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.authentication import SessionAuthentication


from .serializers import UserFavSerializer,UserFavDetailSerializer, UserLeavingMessageSerializer,UserAddressSerializer
from .models import UserFav,UserLeavingMessage,UserAddress
from utils.permissions import IsOwnerOrReadOnly

# Create your views here.


class UserFavViewset(viewsets.GenericViewSet, mixins.CreateModelMixin, mixins.ListModelMixin, mixins.DestroyModelMixin, mixins.RetrieveModelMixin):
    """
    list:
        获取用户收藏列表
    retrieve:
        判断某个商品是否已经收藏
    create:
        收藏商品
    delete:
        取消收藏
    """
    def get_serializer_class(self):
        if self.action == "list":
            return UserFavDetailSerializer
        elif self.action == "create":
            return UserFavSerializer
        return UserFavDetailSerializer
    # queryset = UserFav.objects.filter()
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # serializer_class = UserFavSerializer
    lookup_field = 'goods_id'

    def get_queryset(self):
        return UserFav.objects.filter(user=self.request.user)


class UserLeavingMessageViewSet(viewsets.ModelViewSet):
    serializer_class = UserLeavingMessageSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)

    def get_queryset(self):
        return UserLeavingMessage.objects.filter(user=self.request.user)


class UserAddressViewSet(viewsets.ModelViewSet):
    """
    list:
    收货地址列表
    retrieve:
        查看收货地址详情
    create:
        新建收货地址
    update:
    修改收货地址
    delete:
        删除收货地址
    """

    serializer_class = UserAddressSerializer
    authentication_classes = (JSONWebTokenAuthentication, SessionAuthentication)
    permission_classes = (IsAuthenticated, IsOwnerOrReadOnly)
    # lookup_field = "address_id"

    def get_queryset(self):
        return UserAddress.objects.filter(user=self.request.user)

