from django.db import models

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

    
# .......................................................
# .......................................................
# .......................................................