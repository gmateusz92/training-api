from django.contrib import admin

from .models import Exercise, TrainingCategory, WorkoutPlan

admin.site.register(Exercise)
admin.site.register(WorkoutPlan)
admin.site.register(TrainingCategory)
