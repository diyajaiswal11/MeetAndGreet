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
    que=Question.objects.all().order_by('date_asked')
    context={'que':que}
    return render(request,'home.html',context) 

@login_required(login_url='loginpage')
def answers(request,pk):
    ans=get_object_or_404(Question,pk=pk) 
    context={'ans':ans}
    return render(request,'answers.html',context)

@login_required(login_url='loginpage')
def addevent(request):
    form=QuestionForm(request.POST or None) 
    if request.method=="POST":
        if form.is_valid():
            que=form.save()
            que.date_asked=timezone.now()
            que.save()
            return redirect('home') 
    return render(request,'addevent.html',{'form':form })
















"""@login_required(login_url='loginpage')
def upvotes(request,pk):
    que=Question.objects.get(pk=request.POST['question']) 
    que.upvotes+=1 
    que.save()
    return render(request,'home.html',{'que':que}) 
        """