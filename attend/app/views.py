from django.shortcuts import render,HttpResponse,redirect
from django.contrib.auth.models import User
from .models import Contact
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def index(request):
    if not request.user.is_authenticated:
        return render(request,'login.html')
    return render(request,'index.html')

def handleSignup(request):
    if request.method == "POST":
        fname=request.POST['fname']
        lname=request.POST['lname']
        username=request.POST['username']
        date=request.POST['date']
        num=request.POST['num']
        gender=request.POST['gender']
        email=request.POST['email']
        pass1=request.POST['pass1']
        pass2=request.POST['pass2']

        if pass1 != pass2:
            messages.warning(request,"PASSWORD DOESN'T MATCH, PLEASE TRY AGAIN")
            return redirect('/signup')
        
        try:
            if User.objects.get(username=username):
                messages.warning(request,"USERNAME EXISTS")
                return redirect('/signup')
        except Exception as identifier:
            pass

        myuser=User.objects.create_user(username,email,pass2)
        myuser.first_name=fname
        myuser.last_name=lname
        myuser.save()
        messages.warning(request,"REGISTRATION COMPLETE")
        return redirect('/login')

    return render(request,'signup.html')

def handleLogin(request):
    if request.method == "POST":
        username=request.POST['username']
        pass1=request.POST['pass1']
        user=authenticate(username=username,password=pass1)
        if user is not None:
            login(request,user)
            messages.info(request,"Login SuccessFull")
            return redirect("/")
        else:
            messages.error(request,"Invalid Credentials")
            return redirect("/login") 


    return render(request,'login.html')

def handleLogout(request):
    logout(request)
    messages.info(request,"LOGOUT SUCCESSFUL")
    return redirect('/login')

def about(request):
    return render(request,'about.html')