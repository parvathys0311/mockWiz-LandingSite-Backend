from django.urls import path, include
from . import views


urlpatterns = [
    path('', views.index, name="index"),
    path('terms', views.tc, name="tc"),
    ]