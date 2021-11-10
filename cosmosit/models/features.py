from django.db import models

class Features(models.Model):
    image = models.ImageField(upload_to='section-images')
    content = models.CharField(max_length=200)