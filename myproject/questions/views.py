from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
from django.utils import timezone
#from .forms import CreateUserForm, UserLoginForm, User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseBadRequest, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Question
from .forms import QuestionForm

@login_required(login_url='loginpage')
def home(request):
    ques=Question.objects.all().order_by('date_asked')
    context={'ques':ques}
    return render(request,'home.html',context) 

"""
@login_required(login_url='loginpage')
def addcomment(request,pk):
    event=get_object_or_404(Question,pk=pk) 
    if request.method=="POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.event= event
            comment.user = request.user
            comment.save()
    else:
        form=CommentForm()
    context={'form':form}
    return render(request,'addcomment.html',context)
"""

@login_required(login_url='loginpage')
def addevent(request):
    form=QuestionForm(request.POST or None) 
    if request.method=="POST":
        if form.is_valid():
            que=form.save()
            que.date_asked=timezone.now()
            que.save()
            return redirect('home') 
        else:
            form=QuestionForm() 
    return render(request,'addevent.html',{'form':form })


        

