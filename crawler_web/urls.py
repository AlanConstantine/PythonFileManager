"""crawler_web URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
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
from scratch import views as scratch_views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^$', scratch_views.home),
    url(r'^crawlers/(?P<id>\d+)/update', scratch_views.update),
    url(r'^crawlers/(?P<id>\d+)/edit/', scratch_views.edit),
    url(r'^crawlers/create', scratch_views.create),
    url(r'^crawlers/(?P<id>\d+)/delete/', scratch_views.delete, name='delete'),
    url(r'^crawlers/(?P<id>\d+)/', scratch_views.show, name='show'),
    url(r'^crawlers/new', scratch_views.new),
    url(r'^crawlers', scratch_views.home),
]
