from django.db import models

# Create your models here.
class contact(models.Model):
    nom=models.CharField(max_length=200)
    prenom=models.CharField(max_length=200)
    email=models.EmailField()
    telephone=models.CharField(max_length=200)
    message=models.TextField()
    def __str__(self):
        return self.nom