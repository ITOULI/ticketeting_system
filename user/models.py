from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from organizator.models import Ticket
from organizator.models import Event
from organizator.models import Organizator
from organizator.models import Organism

# Create your models here.

class User(models.Model):
    id_user = models.AutoField(primary_key=True)
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=100, unique=True)
    date_of_birth = models.DateField()
    phone_num = PhoneNumberField() 
    password = models.CharField(max_length=100)
    zipcode = models.IntegerField()
    city = models.CharField(max_length=100)
    
    def __str__(self):
        return f'{self.firstname} {self.lastname} with username : {self.username}'
    
class UserTicket(models.Model):
    user = models.ForeignKey('User', on_delete=models.CASCADE)
    ticket = models.OneToOneField(Ticket, on_delete=models.CASCADE)
    purchase_date = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return f"UserTicket ({self.user}, {self.ticket})"
    
class ConsultUserEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"ConsultUserEvent {self.id}"


class ConsultUserOrganizator(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organizator = models.ForeignKey(Organizator, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"ConsultUserOrganizator {self.id}"


class ConsultUserOrganism(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    organism = models.ForeignKey(Organism, on_delete=models.CASCADE)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"ConsultUserOrganism {self.id}"


class UserRateEvent(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    num_stars = models.IntegerField()
    comment = models.TextField()
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"UserRateEvent {self.id}"
 