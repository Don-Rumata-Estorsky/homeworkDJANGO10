from django.shortcuts import *
from django.http import *
from django.urls import *
from django.shortcuts import *
from .models import *
from django.urls import *



from django.http import Http404
from .forms import BookForm
from .models import Book


def allbook(request):
    
    books = Book.objects.all()
    return render(request, 'allbook.html', {'books': books})


def book_create(request):
    if request.method == 'POST':
        form = BookForm(request.POST)
        if form.is_valid():
           
            form.save()
            
            return redirect('allbook') 
        else:
            raise Http404("404 error hyi tati gyboy trasi") 
    else:
        form = BookForm()

    return render(request, 'book_create.html', {'form': form})


