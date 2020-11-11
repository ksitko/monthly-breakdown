import uuid

from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Event(models.Model):
    uuid = models.UUIDField(primary_key=True, unique=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(
        User, on_delete=models.SET_NULL, related_name="participating_events", null=True, blank=True
    )
    success = models.BooleanField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=False)  # For Testing purposes
