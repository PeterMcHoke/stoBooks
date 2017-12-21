# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader #allows django to import vi
from django.views.generic import TemplateView
# Create your views here.
# def index(request):
#      return render(request, 'stoBooks_app/index.html', {})
class HomePageView(TemplateView):
    def get(self,request,**kwargs):
        return render(request, 'stoBooks_app/index.html', context=None)
class ProfilePageView(TemplateView):
    template_name = "stoBooks_app/user-profile.html"


def stoLib(request):
    #eventually we should find a way to rank by popularity of course or something
    recent_positings = Book.objects.order_by('post_date')[:5]
    output = ','.join([b.title for b in recent_positings])
    return HttpResponse(output)
