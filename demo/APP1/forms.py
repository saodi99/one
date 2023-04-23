from django import forms


class UserForm_add(forms.Form):
    adduser=forms.CharField(label="",max_length=128,widget=forms.TextInput(attrs={"class":"form_input","placeholder":"User"}))
    addpwd=forms.CharField(label="",max_length=256,widget=forms.PasswordInput(attrs={"class":"form_input","placeholder":"Password"}))
class UserForm_login(forms.Form):
    loginuser=forms.CharField(label="",max_length=128,widget=forms.TextInput(attrs={"class":"form_input","placeholder":"User"}))
    loginpwd=forms.CharField(label="",max_length=256,widget=forms.PasswordInput(attrs={"class":"form_input","placeholder":"Password"}))
class imgtest(forms.Form):
    img=forms.ImageField(label="img")