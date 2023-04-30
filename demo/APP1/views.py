from django.shortcuts import render,HttpResponse,redirect
from .mypy import login_my
from .mypy import img_test
from . import forms
from . import models
import os
# Create your views here.

def frame(func): 
    def f(request):
        session=request.session
        print(session.get("info"))
        img=models.User.objects.get(id=session.get("info")["id"]).avater
        return func(request,img)
    return f



#主页
@frame
def index(request,*args):
    if  request.method=="GET":
        data=models.Goods.objects.all()
        print(locals())
        return render(request,"index/index.html",locals())
    print(request.POST)
    return redirect("/index")
#登录、注册
def login(request):
    if request.method=="POST":
       return login_my.post(request)
    return login_my.get(request)
#个人界面
@frame
def user_page(request,*args):
    if request.method=="GET":
        user=models.User.objects.get(id=request.session.get("info").get("id"))
        data=models.Goods.objects.all()
        return render(request,"user/user.html",locals())
#个人商品界面---------（合并到个人界面）
def user_goods_page(request):

    pass
#上架商品
@frame
def submit(request,*args):
    goods=forms.goods()
    if request.method=="GET":
        return render(request,"submit/submit.html",locals())
    data=forms.goods(request.POST,request.FILES)
   
    
    if data.is_valid():
        req=data.cleaned_data
        img=req.get("Goods_img")
        img_path=os.path.join("APP1","static","img",img.name)
        with open(img_path,"wb+") as f:
            for chunk in img.chunks():
                f.write(chunk)
        print(req)
        models.Goods.objects.create(name=req.get("Goods_name"),
                                    level=req.get("Goods_level"),
                                    remark=req.get("Goods_remark"),
                                    price=req.get("Goods_price"),
                                    sort=req.get("Goods_sort"),
                                    count=req.get("Goods_coumt"),
                                    image=os.path.join("img",img.name),
                                    uid=10
                                    )
    return HttpResponse("OK")

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