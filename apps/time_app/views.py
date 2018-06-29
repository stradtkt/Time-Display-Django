# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect

from time import gmtime, strftime

def index(request):
  context = {
    "time": strftime("%B %d", gmtime()),
    "time2": strftime("%Y", gmtime()),
    "time3":strftime("%H:%M %p", gmtime())
  }
  return render(request, "time_app/index.html", context)


