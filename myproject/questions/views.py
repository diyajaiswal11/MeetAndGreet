from django.shortcuts import render
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
#from .forms import CreateUserForm, UserLoginForm, User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
# Create your views here.
from .models import Question

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