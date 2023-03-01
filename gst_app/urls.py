from django.urls import path
from . import views

urlpatterns = [
    path('', views.gst_app, name='main'),
]