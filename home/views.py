from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.contrib import  messages

# Create your views here.
from book.models import Book, Category
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