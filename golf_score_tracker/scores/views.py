from django.shortcuts import render, redirect
from .models import GolfScore

def all_scores(request):
    scores = GolfScore.objects.all()
    return render(request, 'scores/all_scores.html', {'scores': scores})

def add_score(request):
    if request.method == 'POST':
        new_score = GolfScore(
            player_name=request.POST['player_name'],
            date=request.POST['date'],
            course_name=request.POST['course_name'],
            # Add each hole's score from form data
            hole_1=request.POST['hole_1'],
            # Assume continuation up to hole_18
            hole_18=request.POST['hole_18'],
        )
        new_score.save()
        return redirect('all_scores')
    return render(request, 'scores/add_score.html')


def home(request):
    return render(request, 'home.html')


