# scores/urls.py
from django.urls import path
from . import views

app_name = 'scores'

urlpatterns = [
    path('', views.home, name='home'),
    path('add_score/', views.add_score, name='add_score'),
    path('all_scores/', views.all_scores, name='all_scores'),
]
