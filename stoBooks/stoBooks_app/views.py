# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #allows django to import vi

# Create your views here.
def index(request):
    return render(request, 'stoBooks_app/index.html', {})





