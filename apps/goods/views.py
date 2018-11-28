from .serializers import GoodsSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from .models import Goods

# Create your views here.


class GoodsListPagination(PageNumberPagination):
    '''
    定制分页
    '''
    page_size = 10
    page_size_query_param = 'page_size'
    page_size_param = 'p'
    max_page_size = 100


class GoodsListViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    """
    商品列表页
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsListPagination




