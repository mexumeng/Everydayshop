from datetime import datetime
from django.db import models


'''
user_model设计
'''


class UserProfile(models.Model):
    name = models.CharField(max_length=20, verbose_name='名字')
    email = models.CharField(max_length=100, verbose_name='电子邮箱')
    birthday = models.CharField(max_length=datetime, verbose_name='生日')
    gender = models.CharField(max_length=2, choices=['male', 'female'])


