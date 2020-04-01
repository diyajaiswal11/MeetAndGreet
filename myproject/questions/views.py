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

@login_required(login_url='loginpage')
def attendevent(request,pk):
    event=get_object_or_404(Question,pk=pk)
    return render(request,'attendevent.html',{'event':event})


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

"""
@login_required(login_url='loginpage')
def attend_event(request,pk):
    event = get_object_or_404(Question, pk=pk)
    attendee = User.objects.get(username=request.user)
    event.attendees.add(attendee)
    #create_action(attendee, 'is attending', event)
    messages.success(request, 'You are now attending {0}'.format(event.name))
    return redirect('attendevent.html')


@login_required(login_url='loginpage')
def not_attend_event(request, pk):
    event = get_object_or_404(Question, pk=pk)
    attendee = User.objects.get(username=request.user)
    event.attendees.remove(attendee)
    #create_action(attendee, 'no longer attending', event)
    messages.success(request, 'You are no longer attending {0}'.format(event.name))
    return redirect('attendevent.html')
"""


