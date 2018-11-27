__author__ = "xumeng"
__date__ = "2018/11/25 21:56"
from django.views.generic.base import View
from django.views.generic import ListView
from goods.models import Goods


class GoodsListView(View):

    def get(self, request):
        '''
        通过django的view实现商品列表页
        :param request:
        :return:
        '''
        json_list = []
        goods = Goods.objects.all()[:10]
        # for good in goods:
        #     json_dict = {}
        #     json_dict['name'] = good.name
        #     json_dict['category'] = good.category.name
        #     json_dict['market_price'] = good.market_price
        #     json_list.append(json_dict)
        # from django.forms.models import model_to_dict
        """
        通过model_to_dict将good所有的字段提取转化成dict类型,
        问题是imgaeFiled和DateFIled无法序列化成json格式，下面用serialize替换此方法"""
        # for good in goods:
        #     json_dict = model_to_dict(good)
        #     json_list.append(json_dict)
        from django.core import serializers
        '''
        通过serializers将goods直接序列化成json格式
        '''
        import json
        from django.http import HttpResponse, JsonResponse
        json_data = serializers.serialize("json", goods)
        json_data = json.loads(json_data)
        return JsonResponse(json_data,safe=False)


