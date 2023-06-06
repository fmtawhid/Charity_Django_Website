from django.db import models

# Create your models here.
class contact(models.Model):
    name = models.CharField(max_length=100)
    mail = models.EmailField()
    number = models.CharField(max_length=15)
    sms = models.CharField(max_length=300)
    
    def __str__(self):
        return self.name
