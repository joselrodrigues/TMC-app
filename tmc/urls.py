from django.urls import path, include
from django.conf.urls import url
from tmc.views import tmc

urlpatterns = [
    url(r'^$', tmc, name="tmc"),
]
