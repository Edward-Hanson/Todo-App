from django.urls import path
from .views import ListView, DetailView, Accomplish, Accomplish_list, CreateList

urlpatterns=[
    path('list/',ListView,name='list'),
    path('<int:pk>/',DetailView,name='detail'),
    path('<int:pk>/done/',Accomplish,name='accomplish'),
    path('accomplish/',Accomplish_list,name='accomplished_list'),
    path('new/',CreateList,name='new'),
]