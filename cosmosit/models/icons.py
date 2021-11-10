from django.db import models

class Icons(models.Model):
    section = models.CharField(max_length=100)
    icon = models.ImageField(upload_to='icons')