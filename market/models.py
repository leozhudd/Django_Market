from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Category(models.Model):
    name = models.CharField(max_length=32,unique=True)
    id = models.AutoField(primary_key=True)
    def __str__(self):
        return self.name

class Goods(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=128)
    description = models.CharField(max_length=512,blank=True,null=True)
    trade_location = models.CharField(max_length=32,choices=(('学院路校区','学院路校区'),('沙河校区','沙河校区')),default="学院路校区")
    price = models.IntegerField()
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    picture = models.ImageField(upload_to='goods',blank=True,null=True)
    seller = models.ForeignKey(User,on_delete=models.CASCADE,blank=True,null=True)
    goods_phone = models.IntegerField(null=True,blank=True)
    publish_time = models.DateField(auto_now_add=True,blank=True,null=True)

    def __str__(self):
        return self.name
