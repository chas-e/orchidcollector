from django.db import models
from django.urls import reverse

# Create your models here.

FERTILIZER = (
    ('W', 'Just Water'),
    ('O', 'Water with Orchid Pro'),
    ('M', 'Water with Mag Pro Bloombooster'),
    ('C', 'Water with CalMag')
)

class Supply(models.Model):
    name = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse("supply_detail", kwargs={ "pk": self.id })
    
    
class Orchid(models.Model):
    name = models.CharField(max_length = 100)
    genus = models.CharField(max_length = 100)
    description = models.TextField(max_length = 250)
    age = models.IntegerField()
    supplies = models.ManyToManyField(Supply)

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('detail', kwargs={ 'orchid_id': self.id })
    

class Watering(models.Model):
    date = models.DateField('watering date')
    fertilizer = models.CharField(
        max_length=1,
        choices=FERTILIZER,
        default=FERTILIZER[0][0]
        )
    # create an orchid FK
    orchid = models.ForeignKey(Orchid, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.get_fertilizer_display()} on {self.date}'
