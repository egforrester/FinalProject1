from django.urls import path
from . import views

urlpatterns = [
    path('', views.all_scores, name='all_scores'),  # Accessible at '/scores/'
    path('add/', views.add_score, name='add_score'),  # Accessible at '/scores/add/'
]
