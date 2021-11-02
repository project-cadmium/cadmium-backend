from django.db import models
from safedelete.models import SafeDeleteModel
from safedelete.models import HARD_DELETE_NOCASCADE
from django.contrib.auth import get_user_model


class Instructor(SafeDeleteModel):
    # Objects will be hard-deleted, or soft deleted if other objects would have been deleted too.
    _safedelete_policy = HARD_DELETE_NOCASCADE

    user_id = models.OneToOneField(
        get_user_model(), on_delete=models.PROTECT)
    biography = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}".format(self.id)
