"""demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from APP1 import views
urlpatterns = [
    path("",views.index),
    path("admin/", admin.site.urls),
    path("login/",views.login),
    path("index",views.index),
    path("index/<int:num>",views.index),
    path("user",views.user_page),
    path("submit",views.submit),
    path("cart",views.cart),
    path("wallet",views.wallet),
    path("exit",views.exit),
    path("user/set",views.user_set),
    path("test/<int:i>",views.test),
    path("user/<int:uid>",views.show),
    path("qr",views.qr),
    path("img/<str:str>",views.img),
    path('docs', views.docs, name='docs'),
    path("set",views.set)
]
