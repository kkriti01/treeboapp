from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User


class Product(models.Model):
    name = models.CharField(max_length=100, blank=True, null=True)
    price = models. FloatField()
    url = models.CharField(max_length=225)


class UserSubscription(models.Model):
    user = models.ManyToManyField(User,blank=True)
    subscribe = models.CharField(max_length=20)
    product = models.ManyToManyField(Product, blank=True,null=True)
    reason = models.CharField(max_length=225, blank=True, null=True)
    notification_choice = (('ALWAYS', 'ALWAYS'),
                           ('ALL_TIME_LOW', 'ALL_TIME_LOW'),
                           ('MORE_THAN_10', 'MORE_THAN_10'))
    notification_interval = models.CharField(choices=notification_choice, max_length=25,default='')



