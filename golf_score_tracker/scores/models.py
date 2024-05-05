from django.db import models

class GolfScore(models.Model):
    player_name = models.CharField(max_length=100)
    date = models.DateField()
    course_name = models.CharField(max_length=100)
    # Fields for each hole's score, initialized to zero
    hole_1 = models.IntegerField(default=0)
    hole_2 = models.IntegerField(default=0)
    hole_3 = models.IntegerField(default=0)
    hole_4 = models.IntegerField(default=0)
    hole_5 = models.IntegerField(default=0)
    hole_6 = models.IntegerField(default=0)
    hole_7 = models.IntegerField(default=0)
    hole_8 = models.IntegerField(default=0)
    hole_9 = models.IntegerField(default=0)
    hole_10 = models.IntegerField(default=0)
    hole_11 = models.IntegerField(default=0)
    hole_12 = models.IntegerField(default=0)
    hole_13 = models.IntegerField(default=0)
    hole_14 = models.IntegerField(default=0)
    hole_15 = models.IntegerField(default=0)
    hole_16 = models.IntegerField(default=0)
    hole_17 = models.IntegerField(default=0)
    hole_18 = models.IntegerField(default=0)

    def total_score(self):
        # Sum up all the scores from hole 1 to hole 18
        return sum(getattr(self, f'hole_{i}') for i in range(1, 19))

    def __str__(self):
        # String representation including player name, total score, and date
        return f"{self.player_name} - {self.total_score()} on {self.date.strftime('%Y-%m-%d')}"



