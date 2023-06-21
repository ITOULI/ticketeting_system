from django.contrib import admin
from .models import *
# Register your models here.

admin.site.register(Organism)
admin.site.register(Category)
admin.site.register(Event)
admin.site.register(Organizator)
admin.site.register(PricingPlan)
admin.site.register(Ticket)
