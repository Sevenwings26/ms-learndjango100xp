from django.db import models
from django.urls import reverse


# Create your models here.
class Shelter(models.Model):
    name = models.CharField(max_length=200)
    location = models.CharField(max_length=200)
    def __str__(self):
        return self.name

class Dog(models.Model):
    shelter = models.ForeignKey(Shelter, on_delete=models.PROTECT)
    name = models.CharField(max_length=200)
    description = models.TextField(max_length=200)
    intake_date = models.DateTimeField(auto_now_add=True)

    # TODO: Add get_absolute_url
    def get_absolute_url(self):
        return reverse('dog_detail', kwargs={"pk": self.pk})
    
    def __str__(self):
        return self.name