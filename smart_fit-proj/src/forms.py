import datetime

from django import forms
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm

from .models import Workout


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()
    is_staff = forms.BooleanField(required=False)

    class Meta:
        model = User
        fields = ['username', 'password1', 'password2','first_name','last_name','email', 'is_staff']

class WorkoutForm(ModelForm):
    class Meta:
        model = Workout
        fields = [
            'name', 
            'desc', 
            'scale', 
            
            'ex_1_name', 
            'ex_1_sets',
            'ex_1_reps', 
            'ex_1_desc',
            
            'ex_2_name',
            'ex_2_sets',
            'ex_2_reps',
            'ex_2_desc',

            'ex_3_name',
            'ex_3_sets',
            'ex_3_reps',
            'ex_3_desc'
        ]

    
