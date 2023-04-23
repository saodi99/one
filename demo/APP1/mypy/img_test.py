from django.shortcuts import render,HttpResponse,redirect
from .. import forms
from .. import models
def get(req):
    imgtest=forms.imgtest()
    print(locals())
    return render(req,"user/user_2.html",{"imgtest":imgtest})
def post(req):
    imgtest=forms.imgtest()
    print(locals())
    return render(req,"user/user_2.html",locals())
