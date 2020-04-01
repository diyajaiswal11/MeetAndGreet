"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path, include
from . import views
urlpatterns = [
    path('home/',views.home,name='home'),
    #path('question/<int:pk>/',views.answers,name="answers"),
    path('addevent/',views.addevent,name='addevent'),
    path('event/<int:pk>/',views.attendevent,name='attendevent'),
    path('event/<int:pk>/',views.attendevent,name='attendevent'),
   # path('event/<int:pk>/attend',views.attend_event,name='attend_event'),
    #path('event/<int:pk>/not_attend',views.not_attend_event,name='not_attend_event'),
]