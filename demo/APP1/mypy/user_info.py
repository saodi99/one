from django.shortcuts import render,HttpResponse,redirect
from django import forms
from .. import models

class userinfo(forms.Form):    
    # def __init__(self,*args, **kwargs):
    #     super().__init__(*args, **kwargs)
    sort={
             ("male","男"),
             ("female","女"),
             ("未知","保密")
        }

    sex=forms.ChoiceField(label="性别",choices=sort)
    email=forms.EmailField(label="Email")
    message=forms.CharField(label="",max_length=255) 


def get(request,*args):
    uid=request.session.get("info").get("id")
    user=models.User.objects.get(id=uid)
    data=models.Goods.objects.filter(uid=uid)
    form_data = {
    "sex":user.sex,
    "email": user.email,
    "message":  user.message if user.message else "说点什么吧...",
    }
    formuser=userinfo(form_data)
    return render(request,"user/user.html",locals())
def post(request,*args):
    data=userinfo(request.POST,request.POST)
    if data.is_valid():
        user=models.User.objects.filter(id=request.session.get("info").get("id"))
        if data.cleaned_data.get("message")!="说点什么吧...":
            user.update(message=data.cleaned_data.get("message"))
        if data.cleaned_data.get("email")!=user.values()[0].get("email"):
            user.update(email=data.cleaned_data.get("email"))
        if data.cleaned_data.get("sex")!=user.values()[0].get("sex"):
            user.update(sex=data.cleaned_data.get("sex")) 
    return redirect("/user")