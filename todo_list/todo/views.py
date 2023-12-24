from django.shortcuts import render
from .models import task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin



# Create your views here.


class TaskList(LoginRequiredMixin,ListView):
    model = task
    context_object_name= 'tasks'

def home(request):
    return render(request,'home.html')
    
    
    
class TaskDetail(LoginRequiredMixin,DetailView):
    model = task
    context_object_name='task'
    
    
class CreateTask(LoginRequiredMixin,CreateView):
        model = task
        fields = ['title', 'description', 'completed']
        success_url = reverse_lazy('todo:tasks')
        
        def  form_valid(self, form):
            form.instance.user = self.request.user # set user to the currently logged user
            messages.success(self.request,"Form successfully submitted")# create a flash message
            return super(CreateTask,self).form_valid(form)# return the result of the form_valid() method of the superclass
class TaskDelete(LoginRequiredMixin, DeleteView):
    model = task
    context_object_name = 'task'
    success_url = reverse_lazy('todo:tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was deleted successfully.")
        return super(TaskDelete,self).form_valid(form)


class TaskUpdate(LoginRequiredMixin, UpdateView):
    model = task
    fields = ['title','description','completed']
    success_url = reverse_lazy('todo:tasks')
    
    def form_valid(self, form):
        messages.success(self.request, "The task was updated successfully.")
        return super(TaskUpdate,self).form_valid(form)        





#In this example, MyCreateView is a view that handles the creation of a new instance of MyModel. 
# When the form is valid, it sets the user of the new instance to the currently logged user,
# creates a success flash message, 
# and then calls the form_valid() method of the superclass to handle saving the instance to the database        
#and then redirects the user to the "tasks" URL       
        
        
class TaskUpdate(UpdateView):
   model = task
   fields = ['title','description','completed']    
   success_url = reverse_lazy('todo:tasks') 
   
   def form_valid(self,form):
      
       messages.success(self.request,"The task was updated successfully.")
       return super(TaskUpdate,self).form_valid(form)
   
   
class TaskDelete(DeleteView):
    model = task
    context_object_name= 'task'
    success_url = reverse_lazy('todo:tasks')
    
    
    def form_valid(self,form):
      
       messages.success(self.request,"The task was deleted successfully.")
       return super(TaskDelete,self).form_valid(form)
   
   