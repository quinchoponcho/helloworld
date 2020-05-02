
from django.conf.urls import url
from django.conf.urls import include
from myapp import views

urlpatterns = [

    url(r'^$', views.dashBoard, name='dashboard'),
    #url(r'^myapp/', include('myapp.urls')),

]
