from django.conf.urls import url
from . import views #from current directory import views

urlpatterns = [
    url(r'^$', views.index, name='index'),


]
