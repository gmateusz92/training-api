from django.contrib import admin
from .models import Exercise, WorkoutPlan, TrainingCategory

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(TrainingCategory)
