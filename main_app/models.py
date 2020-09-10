from django.db import models
from django.urls import reverse

# Create your models here.

class Supply(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("supplies_detail", kwargs={ "supply_id": self.id })
    
    
    class Orchid(models.Model):
    name = models.CharField(max_length = 100)
    genus = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    age = models.IntegerField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'orchid_id': self.id })
    
