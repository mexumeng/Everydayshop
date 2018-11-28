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
    serializer_class = GoodsSerializer
    pagination_class = GoodsListPagination

    def get_queryset(self):
        queryset = Goods.objects.all()
        price_min = self.request.query_params.get("price_min",0)
        if price_min:
            queryset.filter(shop_price__gt=int(price_min))
        return queryset




