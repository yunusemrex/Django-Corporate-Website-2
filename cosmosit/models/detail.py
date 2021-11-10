from django.db import models

class Detail(models.Model):
    name = models.CharField(max_length=200)
    title = models.CharField(max_length=250)
    detail = models.CharField(max_length=300)


    class Meta:
        db_table = 'detail'
        verbose_name = 'detail'
        verbose_name_plural = 'details'
        

    def __str__(self):
        return self.name