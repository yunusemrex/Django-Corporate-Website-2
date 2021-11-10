from django.db import models

class Testimionals(models.Model):
    value = models.IntegerField(blank=True, null=True)
    description = models.CharField(max_length=240)
    image = models.ImageField(upload_to="testimionals-images")


    class Meta:
        db_table = 'testimional'
        verbose_name = 'testiminonal'
        verbose_name_plural = 'testimionals'

    
    def __str__(self):
        return self.description