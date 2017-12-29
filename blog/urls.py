#!/usr/bin/env python
# -*- coding:utf8 -*-
from django.conf.urls import patterns, include, url
import views

urlpatterns = patterns('blog',
                       url(r'^blog/select$', views.blog_select),

                       )