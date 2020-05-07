import json

from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import  messages
import _json

# Create your views here.
from book.models import Book, Category, Images, Comment
from home.forms import SearchFormu
from home.models import Setting, ContactFormMessage, ContactFormu


def index(request):
    setting =Setting.objects.get(pk=1)
    sliderdata=Book.objects.all()[:4]
    category= Category.objects.all()
    context = {'setting': setting, 'page': 'home',
               'category':category,
               'sliderdata': sliderdata}
    return render(request,'index.html',context)

def about(request):
    setting =Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'about'}
    return render(request,'about.html',context)
def referans(request):
    setting =Setting.objects.get(pk=1)
    context = {'setting': setting, 'page': 'referans'}
    return render(request,'referans.html',context)

def contact(request):

    if request.method=='POST':
        form=ContactFormu(request.POST)
        if form.is_valid():
            data=ContactFormMessage()
            data.name=form.cleaned_data['name']
            data.email = form.cleaned_data['email']
            data.subject = form.cleaned_data['subject']
            data.messages = form.cleaned_data['messages']
            data.ip=request.META.get('REMOTE_ADDR')
            data.save()

            messages.success(request, "Mesajınız iletilmiştir")
            return  HttpResponseRedirect ('/contact')



    setting =Setting.objects.get(pk=1)
    forms =ContactFormu()
    context = {'setting': setting, 'forms':forms}
    return render(request,'contact.html',context)

def category_books(request,id, slug):
    category = Category.objects.all()
    categorydata=Category.objects.get(pk=id)
    books = Book.objects.filter(category_id=id)
    context = {'books': books,
               'category': category,
               'categorydata': categorydata}

    return render(request, 'kitaplar.html', context)

def book_detail(request,id):
    category = Category.objects.all()
    book = Book.objects.get(pk=id)
    images=Images.objects.filter(book_id=id)
    comments =Comment.objects.filter(book_id=id,status='True')
    context = { 'book':book,
               'category': category,
                'images': images,
                'comments': comments
               }

    return render(request, 'kitapdetay.html',context)

def book_search(request):
    if request.method == 'POST':
        form = SearchFormu(request.POST)
        if form.is_valid():
            category=Category.objects.all()
            query = form.cleaned_data['query']
            books=Book.objects.filter(title__icontains=query)
            context= {'books': books , 'category': category, 'query': query }
            return render(request,'book_search.html',context)

        return HttpResponseRedirect('/')


def book_search_auto(request):

         if request.is_ajax():

             q = request.GET.get('term', '')
             book = Book.objects.filter(title__icontains=q)
             results = []
             for pk in book:
                 book_json = {}
                 book_json = pk.title
                 results.append(book_json)

             data = json.dumps(results)

         else:
             data = 'fail'

         mimetype = 'application/json'
         return HttpResponse(data, mimetype)


