# /usr/bin/python2
# -*- coding:utf8 -*-
from django.shortcuts import render
from django.views.decorators.csrf import csrf_protect



def index(request):
    context = {}

    return render(request, '/templates/index.html', context)

