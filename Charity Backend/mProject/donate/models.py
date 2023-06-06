from django.db import models

# Create your models here.
class donarList(models.Model):
    name = models.CharField(max_length=200)
    mail = models.EmailField()
    number = models.CharField(max_length=11)

    def __str__(self):
        return self.name
    