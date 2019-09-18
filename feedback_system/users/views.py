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
   return render(request,'users/Home.html')

def co(request,sem): #co/<int:sem>
    #u=User.objects.get(user_id=request.user.id)
    cid=CourseOutcomes.objects.get(courseid=sem)
    subjects=Subject.objects.filter(courseid=cid)
    content=Content.objects.filter(subid=subjects)
    sl=list(subjects)
    cl=[]
    for s in sl:
        c = Content.objects.filter(subid=s)
        for x in c:
            cl.append(x)


    return render(request,'users\courseoutcome.html',{'subjects':sl,'cl':cl})


def temp(request):
    return render(request,'users/temp.html')



'''
for s in sl:
...     c=Content.objects.filter(subid=s)
...     for x in c:
...             l.append(x)

for s in sl:
...     c=Content.objects.filter(subid=s)
...     cl.append(c)


 for s in sl:
...     print(s)
...     for x in cl[i]:
...             print(x)
...     i=i+1
'''