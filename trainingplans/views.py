from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from .models import WorkoutPlan, Exercise, TrainingCategory
from .serializers import WorkoutPlanSerializer, ExerciseSerializer, TrainingCategorySerializer

class ExerciseList(generics.ListAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

class ExerciseCreate(generics.CreateAPIView):
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)  # current user

class ExerciseDetail(generics.RetrieveUpdateDestroyAPIView): # get, put, delete
    queryset = Exercise.objects.all()
    serializer_class = ExerciseSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class CategoryList(generics.ListAPIView):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer
    permission_classes = [IsAuthenticated]

class CategoryCreate(generics.CreateAPIView):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class CategoryDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = TrainingCategory.objects.all()
    serializer_class = TrainingCategorySerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]

class WorkoutPlanListView(generics.ListAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]

class WorkoutPlanCreate(generics.CreateAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        serializer.save(user=self.request.user)

class WorokoutPlanDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = WorkoutPlan.objects.all()
    serializer_class = WorkoutPlanSerializer
    lookup_field = 'id'
    permission_classes = [IsAuthenticated]  