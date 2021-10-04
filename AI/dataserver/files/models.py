from django.utils import timezone

from django.db import models
from django.contrib.auth.models import User

class Files(models.Model):
    file = models.FileField()
    upload_at = models.DateTimeField(default=timezone.now)
    

# Create your models here.