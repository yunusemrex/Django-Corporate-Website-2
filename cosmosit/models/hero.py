from django.db import models 

class Hero(models.Model):
    hero1 = models.CharField(max_length=250)
    h_service = models.CharField(max_length=90)


    class Meta:
        db_table = 'hero'
        verbose_name = 'hero'
        verbose_name_plural = 'heros'
        

    def __str__(self):
        return self.hero1

