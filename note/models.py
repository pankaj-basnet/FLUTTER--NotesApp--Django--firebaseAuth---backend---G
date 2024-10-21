from django.db import models
from django.utils import timezone

# .......................................................

import uuid

from django.conf import settings

from useraccount.models import User

# Create your models here.
# .......................................................

class Note(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    
    user_id = models.ForeignKey(User, related_name='notes', on_delete=models.CASCADE)
    text = models.TextField()
    is_synced_with_cloud = models.BooleanField()

    #
    created_at = models.DateTimeField(auto_now_add=True)
    # created_at = models.DateTimeField(default = timezone.now) #  migrations done 141021
    updated_at = models.DateTimeField(auto_now=True)

    # def __repr__(self) -> str:
    #     return f'Note: {self.text} ooo.'

    def __str__(self) -> str:
        return f"Note: {self.text[:15]} {self.created_at} ooo."

    
# .......................................................
# .......................................................
# .......................................................