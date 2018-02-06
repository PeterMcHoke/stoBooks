from stoBooks_app.models import Book
from django import forms
from django.contrib.auth.models import User

#Form creation for Selling a book

#Remember to make the seller the current user and the date and time of posting now.
class BookForm(forms.ModelForm):
    title = forms.CharField(
        label='Title',
        required=True,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'name': 'title',
                'placeholder': 'Elementary Number Theory',
                'id': 'inputTitle'
            }
        )
    )
    author = forms.CharField(
        label='Author',
        required=True,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'name': 'author',
                'placeholder': 'David Burton',
                'id': 'inputAuthor'
            }
        )
    )
    edition = forms.CharField(
        label='Edition',
        required=True,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'name': 'edition',
                'placeholder': '7',
                'id': 'inputEdition'
            }
        )
    )
    dept = forms.ChoiceField(
        label='Department',
        required=True,
        choices = Book.DEPT_CHOICES,
        widget= forms.Select(
            attrs={
                'class': 'form-control',
                'name': 'dept',
                'id': 'inputDept'
            }
        )
    )
    class_number = forms.CharField(
        label='Class',
        required=True,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'name': 'class_number',
                'placeholder': '239',
                'id': 'inputClass'
            }
        )
    )
    isbn = forms.CharField(
        label='ISBN',
        required=True,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'name': 'isbn',
                'placeholder': '9780073383149',
                'id': 'inputISBN'
            }
        )
    )
    price = forms.CharField(
        label='Price',
        required=True,
        widget= forms.TextInput(
            attrs= {
                'class': 'form-control',
                'name': 'price',
                'placeholder': '$50',
                'id': 'inputPrice'
            }
        )
    )
    class Meta:
        model = Book
        fields = ['title','author','edition','dept','class_number', 'isbn', 'price']
