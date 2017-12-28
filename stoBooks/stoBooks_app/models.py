# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Custom field so that we can specify what types of input we want
# class IntegerRangeField(models.IntegerField):
#     def __init__(self, verbose_name=None, name=None, min_value=None, max_value=None, **kwargs):
#         self.min_value, self.max_value = min_value, max_value
#         models.IntegerField.__init__(self, verbose_name, name, **kwargs)
#
#     def formfield(self, **kwargs):
#         defaults = {'min_value': self.min_value, 'max_value': self.max_value}
#         defaults.update(kwargs)
#         return super(IntegerRangeField, self).formfield(**defaults)


# Student model with method to create itself
class Student(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    payment = models.CharField(max_length=30)

    def __str__(self):
        return self.username

    @classmethod
    def create(cls, first_name,last_name,username,payment):
        student = cls(
            first_name = first_name,
            last_name = last_name,
            username = username,
            payment = payment
        )
        return student

# student = Student.create("Peter","McCrae","mccrae1","Venmo")
#Make all of these tuples of the form ('Model value','Human readable value')
# DEPT_CHOICES = (
# 'AFAM','AMCON','AMST',
# 'ART','ASIAN','BIO',
# 'CH/BI','CHEM','CHIN',
# 'CLASS','CSCI','DANCE',
# 'ECON','EDUC','ENGL',
# 'ENVST','ESAC','ESTH',
# 'FAMST','FILM','FREN',
# 'GCON','GERM','GREEK',
# 'HIST','ID','IS',
# 'JAPAN','LATIN','MATH',
# 'MEDIA','MGMT','MSCS',
# 'MUSEN','MUSIC','NORW',
# 'NURS','OFFC','PACON',
# 'PHIL','PHYS','PSCI',
# 'PSYCH','RACE','REL',
# 'RUSSN','SCICN','SOAN',
# 'SPAN','STAT','SWRK',
# 'THEAT','WMGST','WRIT'
# )
# Book model with method to construct itself
class Book(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    edition = models.IntegerField()
    dept = models.CharField(max_length=5)
    #This model gives an error that the choices must be an iterable tuples
    # dept = models.CharField(max_length=5,choices=DEPT_CHOICES)

    class_number = models.IntegerField()
    isbn = models.IntegerField()
    # isbn = fields.IntegerRangeField(min_value=1111111111111, max_value=9999999999999)
    price = models.IntegerField()
    # We need to figure out how to make this field a student object
    # seller = models.CharField(max_length=8)
    seller = models.ForeignKey(Student, on_delete=models.CASCADE)
    post_date = models.DateTimeField('date posted')
    #Bind the file data to the form
    # cover = models.ImageField()
    def __str__(self):
        return self.title

    @classmethod
    def create(cls, title, author, edition, dept, class_number, isbn, price, seller):
        book = cls(title=title,
                   author=author,
                   edition=edition,
                   dept=dept,
                   class_number=class_number,
                   isbn=isbn,
                   price=price,
                   seller=seller)
        return book

#An example of how to create a book
# book = Book.create("Moby Dick", "Herman Mellville", 2, "ENG", 231, 1234567891234, 20, "mccrae1")
