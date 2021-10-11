from django.utils import timezone
from django.db import models
from django.contrib.auth.models import User
from django.conf import settings


import os


class File(models.Model):
    file = models.FileField()
    upload_at = models.DateTimeField(default=timezone.now)
    
    def delete(self, *args, **kargs):
        if self.file:
            os.remove(os.path.join(settings.MEDIA_ROOT, self.file.path))
        super(File, self).delete(*args, **kargs)
        
    def __str__(self):
        return str(self.file.name)
        

class TrainedModel(models.Model):
    version = models.AutoField(primary_key=True)
    file = models.FileField()
    result = models.FileField()
    create_at = models.DateTimeField(default=timezone.now)
    matrix = models.FloatField()
    
    def delete(self, *args, **kargs):
        if self.file:   os.remove(os.path.join(settings.MEDIA_ROOT, self.file.path))
        if self.result: os.remove(os.path.join(settings.MEDIA_ROOT, self.result.path))
        super(TrainedModel, self).delete(*args, **kargs)
    
    def __str__(self):
        return str(self.file.name) + '_' + str(self.version)
