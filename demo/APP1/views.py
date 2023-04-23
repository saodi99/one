from django.shortcuts import render,HttpResponse
from .mypy import login_my
from .mypy import img_test
from . import forms
from . import models
# Create your views here.
#主页
def index(request):
    return render(request,"index/index.html")
#登录、注册
def login(request):
    if request.method=="POST":
       return login_my.post(request)
    return login_my.get(request)
#个人界面
def user_page(request):
    if request.method=="GET":
        return render(request,"user/user.html")
#个人商品界面
def user_goods_page(request):

    pass
#上架商品
def submit(request):
    if request.method=="GET":
        return render(request,"submit/submit.html")
#购物车页面
def cart(request):
    if request.method=="GET":
        return render(request,"cart/cart.html")
#搜索展示
def searching_goods(request):
    pass
def wallet(request):
    return render(request,"wallet/wallet.html")

def test(req,char):
    pass