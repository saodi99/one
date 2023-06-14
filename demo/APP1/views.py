from django.shortcuts import render,HttpResponse,redirect
from django.http import JsonResponse
from .mypy import login_my
from .mypy import img_test
from .mypy import user_info
from . import forms

from . import models
import os
import pyqrcode
import random
# Create your views here.

def frame(func): 
    def f(request,num=1):
        if request.session.get("info",None):
            session=request.session
            info=session.get("info")
            img=models.User.objects.get(id=session.get("info")["id"]).avater
        else :
            img="/img/my.jpg"
        return func(request,img,num)
    return f



#主页
@frame
def index(request,*args):
    if  request.method=="GET":
        if args[1]<=0:

            return redirect("/index")
        # data=models.Goods.objects.order_by("?")[(args[1]-1)*15:(args[1]-1)*15+15]
        user=models.User.objects.all()
        data=list(models.Goods.objects.all()[(args[1]-1)*15:(args[1]-1)*15+15])
        random.shuffle(data)
        count=range(models.Goods.objects.count()//15+1)
        print(locals())
        return render(request,"index/index.html",locals())
    print(request.POST)
    return redirect("/index")

#登录、注册
def login(request):
    if request.method=="POST":
    #    print(request.POST)
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
    print(request)
    goods=forms.goods()
    if request.method=="GET":
        if request.session.get("info",None):
            return render(request,"submit/submit.html",locals())
        else:
            return redirect("/login")
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
    return redirect("/user")

#购物车页面
@frame
def cart(request,*args):
    if request.session.get("info",None):
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
    else:
            return redirect("/login")
#搜索展示
def searching_goods(request):
    pass
@frame
def wallet(request,*args):
    if request.session.get("info",None):
        return render(request,"wallet/wallet.html",locals())
    return redirect("/login")
def exit(req):
    req.session.flush()
    return redirect("/index")

def user_set(request):
    set=models.Goods.objects.filter(id=request.POST.get("Goods"))
    set.update(display=not set[0].display)
    return redirect("/user")

def show(request,uid):
    user=models.User.objects.get(id=uid)
    data=models.Goods.objects.filter(uid=uid)
    args=(user.avater,)
    print(locals())
    return render(request,"user/other.html",locals())
def test(request,i):
    data=models.Shopping_cart.objects.filter(uid=request.session.get("info")["id"])
    if i==0:
        data.first().delete()
    elif i==1:
        data.delete()
    return redirect("/cart")
@frame
def qr(req,*args):
    if req.session.get("info",None):
        url=req.get_host()+"/user/"+str(req.session.get("info")["id"])
        url=pyqrcode.create(url,version=5)
        qr_path=os.path.join("APP1","static","qr",str(req.session.get("info")["id"])+".svg")
        print(url.terminal(quiet_zone=1))
  
        url.svg(qr_path,scale=8)
        qr=os.path.join("qr",str(req.session.get("info")["id"])+".svg")
        print(locals())
        return render(req,"QR/qr.html",locals())
    return redirect("/login")
def img(req,str):
    return redirect("/static/img/"+str)
@frame
def set(req,*args):

    if req.method=="GET":
        uid=req.session.get("info").get("id")
        user=models.User.objects.get(id=uid)
        data=models.Goods.objects.filter(uid=uid)
        form_data = {
        "sex":user.sex,
        "email": user.email,
        "message":  user.message if user.message else "说点什么吧...",
        "img":user.avater
        }
        formuser=forms.userinfo(form_data)
        print(locals())
        return render(req,"set_user/set_user.html",locals())
    data=forms.userinfo(req.POST,req.FILES)
    print(data.changed_data)
    if data.is_valid():
        user=models.User.objects.filter(id=req.session.get("info").get("id"))
        if data.cleaned_data.get("message")!="说点什么吧...":
            user.update(message=data.cleaned_data.get("message"))
        if data.cleaned_data.get("email")!=user.values()[0].get("email"):
            user.update(email=data.cleaned_data.get("email"))
        if data.cleaned_data.get("sex")!=user.values()[0].get("sex"):
            user.update(sex=data.cleaned_data.get("sex")) 
        print(data.cleaned_data)
        if data.cleaned_data.get("img")!=user.values()[0].get("img"):
            req=data.cleaned_data
            img=req.get("img")
            img_path=os.path.join("APP1","static","img",img.name)
            with open(img_path,"wb+") as f:
                for chunk in img.chunks():
                    f.write(chunk)
            user.update(avater=os.path.join("img",img.name))
    
    return redirect("/user")

def docs(request):
    return render(request, 'help/help_user.html')