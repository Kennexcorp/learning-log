from os import name
from django.urls import path
from django.urls.conf import include

from . import views

app_name = 'users'

urlpatterns = [
   path('', include('django.contrib.auth.urls')),
   path('register/', views.register, name="register")
]
