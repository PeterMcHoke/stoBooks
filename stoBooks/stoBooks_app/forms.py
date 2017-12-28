from stoBooks_app.models import Book
from stoBooks_app.models import Student



#Form creation for Selling a book

#Remember to make the seller the current user and the date and time of posting now.
class BookForm(ModelForm):
    class Meta:
        model = Book
        fields = ['title','author','edition','dept','class_number', 'isbn', 'price']
