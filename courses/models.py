from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE

from instructors.models import Instructor


class Course(SafeDeleteModel):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.
    _safedelete_policy = HARD_DELETE_NOCASCADE

    instructor_id = models.ForeignKey(
        Instructor, on_delete=models.PROTECT)

    name = models.CharField(max_length=200)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)


class Chapter(SafeDeleteModel):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.
    _safedelete_policy = HARD_DELETE_NOCASCADE

    course_id = models.ForeignKey(
        Course, on_delete=models.PROTECT)

    name = models.CharField(max_length=200)
    description = models.TextField()

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}: {}".format(self.id, self.name)
