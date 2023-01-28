from django.shortcuts import render, get_object_or_404, redirect
from .models import Todo
from .forms import PostForm

# Create your views here.
def ListView(request):
    list= Todo.objects.filter(author=request.user, accomplished=False)
    return render(request,'list.html',{'list':list})

def DetailView(request,pk):
    detail= get_object_or_404(Todo,pk=pk)
    return render(request,'detail.html',{'detail': detail})


def Accomplish(request,pk):
    task=get_object_or_404(Todo,pk=pk)
    task.accomplished_list()
    return redirect('detail',pk=pk)

def Accomplish_list(request):
    tasks= Todo.objects.filter(accomplished = True)
    return render(request,'accomplish.html',{'tasks':tasks})


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