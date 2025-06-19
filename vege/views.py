from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.core.paginator import Paginator

from django.contrib.auth import get_user_model
User = get_user_model()


# Create your views here.
@login_required(login_url='/login/')
def receipe(request):
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')




        print(receipe_name)
        print(receipe_description)
        print(receipe_image)

        Receipe.objects.create(
            reciepe_name=receipe_name,
            reciepe_description=receipe_description,
            reciepe_image=receipe_image
            )
        return redirect ('/receipes/')
    
    queryset=Receipe.objects.all()
    context={
        'receipes':queryset
    }
    return render(request,'receipe.html',context)

def delete_receipe(request,id):
    Receipe.objects.get(id=id).delete()        #or querset= Receipe.objects.get(id=id) querset.delete()
                                                # queryset.delete()
    return redirect('/receipes/')

def update_receipe(request,id):
    queryset=Receipe.objects.get(id=id)
    if request.method=="POST":
        data=request.POST
        receipe_image=request.FILES.get('receipe_image')
        receipe_name=data.get('receipe_name')
        receipe_description=data.get('receipe_description')

        queryset.reciepe_name=receipe_name
        queryset.reciepe_description=receipe_description
        if receipe_image:
            queryset.reciepe_image=receipe_image      # idhr jo reciepe use kr rhaaa voh jo create kri thi voh vaha jo likha hain voh waala hain 
        queryset.save()
        return redirect('/receipes/')
    context={
        'receipe':queryset
    }

    return render(request,'update_receipe.html',context)

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = User.objects.filter(username=username)
        if not user.exists():
            messages.error(request, 'Username does not exist')
            return redirect('/login/')

        user = authenticate(username=username, password=password)

        if not user:
            messages.error(request, 'Invalid Password')
            return redirect('/login/')
        else:
            login(request, user) 
            return redirect('/receipes/')
    
    return render(request, 'login.html')


def register(request):
    if request.method=="POST":
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        username=request.POST.get('Username')
        password=request.POST.get('password')
        
        user=User.objects.filter(username=username)
        if user.exists():
            messages.info(request,'Username already exists')
            return redirect('/register/')
        user=User.objects.create(
            first_name=first_name,
            last_name = last_name,
            username = username
        )
        user.set_password(password)
        user.save()
        messages.info(request,'User Created')
        return redirect('/login/')
    return render(request,'register.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


