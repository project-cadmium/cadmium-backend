from rest_framework import serializers
from .models import Instructor


class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = (
            'id',
            'user_id',
            'biography',
            'created_at',
            'updated_at',
        )
