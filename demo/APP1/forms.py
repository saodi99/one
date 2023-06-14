from django import forms

    

    


class UserForm_add(forms.Form):
    adduser=forms.CharField(label="",max_length=128,widget=forms.TextInput(attrs={"placeholder":"用户名"}))
    addpwd=forms.CharField(label="",max_length=256,widget=forms.PasswordInput(attrs={"placeholder":"密码"}))
class UserForm_login(forms.Form):
    loginuser=forms.CharField(label="",max_length=128,widget=forms.TextInput(attrs={"placeholder":"用户名"}))
    loginpwd=forms.CharField(label="",max_length=256,widget=forms.PasswordInput(attrs={"placeholder":"密码"}))






class imgtest(forms.Form):

    img=forms.ImageField(label="img")
class goods(forms.Form):
        sort={
             (1,"电器"),
             (2,"书籍"),
        }
        Goods_name=forms.CharField(label="商品名",max_length=128)
        Goods_level=forms.IntegerField(label="成色")
        Goods_remark=forms.CharField(label="商品描述",max_length=255)
        Goods_price=forms.DecimalField(label="商品价钱",decimal_places=3)
        Goods_sort=forms.ChoiceField (label="商品类别",choices=sort)
        Goods_coumt=forms.IntegerField(label="数量")
        Goods_img=forms.ImageField(label="img")
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
    img=forms.ImageField(label="img")