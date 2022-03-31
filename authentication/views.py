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
            user = MyUser.objects.create_user(username=username, email=email)
            user.set_password(password)
            user.save()
            messages.success(request,'Registered successfully')
            return redirect('login')
        except Exception as e:
            print (e)
            messages.error(request,e)        
    return render(request,'accounts/register.html')

def login_request(request):

    if request.method == "POST":
        username = request.POST.get('email')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            messages.info(request, f"You are now logged in as {username}.")
            return redirect('post')
        else:
            messages.error(request,"Invalid username or password.")
        # user = MyUser.objects.get(email=username)
        # if user.password == password:
        #     try:
        #         return redirect('post')
        #     except Exception as e:
        #         print(e)
        #         return redirect('post')
    return render(request, 'accounts/login.html')
def logout_request(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect('login')