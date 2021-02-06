from django.shortcuts import render, redirect
from p_library.models import Book, Friend
from django.http import HttpResponse
from django.template import loader
from p_library.forms import BookFriendForm, FriendForm, BookForm
from django.views.generic import CreateView, UpdateView
from django.urls import reverse_lazy

def index(request):
    template = loader.get_template('index.html')
    books = Book.objects.all()
    data = {"books":books}
    return HttpResponse(template.render(data, request))

class BookAdd(CreateView):
    model = Book
    form_class = BookForm  
    success_url = reverse_lazy('p_library:index')  
    template_name = 'book_add.html'

class BookEdit(CreateView):
    model = Book
    form_class = BookForm  
    success_url = reverse_lazy('p_library:index')  
    template_name = 'book_edd.html'

class BookFriendEdit(UpdateView):
    model = Book
    form_class = BookFriendForm  
    success_url = reverse_lazy('p_library:index')  
    template_name = 'book_friend_edit.html'

class FriendAdd(CreateView):
    model = Friend
    form_class = FriendForm
    success_url = reverse_lazy('p_library:index')  
    template_name = 'friend_add.html'

def return_book(request):
    if request.method == 'POST':
        book_id = request.POST['id']
        if not book_id:
            return redirect(reverse_lazy('p_library:index'))
        else:
            book = Book.objects.filter(id=book_id).first()
            if not book:
                return redirect(reverse_lazy('p_library:index'))
            book.friends = None
            book.save()
    return redirect(reverse_lazy('p_library:index'))