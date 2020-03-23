from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
#from .forms import CreateUserForm, UserLoginForm, User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required


def front(request):
    context={}
    return render(request,'front.html',context)