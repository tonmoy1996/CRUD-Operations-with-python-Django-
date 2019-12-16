"""EMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path,include
from EmpApp import views

urlpatterns = [

    path('admin/', admin.site.urls),
    path('check/',views.check,name='check'),
    path('emp/',include('EmpApp.urls')),
    path('',views.index,name='index'),
    path('login/',views.login,name='login'),
    path('login/signin/',views.singin,name='singin'),
    path('show/',views.show,name='show'),
    path('user/',views.user,name='user'),
    path('profile/',views.profile,name='profile'),
    path('logout/',views.user_logout,name='user_logout'),
    # path('edit/<int:id>', views.edit),
    # path('update/<int:id>', views.update),
    # path('delete/<int:id>', views.destroy),
]
