

from re import search
from turtle import title
from django.shortcuts import redirect, render, get_list_or_404,HttpResponseRedirect
from django.template import context
from.models import book, category
from .forms import bookform, categoryform
from django.db.models.signals import post_save, post_delete
# Create your views here.

def index (request):

    if request.method == 'POST':
        add_book = bookform(request.POST,request.FILES)
        if add_book.is_valid():
            add_book.save()
        

        add_category = categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()
        return HttpResponseRedirect("/")
    print(request.method)    
    context = {
        'category': category.objects.all(),
        'books': book.objects.all(),
        'form': bookform(),
        'formcat': categoryform(),
        'allbooks': book.objects.filter(active=True).count(),
        'booksold': book.objects.filter(status='sold').count(),
        'bookrental': book.objects.filter(status='rental').count(),
        'bookAvailable': book.objects.filter(status='Available').count(),
    }

    return render (request, 'pages/index.html', context)


def books (request):

    search = book.objects.all()
    title = None
    if "search_name" in request.GET:
        title = request.GET["search_name"]
        if title:
            search= search.filter(name_book__icontains=title)




    
    if request.method == 'POST':
        add_category = categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {

        'category':category.objects.all(),
         'books': search,
        'formcat': categoryform(),
    
    }

    return render (request, 'pages/books.html', context)

def update (request, id):

    book_id = book.objects.get(id=id)
    if request.method == 'POST':
        book_save =bookform(request.POST, request.FILES , instance=book_id)
        if book_save.is_valid():
            book_save.save()
            return redirect ('/')

    else:
        book_save = bookform(instance=book_id)


    if request.method == 'POST':
        add_category = categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {

        'category':category.objects.all(),
        'formcat': categoryform(),
        'form': book_save,
    
    }

    return render (request, 'pages/update.html', context)

def delete (request, id):

    book_delete = book.objects.get(id=id)
    if request.method == 'POST':
        book_delete.delete()
        return redirect ('/')



    if request.method == 'POST':
        add_category = categoryform(request.POST)
        if add_category.is_valid():
            add_category.save()

    context = {

        'category':category.objects.all(),
        'formcat': categoryform(),
    
    }

    
    
    return render (request, 'pages/delete.html', context)
