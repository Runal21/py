from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def home(request):
    return render(request,"home/home.html")

def about(request):
    return  render(request,"home/about.html")  

def contact(request):
    return render(request,'home/contact.html')

def registerpage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        email=request.POST.get('email')
        password=request.POST.get('password')
        
        user =User.objects.filter(username=username)
        if user.exists():
            return HttpResponse("Username or Email is already in use.")
    
        user =  User.objects.create(username=username,first_name=first_name,last_name=last_name,email=email)
        user.set_password(password)
        user.save()
    return render(request,'home/register.html')
    
def loginpage(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user =authenticate(username=username,password=password)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")
    return render (request,'home/login.html')

def logoutpage(request):
    logout(request)
    return redirect('login')
