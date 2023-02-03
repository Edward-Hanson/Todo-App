from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import PostForm
from django.utils import timezone
from django.views.generic import TemplateView
from django.contrib.auth.decorators import login_required

# Create your views here.

class HomeView(TemplateView):
    model=Todo
    template_name= 'home.html'

@login_required  
def ListView(request):
    list= Todo.objects.filter(author=request.user, accomplished=False)
    return render(request,'list.html',{'list':list})

@login_required
def DetailView(request,pk):
    detail= get_object_or_404(Todo,pk=pk)
    return render(request,'detail.html',{'detail': detail})

@login_required
def Accomplish(request,pk):
    task=get_object_or_404(Todo,pk=pk)
    task.accomplished_list()
    return redirect('detail',pk=pk)
@login_required
def Accomplish_list(request):
    tasks= Todo.objects.filter(accomplished = True)
    return render(request,'accomplish.html',{'tasks':tasks})

@login_required
def CreateList(request):
    if request.method=="POST":
        form=PostForm(request.POST)
        
        if form.is_valid():
            post=form.save(commit=False)
            post.author=request.user
            post.save()
            return redirect('detail',pk=post.pk)
    else:
        form=PostForm()
    return render(request,'new.html',{'form':form})

@login_required
def DeleteTask(request,pk):
    task= get_object_or_404(Todo,pk=pk)        
    task.delete()
    return redirect('list')

@login_required
def EditTask(request,pk):
    task=get_object_or_404(Todo,pk=pk)
    if request.method=="POST":
        form= PostForm(request.POST, instance=task)
        if form.is_valid():
            task= form.save(commit=False)
            task.author= request.user
            task.created_on= timezone.now()
            task.save()
            return redirect('detail',pk=task.pk)
    else:
        form= PostForm(instance=task)    
    return render(request,'edit.html',{'form':form})    