from django.db import models

class About(models.Model):
    header = models.CharField(max_length=230)
    content = models.CharField(max_length=200)
    image = models.ImageField(upload_to='section-images')

    class Meta:
        db_table = 'about'
        verbose_name = 'about'
    
    def __str__(self):
        return self.header