from django.db import models
from django.contrib.auth import get_user_model


class Instructor(models.Model):
    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    biography = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.id)
