from django.urls import path
from . import views

urlpatterns = [
    path('scores/', views.all_scores, name='all_scores'),
    path('add/', views.add_score, name='add_score'),
]
