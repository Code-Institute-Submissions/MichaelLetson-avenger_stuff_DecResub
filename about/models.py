from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()

    def __str__(self):
        return self.name

class Newsletter(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    address = models.CharField(max_length=80)

    def __str__(self):
        return self.name

class Review(models.Model):
    name = models.CharField(max_length=80)
    email = models.EmailField()
    body = models.TextField()
    created_on = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ["created_on"]

    def __str__(self):
        return f"Review: {self.body} by {self.name}"
