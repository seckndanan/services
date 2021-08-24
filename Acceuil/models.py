from django.db import models


# Create your models here.
class acceuil(models.Model):
    nom = models.CharField(max_length=200)
    type = models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nom
