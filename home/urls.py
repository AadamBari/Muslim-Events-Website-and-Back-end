from django.conf.urls import url
from . import views #from current directory import views

urlpatterns = [
    # /
    url(r'^$', views.index, name='index'),

    # /712/
    url(r'^(?P<event_id>[0-9]+)/$', views.detail, name='detail'),

    # /orgs
    url(r'^orgs$', views.organisations, name='organisations'),

    # /orgs/22
    url(r'^orgs/(?P<org_id>[0-9]+)/$', views.orgdetail, name='orgdetail'),

    # /about
    url(r'^about$', views.about, name='about'),


]
