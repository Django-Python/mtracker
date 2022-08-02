from django.db import models

class Feedback(models.Model):
    rating = models.CharField(max_length=5)
    feedback = models.CharField(max_length=500, blank=True, null=True)
    

# Create your models here.
