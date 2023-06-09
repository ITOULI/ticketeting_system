from django.urls import path
from . import views

urlpatterns = [
    path('organizators/', views.organizators, name='organizators'),
]