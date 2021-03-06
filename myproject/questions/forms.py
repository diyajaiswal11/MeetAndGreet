from django import forms
from .models import Question


class QuestionForm(forms.ModelForm):
    text = forms.CharField(widget=forms.TextInput(attrs={'class':'xyz'}),)
    class Meta:   #tells which model to be used
        model=Question 
        fields=['text'] 
"""

class CommentForm(forms.ModelForm):
    class Meta:
        model=Comment
        fields=['content']
"""