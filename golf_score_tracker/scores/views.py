# views.py
from django.shortcuts import render, redirect
from .models import GolfScore


def all_scores(request):
    scores = GolfScore.objects.all()
    return render(request, 'all_scores.html', {'scores': scores})

def add_score(request):
    if request.method == 'POST':
        new_score = GolfScore(
            player_name=request.POST['player_name'],
            date=request.POST['date'],
            course_name=request.POST['course_name'],
        )
        for hole_number in range(1, 19):
            hole_score = request.POST.get(f'hole_{hole_number}', 0)
            setattr(new_score, f'hole_{hole_number}', int(hole_score))
        new_score.save()
        return redirect('scores:all_scores')
    else:
        context = {'holes_range': range(1, 19)}  # Add this line
        return render(request, 'add_score.html', context)


def home(request):
    return render(request, 'home.html')

