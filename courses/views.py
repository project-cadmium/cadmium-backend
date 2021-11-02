from rest_framework import viewsets, permissions

from .models import Course
from .serializers import CourseSerializer


class CourseViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Course.objects.all()
    serializer_class = CourseSerializer
