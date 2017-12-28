# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from django.http import HttpResponse
from django.http import Http404
from django.template import loader #allows django to import vi
from django.views.generic import TemplateView
from .models import Book
from .models import Student
# Create your views here.
# def index(request):
#      return render(request, 'stoBooks_app/index.html', {})
def index(request):
    # def get(self,request,**kwargs):
    #     return render(request, 'stoBooks_app/index.html', context=None)
    recent_postings = Book.objects.order_by('post_date')[:5]
    template = loader.get_template('stoBooks_app/index.html')
    context = {
            'recent_postings':recent_postings,
            }
    return render(request, 'stoBooks_app/index.html', context)

# class ProfilePageView(TemplateView):
#     template_name = "stoBooks_app/user-profile.html"
def profile(request):
    current_student= Student.objects.filter(id=1)
    template = loader.get_template('stoBooks_app/user-profile.html')
    context = {
            'current_student':current_student,
            }
    return render(request, 'stoBooks_app/user-profile.html', context)


def search(request):
    return render(request, 'stoBooks_app/search.html', {})

# def stoLib(request):
#     #eventually we should find a way to rank by popularity of course or something
#     recent_postings = Book.objects.order_by('-post_date')[:5]
#     template = loader.get_template('stoBooks_app/index.html')
#     context = {
#             'recent_postings':recent_postings,
#             }
#     return render(request('stoBooks_app/index.html'))
