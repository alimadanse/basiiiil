
from django.db import models

# Create your models here.
class Tour(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField(null=True, blank=True)
    photo = models.ImageField(upload_to='tour_photos')
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title