from django.shortcuts import redirect, render
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
# Create your views here.

def register_view(request):
    if request.user.is_authenticated:
         return redirect('home')
    try:
        email = request.POST['email']
        username = request.POST['username']
        password = request.POST['password']
        repassword = request.POST['repassword']
        
        if User.objects.filter(email = email).exists():
            return render(request, 'auth/register.html', {"error": "Email already exists!"})
        elif User.objects.filter(username = username).exists():
            return render(request, 'auth/register.html', {"error": "Usernma already exists!"})
        elif password != repassword:
            return render(request, 'auth/register.html', {"error": "Passwords don't match!"})     
        
        user = User.objects.create_user(username = username, email = email, password = password)
        user.save()
        return redirect('login')
            
    except:
        return render(request, 'auth/register.html', {})

def login_view(request):  
    if request.user.is_authenticated:
            return redirect('home')
    
    try:
        username = request.POST['username']
        password = request.POST['password']
        
        if not username or not password:
            return render(request, 'auth/login.html', {"error": "You can't leave username or password blank!"})
        
        user = authenticate(request, username=username, password=password)
        
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return render(request, 'auth/login.html', {"error": "Invalid username or password!"})   
    except:
        return render(request, 'auth/login.html', {})

def logout_view(request):
    logout(request)
    return redirect('home')
