from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import CourseOutcomes,Subject,Answers,Content
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
        return render(request,'users/Home.html')
    return render(request,'users/Signup.html')

def register(request):
    if request.method=="POST":
        u = request.POST['username']
        p = request.POST['password']
        User.objects.create_user(username=u, password=p)
        return render(request, 'users/Login.html')
    return render(request,'users/Signup.html')

def home(request):
    if request.method == 'POST':
        pass

def co(request,sem): #co/<int:sem>
    #u=User.objects.get(user_id=request.user.id)
    cid=CourseOutcomes.objects.get(courseid=sem)
    subjects=Subject.objects.filter(courseid=cid)
    content=Content.objects.filter(subid=subjects)
    return render(request,'users\courseoutcome.html',{'subjects':subjects})


def temp(request):
    return render(request,'users/temp.html')



