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
        for good in goods:
            json_dict = {}
            json_dict['name'] = good.name
            json_dict['category'] = good.category.name
            json_dict['market_price'] = good.market_price
            json_list.append(json_dict)
        import json
        from django.http import HttpResponse
        json_data = json.dumps(json_list)
        return HttpResponse(json_data, content_type='application/json')


