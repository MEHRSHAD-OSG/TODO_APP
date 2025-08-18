from rest_framework import serializers
from todo.models import Task
from rest_framework.exceptions import ValidationError


class TaskSerializer(serializers.ModelSerializer):
    user = serializers.SlugRelatedField(read_only=True, slug_field='email')
    class Meta:
        model = Task
        exclude = ("created_date",)

    def validate(self, attrs):
        forbidden_fields = ["id", "user", "created_date", "updated_date"]
        for fields in forbidden_fields:
            if fields in self.initial_data:
                raise ValidationError(f"You can't fill the '{fields}' field manually.")
        return attrs
