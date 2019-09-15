from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect

'''
def loginView(request):
    u=request.POST['username']
    p=request.POST['password']
    user=authenticate(username=u,password=p)
    if user is not None:
        login(request,user)
        return pass
    return pass

'''


def validate(request):
    u = request.POST['username']
    p = request.POST['password']
    user = authenticate(username=u, password=p)
    if user is not None:
        login(request, user)
        return render(request,'users/temp.html')
    return render(request,'users/Signup.html')

def register(request):
    if request.method=="POST":
        u = request.POST['username']
        p = request.POST['password']
        User.objects.create_user(username=u, password=p)
        return render(request, 'users/temp.html')
    return render(request,'users/Signup.html')

def home(request):
    if request.method == 'POST':
        pass







