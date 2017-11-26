"""saborto URL Configuration

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
from django.conf.urls import url
from django.contrib import admin
from Hospedajes.views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', index, name = 'index'),
    url(r'^show_all_rooms/', show_all_rooms_view, name = 'rooms'),
    url(r'^search_rooms/', search_rooms_view, name = 'search'),
    url(r'^show_rooms/', show_rooms_view, name = 'show'),
    url(r'^show_single_room/(?P<room_id>\d+)', show_singleR_view, name = 'single'),
    url(r'^det/(?P<id>\d+)', aaa, name = 'details')



] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)