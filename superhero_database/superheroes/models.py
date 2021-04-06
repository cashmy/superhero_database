from django.db import models


# Create your models here.
class Superhero(models.Model):
    name = models.CharField(max_length=50)
    alterEgo = models.CharField(max_length=50)
    primaryAbility = models.CharField(max_length=50)
    secondaryAbility = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=150)

    def __str__(self):
        return self.name
