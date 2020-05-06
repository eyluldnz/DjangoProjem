from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from book.models import CommentForm , Comment

# Create your views here.

def index(request):
    return HttpResponse("Book Page")


@login_required(login_url='/login')
def addcomment(request, id):
    if request.method == 'POST':
        form = CommentForm(request.POST)
        url = request.META.get('HTTP_REFERER')
        if form.is_valid():
            current_user=request.user

            data = Comment()
            data.user_id = current_user.id
            data.book_id = id
            data.subject = form.cleaned_data['subject']
            data.comment = form.cleaned_data['comment']
            data.rate = form.cleaned_data['rate']
            data.ip = request.META.get('REMOTE_ADDR')
            data.save()
            messages.success(request, "Yorumunuz iletilmiştir.")

            return HttpResponseRedirect(url)
        messages.warning(request, "Yorumunuz gönderilmedi. Kontrol ediniz")
        return HttpResponseRedirect(url)




















