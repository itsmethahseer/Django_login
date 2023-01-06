from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.views.decorators.cache import never_cache

# Create your views here.
@never_cache
def Homepage(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    else:
        return redirect(login_page)

@never_cache
def sign(request):
    if request.user.is_authenticated:
        return render(request, 'homepage.html')
    if request.method=='POST':
        uname =request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1!=pass2:
            return HttpResponse("Your password and conform password are not same")
        else:
            my_user =User.objects.create_user(uname,email,pass1)
            my_user.save()
        # return HttpResponse("User has been created successfully")
            return redirect('login')
        #print(uname,email,pass1,pass2)

    return render(request, 'signup.html')


@never_cache
def login_page(request):
    if request.user.is_authenticated:
        return redirect('homepage')
    if request.method=='POST':
        username=request.POST.get('username')
        password=request.POST.get('pass')
        user=authenticate(request,username=username,password=password)
        if user is not None:
            # request.session['username'] = username

            login(request,user)
            return redirect('homepage')
        else:
            return HttpResponse("username or password is incorrect")
    return render(request, 'index.html')
@never_cache
def Logoutpage(request):
    if request.user.is_authenticated:
        logout(request)
    return redirect('login')
