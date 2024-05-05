# scores/urls.py
from django.urls import path
from . import views


app_name = 'scores'  # Define the application namespace

urlpatterns = [
    path('', views.all_scores, name='all_scores'),
    path('add/', views.add_score, name='add_score'),
]
