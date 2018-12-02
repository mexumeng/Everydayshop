"""Everydayshop URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
# from django.contrib import admin
from django.views.static import serve
from django.urls import path, include, re_path
import xadmin, DjangoUeditor
from .settings import MEDIA_ROOT

# from goods.views_base import GoodsListView
from goods.views import GoodsListViewSet, CategoryViewSet, HotSearchViewSet, BannerViewSet
from users.views import SysCodeViewSet,UserViewset
from user_operation.views import UserFavViewset, UserLeavingMessageViewSet,UserAddressViewSet
from trade.views import ShoppingCartViewSet,OrderViewSet
from rest_framework.documentation import include_docs_urls
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views
from rest_framework_jwt.views import obtain_jwt_token


router = DefaultRouter()
# 商品列表页
router.register('goods', viewset=GoodsListViewSet, base_name='goods',)
router.register('categorys', viewset=CategoryViewSet, base_name='categorys',)
router.register('codes', SysCodeViewSet, base_name='codes',)
router.register('users', UserViewset, base_name='users',)
router.register('userfavs',UserFavViewset, base_name='userfavs')
router.register('messages',UserLeavingMessageViewSet, base_name='messages')
router.register('address',UserAddressViewSet, base_name='address')
router.register('shopcarts',ShoppingCartViewSet, base_name='shopcarts')
router.register('orders',OrderViewSet, base_name='orders')
router.register('hotsearchs',HotSearchViewSet, base_name='hotsearchs')
router.register('banners',BannerViewSet, base_name='banners')





urlpatterns = [
    path('xadmin/', xadmin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('ueditor', include('DjangoUeditor.urls')),
    # 处理图片显示的url,使用Django自带serve,传入参数告诉它去哪个路径找，我们有配置好的路径MEDIAROOT
    re_path('media/(?P<path>.*)', serve, {"document_root": MEDIA_ROOT}),
    path('docs/', include_docs_urls(title="孟哥哥商城文档")),
    # drf自带的权限认证
    path('api-token-auth/', views.obtain_auth_token),
    path('', include(router.urls)),
    # jwt的权限认证
    path('login/', obtain_jwt_token)
]
