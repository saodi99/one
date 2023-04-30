from django.db import models

# Create your models here.
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = models.CharField(max_length=128, unique=True)
    email = models.EmailField(null=False)
    sex = models.CharField(max_length=32, choices=gender, default="未知")
    c_time = models.DateTimeField(auto_now_add=True)
    avater = models.ImageField(upload_to="img",max_length=255,default="img/my.jpg")
    message = models.CharField(blank=True,max_length=255,default="")
class Goods(models.Model):
    c_time = models.DateTimeField(auto_now_add=True)
    name=models.CharField(max_length=50,blank=False)
    level=models.SmallIntegerField(blank=True)
    remark=models.CharField(max_length=255,blank=True)
    price=models.DecimalField(max_digits=10,decimal_places=2,blank=False)
    sort=models.PositiveSmallIntegerField(blank=False)
    count=models.PositiveSmallIntegerField(blank=False)
    display=models.BooleanField(default=False)
    transaction = models.PositiveSmallIntegerField(blank=True,null=True)
    sales = models.PositiveSmallIntegerField(default=0)
    uid =models.IntegerField()
    image=models.ImageField(upload_to="img",max_length=255)

class Passwrd(models.Model):
    c_time = models.DateTimeField(auto_now_add=True)
    password = models.CharField(max_length=255,blank=False)
    uid =models.OneToOneField(User,on_delete=models.CASCADE,primary_key=True)

class Goods_message(models.Model):
    c_time=models.DateTimeField(auto_now_add=True)
    sid=models.IntegerField()
    content=models.CharField(max_length=128)
    display=models.BooleanField(default=True)
    uid=models.IntegerField()

class Post_goods(models.Model):
    c_time=models.DateTimeField(auto_now_add=True)
    displa=models.BooleanField(default=False)
    uid=models.IntegerField()
    sid=models.IntegerField()

class Bought_goods(models.Model):
    c_time=models.DateTimeField(auto_created=True)
    state=models.PositiveSmallIntegerField(default=0)
    uid=models.IntegerField()
    sid=models.IntegerField()
    quantity=models.IntegerField()

class Shopping_cart(models.Model):
    c_time=models.DateTimeField(auto_now_add=True)
    display=models.BooleanField()
    uid=models.IntegerField()
    sid=models.IntegerField()
    quantity=models.IntegerField()
