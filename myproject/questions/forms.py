from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    class Meta:   #tells which model to be used
        model=Question 
        fields=['text']