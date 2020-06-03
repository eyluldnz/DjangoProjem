from django.urls import path
from . import views

urlpatterns = [
    # ex: /home/
    path('', views.index, name='index'),
    path('password/', views.change_password, name='change_password'),
    path('update/', views.user_update, name='user_update'),
    # ex: /polls/5/
   # path('<int:question_id>/', views.detail, name='detail'),
    # ex: /polls/5/results/
   # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/

]