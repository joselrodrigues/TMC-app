from django.urls import path, include
from tmc.views import tmc

urlpatterns = [
    path('', tmc),
]
