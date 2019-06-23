from django.urls import path
from . import views

urlpatterns = [
    path('buildmap', views.buildmap, name='buildmap'),
    path('', views.upload_file, name='upload_file'),
]
