from django.contrib import admin
from market.models import Goods, Category
# Register your models here.

# from django.contrib.auth.models import User
admin.site.register(Goods)
admin.site.register(Category)