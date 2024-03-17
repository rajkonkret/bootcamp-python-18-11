from django.shortcuts import render, redirect
from .models import Book
from .forms import BookForm


# Create your views here.
def book_list(request):
    books = Book.objects.all()
    return render(request, 'books/book_list.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('book_list')
    else:
        form = BookForm()
        return render(request, 'books/book_form.html', {'form': form})
