from django.urls import reverse_lazy
from .forms import CustomUserCreationForm
from django.views import View
from django.shortcuts import redirect, render


    
# class SignUpView(CreateView):
#     form_class= CustomUserCreationForm
#     success_url= reverse_lazy('login')
#     template_name= 'registration/signup.html'
    
#     def get(self,request,*args,**kwargs):
#         if self.request.user.is_authenticated:
#             return redirect('list')        
#         form= CustomUserCreationForm() 
#         return render(request,self.template_name,{'form':form})
    
def SignUpView(request):
    if request.user.is_authenticated:
        return redirect('list')
    if request.method=="POST":
        form= CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form=CustomUserCreationForm()
    return render(request,'registration/signup.html',{'form':form})