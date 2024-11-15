from rest_framework import serializers

from .models import Exercise, TrainingCategory, WorkoutPlan


class TrainingCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = TrainingCategory
        fields = ["id", "name", "user"]
        read_only_fields = ["user"]  # can't be modified

    def validate_name(self, value):
        if TrainingCategory.objects.filter(name=value).exists():
            raise serializers.ValidationError("Category exists.")
        return value

    def create(self, validated_data):
        # automaticly assign logged user
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class ExerciseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exercise
        fields = ["id", "name", "set", "repetitions", "duration", "user"]
        read_only_fields = ["user"]

    def validate_name(self, value):
        if Exercise.objects.filter(name=value).exists():
            raise serializers.ValidationError("Exercise exists.")
        return value

    def create(self, validated_data):
        validated_data["user"] = self.context["request"].user
        return super().create(validated_data)


class WorkoutPlanSerializer(serializers.ModelSerializer):
    exercises = serializers.ListField(child=serializers.CharField(), write_only=True)
    category = serializers.CharField(write_only=True)

    class Meta:
        model = WorkoutPlan
        fields = ["id", "name", "description", "user", "category", "exercises"]
        read_only_fields = ["user"]

    def validate_name(self, value):
        if self.instance:
            if (
                WorkoutPlan.objects.filter(name=value)
                .exclude(id=self.instance.id)
                .exists()
            ):
                raise serializers.ValidationError(
                    "Workout plan with this name already exists."
                )
        else:
            if WorkoutPlan.objects.filter(name=value).exists():
                raise serializers.ValidationError(
                    "Workout plan with this name already exists."
                )
        return value

    def create(self, validated_data):
        exercise_names = validated_data.pop("exercises", [])
        category_name = validated_data.pop("category")

        category, created = TrainingCategory.objects.get_or_create(name=category_name)

        workout_plan = WorkoutPlan.objects.create(category=category, **validated_data)

        exercises = Exercise.objects.filter(name__in=exercise_names)
        workout_plan.exercises.set(exercises)
        return workout_plan

    def update(self, instance, validated_data):
        exercise_names = validated_data.pop("exercises", [])
        category_name = validated_data.pop("category", None)

        if category_name:
            category, created = TrainingCategory.objects.get_or_create(
                name=category_name
            )
            instance.category = category

        instance.name = validated_data.get("name", instance.name)
        instance.description = validated_data.get("description", instance.description)

        if exercise_names:
            exercises = Exercise.objects.filter(name__in=exercise_names)
            instance.exercises.set(exercises)

        instance.save()
        return instance

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation["exercises"] = [
            exercise.name for exercise in instance.exercises.all()
        ]
        representation["category"] = instance.category.name
        return representation
