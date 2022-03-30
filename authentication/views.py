from django.http.response import HttpResponse
from django.shortcuts import render,redirect
from  django.contrib.auth import authenticate,login,logout
from django.contrib import messages
from validate_email import validate_email
from . models import MyUser

# Create your views here.
def register_request(request):
    if request.method == "POST":
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')
        
        if len(password) < 6:
            messages.error(request,'Password should be at least 6 characters')
            return redirect('register')
        
        if password != password2:
            messages.error(request,'Password mismatch')
            return redirect('register')
        
        if not validate_email(email):
            messages.error(request, 'Enter a valid email address')
            return redirect('register')
        
        if not username:
            messages.error(request, 'Username is required')
            return redirect('register')
        
        if MyUser.objects.filter(username=username).exists():
            messages.error(request,  'Username is taken, choose another one')
            return redirect('register')
        
        if MyUser.objects.filter(email=email).exists():
            messages.error(request,'Email is taken, choose another one')
        try:
            user = MyUser.objects.create(
                email =email,
                username = username,
                password =password,
                )
            messages.success(request,'Registered successfully')
            return redirect('login')
        except Exception as e:
            print (e)
            messages.error(request,e)        
    return render(request,'accounts/register.html')

def login_request(request):
    
    user=''
    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        
        user = MyUser.objects.get(email=username)
        if user.password == password:
            try:
                return redirect('post')
            except Exception as e:
                print(e)
                return redirect('post')
        if not user:
            messages.error(request, 'Invalid credentials, try again')
            return redirect('login')
    return render(request, 'accounts/login.html')
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login')