from datetime import datetime
from django.db import models
from users.models import UserProfile
from goods.models import Goods
# 但是当第三方模块根本不知道你的user model在哪里如何导入呢
from django.contrib.auth import get_user_model
# 这个方法会去setting中找AUTH_USER_MODEL
User = get_user_model()


# Create your models here.


class ShoppingCart(models.Model):
    """
    购物车
    """
    user = models.ForeignKey(User, verbose_name=u"用户", related_name=u"用户", on_delete=models.CASCADE)
    goods = models.ForeignKey(Goods, verbose_name=u"商品", on_delete=models.CASCADE)
    nums = models.IntegerField(default=0, verbose_name=u"购买数量")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"购物车"
        verbose_name_plural = verbose_name

    def __str__(self):
        return "{name}({nums})".format(name=self.goods.name, nums=self.nums)


class OrderInfo(models.Model):
    """
    订单信息
    """
    ORDER_STATUS = (
        ("TRADE_SUCCESS", u"成功"),
        ("TRADE_CLOSED", u"超时关闭"),
        ("WAIT_BUYER_PAY", u"交易创建"),
        ("TRADE_FINISHED", u"交易结束"),
        ("paying", u"待支付"),
    )
    PAY_TYPE = (
        ("alipay", u"支付宝"),
        ("wechat", u"微信"),
    )

    user = models.ForeignKey(User, verbose_name=u"用户", on_delete=models.CASCADE)
    # unique订单号唯一
    order_sn = models.CharField(max_length=30, null=True, blank=True, unique=True, verbose_name=u"订单编号")
    # 微信支付可能会用到
    nonce_str = models.CharField(max_length=50, null=True, blank=True, unique=True, verbose_name=u"随机加密串")
    # 支付宝支付时的交易号与本系统进行关联
    trade_no = models.CharField(max_length=100, unique=True, null=True, blank=True, verbose_name=u"交易号")
    # 以防用户支付到一半不支付了
    pay_status = models.CharField(choices=ORDER_STATUS, default="paying", max_length=30, verbose_name=u"订单状态")
    # 订单的支付类型
    pay_type = models.CharField(choices=PAY_TYPE, default="alipay", max_length=10, verbose_name=u"支付类型")
    post_script = models.CharField(max_length=200, verbose_name=u"订单留言")
    order_mount = models.FloatField(default=0.0, verbose_name=u"订单金额")
    pay_time = models.DateTimeField(null=True, blank=True, verbose_name=u"支付时间")

    # 用户的基本信息
    address = models.CharField(max_length=100, default="", verbose_name=u"收货地址")
    signer_name = models.CharField(max_length=20, default="", verbose_name=u"签收人")
    signer_mobile = models.CharField(max_length=11, verbose_name=u"联系电话")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"订单基本信息"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order_sn)


class OrderGoods(models.Model):
    """
    订单内的商品详情
    """
    # 一个订单对应多个商品，所以添加外键
    order = models.ForeignKey(OrderInfo, verbose_name=u"订单信息", related_name="goods", on_delete=models.CASCADE)
    # 两个外键形成一张关联表
    goods = models.ForeignKey(Goods, verbose_name=u"商品", on_delete=models.CASCADE)
    goods_num = models.IntegerField(default=0, verbose_name=u"商品数量")

    add_time = models.DateTimeField(default=datetime.now, verbose_name=u"添加时间")

    class Meta:
        verbose_name = u"订单内商品项"
        verbose_name_plural = verbose_name

    def __str__(self):
        return str(self.order.order_sn)

