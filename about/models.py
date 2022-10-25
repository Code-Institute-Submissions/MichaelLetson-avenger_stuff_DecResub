from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name
