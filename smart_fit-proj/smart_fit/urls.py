"""smart_fit URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from src import views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('register/', views.registration, name='auth.registration'),
    path('login/', views.login_user, name='auth.login'),
    path('logout/', views.logout_user, name='auth.logout'),

    path('workouts/', views.workouts_index, name='workouts.index'),
    path('workouts/new', views.workouts_create, name='worksouts.new'),
    path('workouts/<int:workout_id>', views.workouts_read, name='workouts.read'),
    path('workouts/update/<int:workout_id>', views.workouts_update, name='workouts.update'),
    path('workouts/delete/<int:workout_id>', views.workouts_delete, name="workouts.delete"),

    path('workouts/exercises', views.workouts_excercises, name='worksouts.excercises.index'),

    path('', views.home_index , name='home.index'),
]
