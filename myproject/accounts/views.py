from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm, UserLoginForm, User
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required





def register(request):
    user=request.user
    if user.is_authenticated:
        return redirect('home') 
    else:
        if request.method == 'POST':
            form=CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user=form.cleaned_data.get('username')
                messages.success(request,'Account was created for '+ user)
                return redirect('loginpage')
        else:
            form=CreateUserForm()    
        context = {'form':form }    
        return render(request,'register.html',context)

def loginpage(request):
    user = request.user
    if user.is_authenticated:
        return redirect('home') 
    else:
        next = request.GET.get('next')
        form = UserLoginForm(request.POST or None)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            
            login(request, user)
            if next:
                return redirect(next)
            return redirect('home')
        
        context = {
            'form': form,
        }
        return render(request, 'loginpage.html', context)

def logoutpage(request):
    logout(request)
    return redirect('front')



"""def loginpage(request):
    if request.method == "POST":
        username=request.POST.get('username')
        password=request.POST.get('password')

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home') 
            
    context={}
    return render(request,'loginpage.html',context) 
"""
