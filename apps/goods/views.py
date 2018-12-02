from .serializers import GoodsSerializer, CategorySerializer, HotSearchSerializer, BannerSerializer
from rest_framework.pagination import PageNumberPagination
from rest_framework import viewsets
from rest_framework import mixins
from rest_framework import filters
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.authentication import TokenAuthentication
from .models import Goods, GoodsCategory, HotSearchWords, Banner
from .filter import GoodsFilter
# Create your views here.


class GoodsListPagination(PageNumberPagination):
    """
    定制分页
    """

    page_size = 12
    page_size_query_param = 'page_size'
    page_size_param = 'page'
    max_page_size = 100


class CategoryViewSet(mixins.ListModelMixin, viewsets.GenericViewSet, mixins.RetrieveModelMixin):
    """
    list:
        商品分类列表数据
    retrieve:
        获取商品分类详情
    """
    queryset = GoodsCategory.objects.filter(category_type=1)
    serializer_class = CategorySerializer


class GoodsListViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    list:
        商品列表,分页，搜索，过滤

    retrieve:
        商品详情
    """
    queryset = Goods.objects.all()
    serializer_class = GoodsSerializer
    pagination_class = GoodsListPagination
    # 权限验证单个view接口,goods列表用不到，总不能让用户登陆之后才能看到商品列表吧
    # authentication_classes = (TokenAuthentication,)
    filter_backends = (DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter)
    # filter_fields = ('name', 'shop_price')
    filter_class = GoodsFilter
    search_fields = ('name', 'goods_brief', 'goods_desc')
    ordering_fields = ('sold_num', 'shop_price')


#
    # def get_queryset(self):
    #     queryset = Goods.objects.all()
    #     price_min = self.request.query_params.get("price_min",0)
    #     if price_min:
    #         queryset.filter(shop_price__gt=int(price_min))
    #     return queryset


class HotSearchViewSet(viewsets.ModelViewSet):
    serializer_class = HotSearchSerializer
    queryset = HotSearchWords.objects.all()


class BannerViewSet(viewsets.ModelViewSet):
    serializer_class = BannerSerializer
    queryset = Banner.objects.all()
