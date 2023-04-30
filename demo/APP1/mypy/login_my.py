from django.shortcuts import render,HttpResponse,redirect
from .. import forms
from .. import models
def get(request):
    login_form_add = forms.UserForm_add()
    login_form_login=forms.UserForm_login()

    return render(request,"login/login.html",locals())

def post(request):
    login_form_add = forms.UserForm_add()
    login_form_login=forms.UserForm_login()
    data=forms.UserForm_add(request.POST)
    if data.is_valid():        
        uid=models.User.objects.create(name=data.cleaned_data.get("adduser"),email="",).id
        models.Passwrd.objects.create(uid=models.User.objects.get(id=uid),password=data.cleaned_data.get("addpwd"))
        return HttpResponse("注册成功")
    else :
        data=forms.UserForm_login(request.POST)
        if data.is_valid():
            print(data.cleaned_data)
            username=data.cleaned_data.get("loginuser")
            userpwd=data.cleaned_data.get("loginpwd")
            try:
                user=models.User.objects.get(name=username)
            except:
                return render(request,"login/login.html",locals())
            if models.Passwrd.objects.get(uid=user.id).password != userpwd:
                return render(request,"login/login.html",locals())
            else:
                request.session["info"]={"id":user.id,"name":user.name}
                return redirect("/index")
