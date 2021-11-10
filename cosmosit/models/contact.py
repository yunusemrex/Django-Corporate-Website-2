from django.db import models


class Contact(models.Model):
    email =  models.EmailField(max_length=50, blank=False, null=False)
    full_name = models.CharField(max_length=150)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_date = models.DateTimeField(auto_now_add=True) 


    class Meta:
        db_table = 'contact'
        verbose_name = 'contact'
        verbose_name_plural = 'contact'
        

    def __str__(self):
        return self.email