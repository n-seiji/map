from django.urls import path
from . import views

urlpatterns = [
    path('', views.buildmap, name='buildmap'),
    path('', views.hello, name='hello'),
]
