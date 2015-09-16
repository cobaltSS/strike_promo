"""t URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.conf.urls import include, url
from django.contrib import admin
from django.core.urlresolvers import reverse
from strusers.views import AddGammerViev, AllGammers, MainPage, DeleteGammerView
from django.conf import settings

urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', MainPage.as_view(), name='main'),
    url(r'^all/$', AllGammers.as_view(), name='all'),
    url(r'^add/$', AddGammerViev.as_view(), name='add'),
    url(r'^delete/(?P<pk>\d+)/$', DeleteGammerView.as_view(), name='delete'),
    url(r'^static/(?P<path>.*)$', 'django.views.static.serve',
    {'document_root', settings.STATIC_ROOT}
  ),
]
