from django.shortcuts import render,redirect
from django.urls import reverse
from .forms import *
from django.contrib.auth import login,logout,authenticate

# Create your views here.
def login_def(request):
    next = request.GET.get('next')
    form = FormForLogin(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username = username, password = password)
        login(request,user)
        if next:
            return redirect(next)
        return redirect(reverse('projects_list_url'))
    return render(request,'accounts/login.html',{'form':form})


def logout_def(request):
    next = request.GET.get('next')
    logout(request)
    return redirect(next)


def signup_def(request):
    next = request.GET.get('next')
    form = FormForSignup(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username = user.username, password= password)
        login(request,new_user)
        if next:
            return redirect(next)
        return redirect(reverse('projects_list_url'))
    return render(request,'accounts/signup.html',{'form':form})

def password_change(request):
    form = FormForChangePassword(request.POST or None,user=request.user)
    if form.is_valid():
        password = form.cleaned_data.get('new_password2')
        user = User.objects.get(username=request.user)
        user.set_password(password)
        user.save()
        logout(request)
        return redirect(reverse('login_url'))
    return render(request,'accounts/password_change.html',{'form':form})
