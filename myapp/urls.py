from django.conf.urls import url
from django.urls import path
from myapp import views
from . import views

urlpatterns = [

    path('', views.dashBoard, name="dashboard"),
]
