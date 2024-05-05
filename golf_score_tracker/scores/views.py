# views.py
from django.shortcuts import render, redirect
from .models import GolfScore


def all_scores(request):
    scores = GolfScore.objects.all()
    return render(request, 'all_scores.html', {'scores': scores})

def add_score(request):
    if request.method == 'POST':
        pass
        new_score = GolfScore(
            player_name=request.POST['player_name'],
            date=request.POST['date'],
            course_name=request.POST['course_name'],
        )
        for hole_number in range(1, 19):
            setattr(new_score, f'hole_{hole_number}', int(request.POST.get(f'hole_{hole_number}', 0)))
        new_score.save()
        return redirect('all_scores')  # Redirect to the score listing page after the form is processed
    return render(request, 'add_score.html')


def home(request):
    return render(request, 'home.html')

