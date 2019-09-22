from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.models import User
from django.shortcuts import render, redirect
from .models import CourseOutcomes,Subject,Answers,Content,questions
from .form import feedbackform
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required

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


l=[]
def validate(request):
    global l
    l=[]
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
        user=User.objects.create_user(username=u, password=p)
        login(request,user)
        return render(request, 'users/Login.html')
    return render(request,'users/Signup.html')

@login_required
def home(request):
   return render(request,'users/Home.html')

@login_required
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


    return render(request,'users\courseoutcome.html',{'subjects':sl,'cl':cl,'cid':cid})

@login_required
def feedback_save(request,qid):
    #if request.method == "POST":
        a = request.GET['ans']
        ques=questions.objects.get(pk=qid)
        cid=ques.courseid
        ansobj = Answers(answer=a,courseid=cid,questionid=ques)
        ansobj.save()
        return feedback_create_view(request,ques,cid)
def temp(request):
    return render(request,'users/temp.html')





@login_required
def temp(request):
    return render(request,'users/temp.html')


def donesubmitting(request):
    global l
    l=[]
    return logoutview(request)

def logoutview(request):
    logout(request)
    return render(request,'users/Login.html')

@login_required
def feedback_create_view(request,ques=None,cid=None):
    '''
    form=feedbackform(request.POST or None)

    if form.is_valid():
        form.save()
    '''
    a=CourseOutcomes.objects.all()
    if cid in a:
        c=cid
    else:
        c= CourseOutcomes.objects.get(courseid=cid)
    q = questions.objects.filter(courseid=c)

    if ques != None:
     #   l[ques]=True
        l.append(ques)
    context={
        "q" : q,
        'l':l,
    }
    return render(request,"users/feedback.html",context)




@login_required
def add_answer_view(request):
    temp =  request.GET
    print(list(User.objects.all()))
    #Answers(answer = '1',courseid = CourseOutcomes(),questionid = questions()).save()
    return home(request)

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