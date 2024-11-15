from django.conf import settings
from django.db import models


class Exercise(models.Model):
    name = models.CharField(max_length=255)
    set = models.IntegerField(null=True)
    repetitions = models.IntegerField()
    duration = models.DurationField()
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class TrainingCategory(models.Model):
    name = models.CharField(max_length=100)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    def __str__(self):
        return self.name


class WorkoutPlan(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    category = models.ForeignKey(
        TrainingCategory, on_delete=models.CASCADE, related_name="workout_plans"
    )
    exercises = models.ManyToManyField(
        Exercise, related_name="workout_plans"
    )  # Wiele ćwiczeń

    def __str__(self):
        return self.name
