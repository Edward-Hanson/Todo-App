from django.urls import path
from .views import ListView, DetailView, Accomplish, Accomplish_list, CreateList, DeleteTask, EditTask, HomeView

urlpatterns=[
    path('',HomeView.as_view(),name='home'),
    path('list/',ListView,name='list'),
    path('<uuid:pk>/',DetailView,name='detail'),
    path('<uuid:pk>/done/',Accomplish,name='accomplish'),
    path('accomplish/',Accomplish_list,name='accomplished_list'),
    path('new/',CreateList,name='new'),
    path('<uuid:pk>/erase/',DeleteTask,name='delete'),
    path('<uuid:pk>/edit',EditTask, name= 'edit'),
]