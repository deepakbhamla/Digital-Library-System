from django.db import models
from django.contrib.auth.models import User
class Book(models.Model):
    title=models.CharField(max_length=30)
    auther=models.CharField(max_length=15)
    publisher=models.CharField(max_length=10)
    price=models.FloatField()
    copy=models.IntegerField()

class DLSuser(models.Model):
    user=models.OneToOneField(User,on_delete='models.CASCADE')
    nickname=models.CharField(max_length=20,null=False)
