from django.db import models

class Score(models.Model):
    player_name = models.CharField(max_length=100)
    date = models.DateField()
    score = models.IntegerField()
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.player_name} - {self.score} on {self.date}"
