from os import name
from django.urls import path

from . import views

app_name = 'learning_logs'

urlpatterns = [

    # Home page
    path('', views.index, name='index'),

    # All topics page
    path('topics/', views.topics, name='topics'),

    # Detail page for a single topic
    path('topics/<int:topic_id>/', views.topic, name='topic'),

    # Page for adding new topics
    path('topics/create', views.create, name='create'),

    # Page for adding new entry
    path('new_entry/<int:topic_id>/', views.new_entry, name='new_entry'),

    # Edit an entry
    path('edit_entry/<int:entry_id>/', views.edit_entry, name='edit_entry'),
    
]
