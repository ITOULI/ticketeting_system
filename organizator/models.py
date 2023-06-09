from django.db import models

# Create your models here.

class Organism(models.Model):
    id_organism = models.AutoField(primary_key=True)
    organism_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='organism_logos/')
    description = models.TextField()

    def __str__(self):
        return self.organism_name