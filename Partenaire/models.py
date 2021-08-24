from django.db import models

# Create your models here.
class partenaire(models.Model):
    nom=models.CharField(max_length=200)
    description=models.CharField(max_length=200)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.nom