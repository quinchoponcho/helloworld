from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
from myapp import views

urlpatterns = [
url(r'^$', views.index, name='index'),
url(r'^myapp/', include('myapp.urls')),
url(r'^admin/', admin.site.urls),
]


