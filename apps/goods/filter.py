__author__ = "xumeng"
__date__ = "2018/11/28 16:17"


from django.db.models import Q
import django_filters
from rest_framework import generics


from .models import Goods


class GoodsFilter(django_filters.rest_framework.FilterSet):
    def top_category_filter(self, queryset, name, value):
        # 不管当前点击的是一级目录二级目录还是三级目录。
        return queryset.filter(Q(category_id=value)|Q(category__parent_category_id=value)|Q(category__parent_category__parent_category_id=value))
    pricemin = django_filters.NumberFilter(field_name="shop_price", lookup_expr='gte')
    pricemax = django_filters.NumberFilter(field_name="shop_price", lookup_expr='lte')
    name = django_filters.CharFilter(field_name='name', lookup_expr='icontains')
    top_category = django_filters.NumberFilter(name="category", method='top_category_filter')

    class Meta:
        model = Goods
        fields = ['pricemax', 'pricemin', 'name', 'top_category', 'is_hot']




