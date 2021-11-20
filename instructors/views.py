from rest_framework import permissions, viewsets

from .models import Instructor
from .serializers import InstructorSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    permission_classes = (permissions.IsAuthenticated,)
    queryset = Instructor.objects.all()
    serializer_class = InstructorSerializer
    lookup_field = 'user_id'
