# -*- coding: utf-8 -*-
from django.conf.urls import patterns, include, url

from website.views import view_login

urlpatterns = patterns('',
    url(r'^$', view_login.homepage, name="home"),
)