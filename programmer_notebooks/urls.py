"""Defines URL patterns for programmer_notebooks"""

from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # Home Page
    path('', index, name='index'),

    # Topics Page (all topics)
    path('topics', topics, name='topics'),

    # Topic Page (individual topic)
    path('topics/<int:topic_id>', topic, name='topic')
]