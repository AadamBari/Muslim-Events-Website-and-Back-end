"""Muslim_Events URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.urlpatterns import format_suffix_patterns
from home import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^muslimadmin/', admin.site.urls),
    url(r'^organisations/', views.OrganisationList.as_view()),
    url(r'^events/', views.EventList.as_view()),
    url(r'^locations/', views.LocationList.as_view()),
    url(r'', include('home.urls', namespace='home')),

]

urlpatterns = format_suffix_patterns(urlpatterns)

# see bucky django 33 for explanation
# urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

