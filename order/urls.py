from django.urls import path
from . import views

urlpatterns = [
    # ex: /home/
   # path('', views.index, name='index'),
    # ex: /polls/5/
    path('addtocart/<int:id>', views.addtocart, name='addtocart'),
    path('deletefromcart/<int:id>', views.deletefromcart, name='deletefromcart'),
    # ex: /polls/5/results/
   # path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
   # path('addcomment/<int:id>', views.addcomment, name='addcomment'),
]