import os
import json

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.conf import settings

from .forms import UserRegisterForm, WorkoutForm
from .models import Workout

with open(os.path.join(settings.BASE_DIR, 'src', 'static', 'SmartFit', 'js', 'exercises.json')) as json_file:
    EXERCISES = json.load(json_file)

def registration(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            user = authenticate(request, username=request.POST['username'], password=request.POST['password1'])
            login(request, user)
            return redirect('home.index')
    else:
        form = UserRegisterForm()
    return render(request, 'auth/registration.html', {'form': form})

def login_user(request):
    if request.method == 'POST':
        user = authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user is None:
            return redirect('auth.login')
        else:
            login(request, user)
            return redirect('home.index')
    
    return render(request, 'auth/login.html')

def logout_user(request):
    logout(request)
    return redirect('home.index')

def workouts_index(request):
    _workout = Workout.objects.all().order_by('-scale')
    return render(request, 'workouts/index.html', {'workouts': _workout})

@login_required
def workouts_create(request):
    if request.method == 'POST':
        _form = WorkoutForm(request.POST)
        if _form.is_valid():
            _form.save()
            return redirect('home.index')
        else:
            return render(request, 'workouts/new.html', {'form': _form, 'errMsg': 'not valid form'})

    else:
        _form = WorkoutForm()
    return render(request, 'workouts/new.html', {'form': _form})

@login_required
def workouts_read(request, workout_id):
    _workout = get_object_or_404(Workout, pk=workout_id)
    exercise1 = {'name':_workout.ex_1_name,'sets': _workout.ex_1_sets, 'reps':_workout.ex_1_reps,'desc': _workout.ex_1_desc}
    exercise2 = {'name':_workout.ex_2_name,'sets': _workout.ex_2_sets,'reps':_workout.ex_2_reps,'desc': _workout.ex_2_desc}
    exercise3 = {'name':_workout.ex_3_name,'sets': _workout.ex_3_sets,'reps':_workout.ex_3_reps,'desc': _workout.ex_3_desc}
    exList = [exercise1, exercise2, exercise3]
    return render(request, 'workouts/show.html', {'workout': _workout, 'list':exList})

@login_required
def workouts_update(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    form = WorkoutForm(request.POST or None, instance=workout)
    
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('workouts.read', workout_id=workout.id)
        
    return render(request, 'workouts/new.html', {'form': form, 'exercises': EXERCISES})

@login_required
def workouts_delete(request, workout_id):
    workout = get_object_or_404(Workout, pk=workout_id)
    if request.method == 'POST':
        workout.delete()
        return redirect('workouts.index')

    return render(request, 'home/index.html')

def workouts_excercises(request):
    return JsonResponse(EXERCISES, safe=False)

def home_index(request):
    _workout = Workout.objects.all().order_by('-scale')[:4]
    return render(request, 'home/index.html', {'workouts': _workout})