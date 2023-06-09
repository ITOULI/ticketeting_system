from django.db import models

# Create your models here.

class Organism(models.Model):
    id_organism = models.AutoField(primary_key=True)
    organism_name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='organism_logos/')
    description = models.TextField()

    def __str__(self):
        return self.organism_name
    
class Category(models.Model):
    id_category = models.AutoField(primary_key=True)
    label = models.CharField(max_length=100)

    def __str__(self):
        return self.label
    
class Event(models.Model):
    id_event = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    description = models.TextField()
    main_img = models.ImageField(upload_to='event_images/')
    thumbnail = models.ImageField(upload_to='event_thumbnails/')
    licence = models.TextField(max_length=100)
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    organism = models.ForeignKey('Organism', on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class Organizator(models.Model):
    id_organizator = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone_num = models.CharField(max_length=20)
    password = models.CharField(max_length=100)
    is_admin = models.BooleanField(default=False)
    organism = models.ForeignKey('Organism', on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.firstname} {self.lastname}"
    
class PricingPlan(models.Model):
    id_plan = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    tickets_available = models.IntegerField()
    description = models.TextField()
    event = models.ForeignKey('Event', on_delete=models.CASCADE)

    def __str__(self):
        return self.name