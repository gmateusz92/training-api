from django.urls import path

from .views import (CategoryCreate, CategoryDetail, CategoryList,
                    ExerciseCreate, ExerciseDetail, ExerciseList,
                    WorkoutPlanCreate, WorkoutPlanListView, WorokoutPlanDetail)

urlpatterns = [
    # exercies
    path("exercises/", ExerciseList.as_view(), name="exercises-list"),
    path("add-exercise/", ExerciseCreate.as_view(), name="execrise-create"),
    path("exercises/<int:id>/", ExerciseDetail.as_view(), name="exercise-detail"),
    # categories
    path("categories/", CategoryList.as_view(), name="categories-list"),
    path("add-category/", CategoryCreate.as_view(), name="training-category-create"),
    path("categories/<int:id>/", CategoryDetail.as_view(), name="categories-detail"),
    # path('categories/', TrainingCategoryListCreateView.as_view(), name='training-category-list-create'),
    path("workout-plans/", WorkoutPlanListView.as_view(), name="workout-plan-list"),
    path("add-workout-plan/", WorkoutPlanCreate.as_view(), name="workout-plan-create"),
    path(
        "workout-plans/<int:id>/",
        WorokoutPlanDetail.as_view(),
        name="workoutplan-detail",
    ),
]
