from rest_framework import viewsets, permissions, filters
from filters.mixins import (
    FiltersMixin,
)

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(FiltersMixin, viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer

    filter_backends = {filters.OrderingFilter, }
    filter_mappings = {
        'instructor_id': 'instructor_id'
    }
