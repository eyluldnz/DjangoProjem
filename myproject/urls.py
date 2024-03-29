"""myproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path,include

from home import views
from order import views as orderviews

urlpatterns = [
    path('', include('home.urls')),
    path('home/', include('home.urls')),
    path('about/', views.about, name='about'),
    path('referans/', views.referans, name='referans'),
    path('contact/', views.contact, name='contact'),
    path('book/', include('book.urls')),
    path('admin/', admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),
    path('category/<int:id>/<slug:slug>/', views.category_books, name='category_books'),
    path('book/<int:id>/', views.book_detail, name='book_detail'),
    path('search/', views.book_search, name='book_search'),
    path('search_auto/', views.book_search_auto, name='book_search_auto'),
    path('logout/', views.logout_view, name='logout_view'),
    path('login/', views.login_view, name='login_view'),
    path('join/', views.join_view, name='join_view'),
    path('user/', include('user.urls')),
    path('order/', include('order.urls')),
    path('content/', include('content.urls')),
    path('loancart/', orderviews.loancart, name='loancart'),
    path('menu/<int:id>', views.menu, name='menu'),
    path('content/<int:id>/<slug:slug>/', views.contentdetail, name='contentdetail'),
    path('sss/', views.faq, name='faq'),



]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
