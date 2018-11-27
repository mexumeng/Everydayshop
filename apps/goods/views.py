# from django.shortcuts import render
from .serializers import GoodsSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
# from rest_framework import status

from .models import Goods

# Create your views here.


class GoodsListView(APIView):
    """
    商品列表展示页数据
    """
    def get(self, request, format=None):
        goods = Goods.objects.all()[:10]
        serializer = GoodsSerializer(goods, many=True)
        return Response(serializer.data)
