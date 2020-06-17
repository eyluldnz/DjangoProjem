import json

from django.contrib.auth import logout, authenticate, login
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import  messages
import _json

# Create your views here.
from book.models import Book, Category, Images, Comment
from content.models import Menu, Content, CImages
from home.forms import SearchFormu, KayıtFormu
from home.models import Setting, ContactFormMessage, ContactFormu, UserProfil, Faq


def index(request):
    setting =Setting.objects.get(pk=1)
    sliderdata=Book.objects.all().order_by('-id')[:6]
    category= Category.objects.all()
    randombooks=Book.objects.all().order_by('?')[:6]
    menu= Menu.objects.all()
    news= Content.objects.filter(type='haber').order_by('-id')[:4]
    duyurular=  Content.objects.filter(type='duyuru').order_by('-id')[:4]
    current_user = request.user
    profil = UserProfil.objects.get(user_id=request.user.id)

    context = {'setting': setting, 'page': 'home',
               'category':category,
               'sliderdata': sliderdata,
               'menu': menu,
               'news': news,
               'duyurular':duyurular,
               'books': randombooks,'profil':profil,
               }
    return render(request,'index.html',context)

def about(request):
    setting =Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    profil = UserProfil.objects.get(user_id=request.user.id)
    context = {'setting': setting, 'page':about,  'menu':menu,'profil':profil,}
    return render(request,'about.html',context)
def referans(request):
    setting =Setting.objects.get(pk=1)
    menu = Menu.objects.all()
    profil = UserProfil.objects.get(user_id=request.user.id)
    context = {'setting': setting, 'page':referans,  'menu':menu,'profil':profil,}
    return render(request,'referans.html',context, )

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
    menu = Menu.objects.all()
    profil = UserProfil.objects.get(user_id=request.user.id)
    context = {'setting': setting, 'forms':forms, 'menu':menu,'profil':profil,}
    return render(request,'contact.html',context)

def category_books(request,id, slug):
    category = Category.objects.all()
    menu = Menu.objects.all()
    profil = UserProfil.objects.get(user_id=request.user.id)
    categorydata=Category.objects.get(pk=id)
    books = Book.objects.filter(category_id=id)
    setting = Setting.objects.get(pk=1)
    context = {'setting': setting,'books': books,
               'category': category,
               'categorydata': categorydata,'profil':profil, 'menu':menu,}

    return render(request, 'kitaplar.html', context)

def book_detail(request,id):
    profil = UserProfil.objects.get(user_id=request.user.id)
    category = Category.objects.all()
    menu = Menu.objects.all()
    book = Book.objects.get(pk=id)
    images=Images.objects.filter(book_id=id)
    setting = Setting.objects.get(pk=1)
    comments =Comment.objects.filter(book_id=id,status='True')
    context = { 'book':book,
               'category': category,
                'images': images,
                'comments': comments,
                'profil': profil,
                'menu': menu,'setting': setting,'profil':profil,
               }

    return render(request, 'kitapdetay.html',context)


def book_search(request):
    profil = UserProfil.objects.get(user_id=request.user.id)
    if request.method == 'POST':
        form = SearchFormu(request.POST)
        if form.is_valid():
            category=Category.objects.all()
            menu = Menu.objects.all()
            query = form.cleaned_data['query']
            books=Book.objects.filter(title__icontains=query)
            setting = Setting.objects.get(pk=1)
            context= {'books': books , 'category': category, 'query': query,'profil':profil, 'menu':menu, 'setting': setting,'profil':profil, }
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


def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/')


def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return HttpResponseRedirect('/')
        else:
            messages.warning(request, "Lütfen şifrenizi/mailinizi doğru giriniz ")
            return HttpResponseRedirect('/login/')

    category = Category.objects.all()
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category, 'menu':menu,'setting': setting,}
    return render(request, 'login.html', context)


def join_view(request):
    if request.method == 'POST':
        form=KayıtFormu(request.POST)
        if form.is_valid():
            form.save()
            username = request.POST['username']
            password = request.POST['password1']
            user = authenticate(request, username=username, password=password)
            login(request, user)
            current_user = request.user
            data = UserProfil()
            data.user_id = current_user.id
            data.image = "images/users/user.png"
            data.save()
            return HttpResponseRedirect('/')

    form= KayıtFormu()
    category = Category.objects.all()
    menu = Menu.objects.all()
    setting = Setting.objects.get(pk=1)
    context = {'category': category,
               'form':form,
               'menu': menu,'setting': setting,'profil':profil,
               }
    return render(request, 'join.html', context)


def menu (request, id):

    try:
        content = Content.objects.get(menu_id=id)
        link='/content/'+str(content.id)+'/menu'
        return HttpResponseRedirect(link)
    except:
        messages.error(request, "Hata ! İlgili içerik bulunamadı")
        link='/'
        return HttpResponseRedirect(link)


def contentdetail(request, id, slug):
    category = Category.objects.all()
    menu = Menu.objects.all()
    content = Content.objects.get(pk=id)
    images=CImages.objects.filter(content_id=id)
    setting = Setting.objects.get(pk=1)
    profil = UserProfil.objects.get(user_id=request.user.id)
    context = {'category': category,
               'content': content,
               'menu':menu,
               'images':images,'setting': setting,'profil':profil,}
    return render(request, 'content_detail.html', context)


def faq(request):
    category = Category.objects.all()
    menu = Menu.objects.all()
    faq=Faq.objects.all()
    setting = Setting.objects.get(pk=1)
    profil = UserProfil.objects.get(user_id=request.user.id)
    context = {'category': category, 'menu':menu, 'faq':faq,'setting':setting ,'profil':profil,}
    return render(request, 'faq.html', context)