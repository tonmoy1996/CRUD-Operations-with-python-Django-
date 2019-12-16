from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from EmpApp.forms import LoginForm, UserForm
from . import forms
from EmpApp.models import Login

# from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate,login,logout
from django.urls import reverse
# Create your views here.

def index(request):
    # return HttpResponse("Hello World")
    return render(request,'userlogin.html')



# @login_required
def user_logout(request):

    logout(request)
    return HttpResponseRedirect(reverse('index'))



def check(request):
    if request.method=="POST":
        username=request.POST.get("username")
        password=request.POST.get('password')
        user=authenticate(username=username,password=password)
        if user:

            if user.is_active:
                login(request)
                return HttpResponseRedirect(reverse("profile"))
            else:
                return HttpResponse("User Is Not Valid!!!")
        else:
            return HttpResponse("invalid User Login")
    else:
        return render(request,'index/',name='index')


def user(request):
    user=UserForm()

    return render(request,'user.html',{'user':user})





def profile(request):

    # return HttpResponse("Welcome Mr. ...")
    return render(request,'profile.html')


def login(request):
    form=LoginForm()

    return render(request,'login.html',{'form':form})

# class singin(request):
#
#     if request.method=="POST":
#         form=LoginForm(request.POST)
#         if form.is_valid():
#             try:
#                 form.save()
#             except:
#                 pass
#
#     else:
#         form = LoginForm()
#     return render(request,'login.html',{'form':form})




def singin(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        print(request.POST)
        if form.is_valid():
            try:
                form.save()
                return HttpResponseRedirect(reverse('show'))
            except:
                pass
    else:
        form = LoginForm()
    return render(request,'login.html',{'form':form})


def show(request):
    user=Login.objects.all()

    return render(request,'show.html',{'user':user})
