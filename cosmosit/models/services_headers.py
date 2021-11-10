from django.db import models

class ServiceHeaders(models.Model):
    header1 = models.CharField(max_length=60)
    header2 = models.CharField(max_length=80)


    class Meta:
        db_table = 'service_header'
        verbose_name = 'service_header'
        verbose_name_plural = 'service_headers'


    def __str__(self):
        return self.header1
