from django.conf.urls import url
from . import views #from current directory import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /712/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),

    # /organisations
    url(r'^orgs$', views.organisations, name='organisations'),


]
