from django.db import models


class GolfScore(models.Model):
    player_name = models.CharField(max_length=100)
    date = models.DateField()
    course_name = models.CharField(max_length=100)
    hole_1 = models.IntegerField(default=0)
    # Assume continuation up to hole_18
    hole_18 = models.IntegerField(default=0)

    def total_score(self):
        return sum([getattr(self, f'hole_{i}') for i in range(1, 19)])

    def __str__(self):
        return f"{self.player_name} - {self.total_score()} on {self.date}"
