from django.db import models


# Create your models here.
class apropos(models.Model):
    surnom = models.CharField(max_length=200,null=True)
    desc = models.CharField(max_length=200, null=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.surnom