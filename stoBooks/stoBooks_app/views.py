# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.http import Http404
from django.template import loader #allows django to import vi
from django.views.generic import TemplateView
from .models import Book
from .forms import BookForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.core import serializers

json_serializer = serializers.get_serializer("json")()


def index(request):
    recent_postings = Book.objects.order_by('post_date')[:5]
    template = loader.get_template('stoBooks_app/index.html')
    context = {
            'recent_postings':recent_postings,
            }
    return render(request, 'stoBooks_app/index.html', context)

def profile(request):
    all_posts = Book.objects.all()
    current_student= Student.objects.filter(id=1)
    template = loader.get_template('stoBooks_app/user-profile.html')
    context = {
            'current_student':current_student,
            'all_posts':all_posts,
            }
    return render(request, 'stoBooks_app/user-profile.html', context)


def search(request):
    all_posts = json_serializer.serialize(Book.objects.all(), ensure_ascii=False)
    return render(request, 'stoBooks_app/search.html', {'all_posts': all_posts})

def buy(request):
    all_posts = Book.objects.all()
    recent_postings = Book.objects.order_by('post_date')[:5]
    template = loader.get_template('stoBooks_app/buy.html')
    context = {
            'all_posts':all_posts
            }
    return render(request, 'stoBooks_app/buy.html', context)

def sell(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        book = form.save(commit=False)
        book.seller = User.objects.get(username=request.user)
        book.save()
        return HttpResponseRedirect('/sell/')
        # print(book)
        #     book.save()
        #     print(reverse('sell'))
        #     return HttpResponseRedirect(reverse('sell'))
        # else:
        #     print(form.errors)
    else:
        form = BookForm()
    return render(request, 'stoBooks_app/sell.html', {'form': form})



# def stoLib(request):
#     #eventually we should find a way to rank by popularity of course or something
#     recent_postings = Book.objects.order_by('-post_date')[:5]
#     template = loader.get_template('stoBooks_app/index.html')
#     context = {
#             'recent_postings':recent_postings,
#             }
#     return render(request('stoBooks_app/index.html'))
