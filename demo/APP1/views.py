from django.shortcuts import render,HttpResponse,redirect
from .mypy import login_my
from .mypy import img_test
from .mypy import user_info
from . import forms
from . import models
import os
# Create your views here.

def frame(func): 
    def f(request):
        if request.session.get("info",None):
            session=request.session
            info=session.get("info")
            img=models.User.objects.get(id=session.get("info")["id"]).avater
        else :
            img="/img/my.jpg"
        return func(request,img)
    return f



#主页
@frame
def index(request,*args):
    if  request.method=="GET":
        data=models.Goods.objects.all()
        user=models.User.objects.all()
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
    if request.session.get("info",None):
        if request.method=="GET":
            return user_info.get(request,*args)
        return user_info.post(request,*args)
    else:
        return redirect("login/")
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
                                    uid=request.session.get("info").get("id")
                                    )
    return HttpResponse("OK")

#购物车页面
@frame
def cart(request,*args):
    if request.method=="GET":
        cart=models.Shopping_cart.objects.filter(uid=request.session.get("info")["id"])
        data=[]
        suser=[]
        for i in cart:
            goods=models.Goods.objects.get(id=i.sid)
            data.append({
                "id":goods.id,
                "name":goods.name,
                "price":goods.price,
                "img":goods.image,
                "count":goods.count,    
                "display":goods.display,
                "seller_id":goods.uid
                })
            scr={
                "seller_id":goods.uid,
                "uname":models.User.objects.get(id=goods.uid).name,
                "avater":models.User.objects.get(id=goods.uid).avater,
            }
            if scr not in suser :
                suser.append(scr) 
        print(data)
        return render(request,"cart/cart.html",locals())
    print(request.POST)
    models.Shopping_cart.objects.create(
        display=True,
        uid=request.session.get("info")["id"],
        sid=request.POST.get("Goods"),
        quantity=1
    )
    return redirect("/cart")
#搜索展示
def searching_goods(request):
    pass
def wallet(request):
    return render(request,"wallet/wallet.html")

def exit(req):
    req.session.flush()
    return redirect("/index")

def user_set(requset):
    set=models.Goods.objects.filter(id=requset.POST.get("Goods"))
    set.update(display=not set[0].display)
    return redirect("/user")
def show(request,uid):
    print(uid)
    return redirect("/index")
def  test(requset):
    print(requset.GET)
    return HttpResponse("未实现")