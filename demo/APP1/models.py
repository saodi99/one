from django.db import models

# Create your models here.
class Status(models.TextChoices):
     UNSTARTED = 'u', "Not started yet"
     ONGOING = 'o', "Ongoing"
     FINISHED = 'f', "Finished"
class User(models.Model):

    gender = (
        ('male', "男"),
        ('female', "女"),
    )
    name = models.CharField(verbose_name="用户昵称",max_length=128, unique=True)
    email = models.EmailField(verbose_name="邮箱",null=False)
    sex = models.CharField(verbose_name="性别",max_length=32, choices=gender, default="未知")
    c_time = models.DateTimeField(verbose_name="注册时间",auto_now_add=True)
    avater = models.ImageField(verbose_name="头像",upload_to="img",max_length=255,default="img/my.jpg")
    message = models.CharField(verbose_name="留言",blank=True,max_length=255,default="")
    class Meta:
         verbose_name = "用户信息"
         verbose_name_plural = "用户"
    def __str__(self):
         return self.name
class Goods(models.Model):
    c_time = models.DateTimeField(verbose_name="修改时间",auto_now_add=True)
    name=models.CharField(verbose_name="商品名称",max_length=50,blank=False)
    level=models.SmallIntegerField(verbose_name="商品成色",blank=True)
    remark=models.CharField(verbose_name="商品详细",max_length=255,blank=True)
    price=models.DecimalField(verbose_name="商品价格",max_digits=10,decimal_places=2,blank=False)
    sort=models.PositiveSmallIntegerField(verbose_name="商品类别",blank=False)
    count=models.PositiveSmallIntegerField(verbose_name="商品数量",blank=False)
    display=models.BooleanField(verbose_name="已上架",default=False)
    transaction = models.PositiveSmallIntegerField(verbose_name="交易方式",blank=True,null=True)
    sales = models.PositiveSmallIntegerField(verbose_name="商品销量",default=0)
    uid =models.IntegerField(verbose_name="商品卖家",)
    image=models.ImageField(verbose_name="商品图片",upload_to="img",max_length=255)
    class Meta:
         verbose_name = "商品信息"
         verbose_name_plural = "商品信息"
class Passwrd(models.Model):
    c_time = models.DateTimeField(verbose_name="修改时间",auto_now_add=True)
    password = models.CharField(verbose_name="用户密码",max_length=255,blank=False)
    uid =models.OneToOneField(User,verbose_name="用户id",on_delete=models.CASCADE,primary_key=True)
    class Meta:
         verbose_name = "密码"
         verbose_name_plural = "密码"
class Goods_message(models.Model):
    c_time=models.DateTimeField(verbose_name="修改时间",auto_now_add=True)
    sid=models.IntegerField(verbose_name="商品的id",)
    content=models.CharField(verbose_name="留言内容",max_length=128)
    display=models.BooleanField(verbose_name="是否可见",default=True)
    uid=models.IntegerField(verbose_name="评论的用户id",)
    class Meta:
         verbose_name = "商品留言"
         verbose_name_plural = "商品留言"
class Post_goods(models.Model):
    c_time=models.DateTimeField(verbose_name="修改时间",auto_now_add=True)
    displa=models.BooleanField(verbose_name="是否被删除",default=False)
    uid=models.IntegerField(verbose_name="用户id",)
    sid=models.IntegerField(verbose_name="对应商品id",)
    class Meta:
         verbose_name = "用户发布的商品"
         verbose_name_plural = "用户发布的商品"
class Bought_goods(models.Model):
    c_time=models.DateTimeField(verbose_name="修改时间",auto_created=True)
    state=models.PositiveSmallIntegerField(verbose_name="商品当前的状态",default=0)
    uid=models.IntegerField(verbose_name="用户id",)
    sid=models.IntegerField(verbose_name="商品id",)
    quantity=models.IntegerField(verbose_name="商品数量",)
    class Meta:
         verbose_name = "用户已购买商品"
         verbose_name_plural = "用户已购买商品"
class Shopping_cart(models.Model):
    c_time=models.DateTimeField(verbose_name="修改时间",auto_now_add=True)
    display=models.BooleanField(verbose_name="商品是否被删除",)
    uid=models.IntegerField(verbose_name="用户id",)
    sid=models.IntegerField(verbose_name="商品id",)
    quantity=models.IntegerField(verbose_name="商品数量",)
    class Meta:
         verbose_name = "用户购物车"
         verbose_name_plural = "用户购物车"