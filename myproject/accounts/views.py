from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
# Create your views here.
from .forms import CreateUserForm, UserLoginForm, User, UserProfileForm
from django.contrib import messages
from django.contrib.auth import authenticate, login , logout
from django.http import HttpResponseBadRequest
from django.contrib.auth.decorators import login_required
from .models import Profile

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

@login_required(login_url='loginpage')
def profile(request):
    return render(request,'profile.html')

@login_required(login_url='loginpage')
def editprofile(request):
    try:
        profile=request.user.profile
    except Profile.DoesNotExist:
        profile = Profile.objects.create(user=request.user)
    
    #form=UserProfileForm(instance=userprofile)
    if request.method=="POST":
        form=UserProfileForm(request.POST,request.FILES,instance=profile)
        if form.is_valid():
            form.save()
    else:
        form=UserProfileForm(instance=profile)
    context={'form':form }
    return render(request,'editprofile.html',context)