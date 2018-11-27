from datetime import datetime
from django.db import models
from django.contrib.auth.models import AbstractUser


class UserProfile(AbstractUser):

    """
    用户表
    """
    GENDER_CHOICE = (
        ('male', u'男'),
        ('female', u'女')
    )
    username = models.CharField(max_length=20, blank=True, null=True,unique=True, verbose_name=u'名字')
    email = models.CharField(max_length=100, blank=True, null=True, verbose_name='电子邮箱')
    birthday = models.DateField(blank=True, null=True, verbose_name='生日')
    gender = models.CharField(max_length=10, choices=GENDER_CHOICE, default='female', verbose_name=u'性别')
    mobile = models.CharField(max_length=11, verbose_name='手机号')

    class Meta:
        verbose_name = u'用户'
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.username


class VerifyCode(models.Model):
    """
    短信验证码,回填验证码进行验证。可以保存在redis中
    """
    code = models.CharField(max_length=10, verbose_name="验证码")
    mobile = models.CharField(max_length=11, verbose_name="电话")
    add_time = models.DateTimeField(default=datetime.now, verbose_name="添加时间")

    class Meta:
        verbose_name = "短信验证码"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.code



