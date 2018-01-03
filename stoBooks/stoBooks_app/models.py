# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone


# Student model with method to create itself
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    payment = models.CharField(max_length=30)

    def __str__(self):
        return self.username

    class Meta:
        ordering = ['-username']


#Make all of these dept tuples of the form ('Model value','Human readable value')
class Book(models.Model):
    DEPT_CHOICES = (
        ('AFAM','AFAM'),('AMCON','AMCON'),('AMST','AMST'),
        ('ART','ART'),('ASIAN','ASIAN'),('BIO','BIO'),
        ('CH/BI','CH/BI'),('CHEM','CHEM'),('CHIN','CHIN'),
        ('CLASS','CLASS'),('CSCI','CSCI'),('DANCE','DANCE'),
        ('ECON','ECON'),('EDUC','EDUC'),('ENGL','ENGL'),
        ('ENVST','ENVST'),('ESAC','ESAC'),('ESTH','ESTH'),
        ('FAMST','FAMST'),('FILM','FILM'),('FREN','FREN'),
        ('GCON','GCON'),('GERM','GERM'),('GREEK','GREEK'),
        ('HIST','HIST'),('ID','ID'),('IS','IS'),
        ('JAPAN','JAPAN'),('LATIN','LATIN'),('MATH','MATH'),
        ('MEDIA','MEDIA'),('MGMT','MGMT'),('MSCS','MSCS'),
        ('MUSEN','MUSEN'),('MUSIC','MUSIC'),('NORW','NORW'),
        ('NURS','NURS'),('OFFC','OFFC'),('PACON','PACON'),
        ('PHIL','PHIL'),('PHYS','PHYS'),('PSCI','PSCI'),
        ('PSYCH','PSYCH'),('RACE','RACE'),('REL','REL'),
        ('RUSSN','RUSSN'),('SCICN','SCICN'),('SOAN','SOAN'),
        ('SPAN','SPAN'),('STAT','STAT'),('SWRK','SWRK'),
        ('THEAT','THEAT'),('WMGST','WMGST'),('WRIT','WRIT')
    )
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    edition = models.IntegerField()
    dept = models.CharField(max_length=5,choices=DEPT_CHOICES)
    class_number = models.IntegerField()
    isbn = models.IntegerField()
    # isbn = fields.IntegerRangeField(min_value=1111111111111, max_value=9999999999999)
    price = models.IntegerField()
    seller = models.ForeignKey(Student, on_delete=models.CASCADE)
    post_date = models.DateTimeField(default=timezone.now)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    slug = models.SlugField(max_length=40)

    # Feature wave #2. Bind the file data to the form
    # cover = models.ImageField()

    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-post_date']

#An example of how to create a book
# book = Book.create("Moby Dick", "Herman Mellville", 2, "ENG", 231, 1234567891234, 20, "mccrae1")
