from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponseBadRequest
def home(request):
    context={}
    return render(request,'home.html',context)


def register(request):
    form = CreateUserForm()
    context = {'form':form }
    if request.method == 'POST':
        form=CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user=form.cleaned_data.get('username')
            messages.success(request,'Account was created for '+ user)
            return redirect('loginpage')
            
    return render(request,'register.html',context)

def loginpage(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
            
    context={}
    return render(request,'loginpage.html',context) 

