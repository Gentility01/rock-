from django.db import models
import datetime

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length= 30)
    phone = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    message = models.TextField()
    date = models.DateTimeField(auto_now_add = True)

    class meta:
        verbose_name_plural = 'Contacts'
        db_table = 'Contacts'

    def __str__(self):
        return self.name + ' ' + self.phone
        
