from django.shortcuts import render , HttpResponse , redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from .models import *


@login_required(login_url="login/")
def homepage(request):
    notes = {1:'Hello', 2: 'careful'}
    return render(request,"templates/homepage.html",{'notes':notes})

def login(request):
    if request.method == "GET":
        return render(request,"templates/login.html")
    elif request.method == "POST":
        username = request.POST["username"]
        password = request.POST ["password"]
        user = authenticate(request, username=username,password=password)
        if user:
            print("ok")
            auth_login(request,user)
            return redirect("homepage")
        else :
            pass
            


    else:
        return HttpResponse(status=404)
        


@login_required(login_url="login/")
def add_request(request):
   request1 = {'request':'1'}
   return render(request,'templates/add_request.html',request1)


@login_required(login_url="login/")
def contact_us(request):
   return render(request,'templates/contact_us.html')
    
