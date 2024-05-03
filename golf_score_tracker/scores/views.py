from django.shortcuts import render
from .models import Score

def all_scores(request):
    scores = Score.objects.all()
    return render(request, 'scores/all_scores.html', {'scores': scores})

def add_score(request):
    if request.method == 'POST':
        new_score = Score(
            player_name=request.POST['player_name'],
            date=request.POST['date'],
            score=request.POST['score'],
            course_name=request.POST['course_name']
        )
        new_score.save()
        return redirect('all_scores')
    return render(request, 'scores/add_score.html')
