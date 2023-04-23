from django.contrib import admin

# Register your models here.
from . import models
admin.site.register(models.User)
admin.site.register(models.Bought_goods)
admin.site.register(models.Goods)
admin.site.register(models.Goods_message)
admin.site.register(models.Passwrd)
admin.site.register(models.Shopping_cart)
admin.site.register(models.Post_goods)
