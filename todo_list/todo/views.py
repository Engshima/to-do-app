from django.shortcuts import render
from .models import task
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView 
from django.views.generic.edit import CreateView 
from django.urls import reverse_lazy
from django.contrib import messages



# Create your views here.
def home(request):
    return render(request,'home.html')


class TaskList(ListView):
    model = task
    context_object_name= 'tasks'
    
class TaskDetail(DetailView):
    model = task
    context_object_name='task'
    
    
class CreateTask(CreateView):
        model = task
        fields = ['title', 'description', 'completed']
        success_url = reverse_lazy('todo:tasks')
        
        def  form_valid(self, form):
            form.instance.user = self.request.user # set user to the currently logged user
            messages.success(self.request,"Form successfully submitted'")# create a flash message
            return super(CreateTask,self).form_valid(form)# return the result of the form_valid() method of the superclass
        
#In this example, MyCreateView is a view that handles the creation of a new instance of MyModel. 
# When the form is valid, it sets the user of the new instance to the currently logged user,
# creates a success flash message, 
# and then calls the form_valid() method of the superclass to handle saving the instance to the database        
#and then redirects the user to the "tasks" URL       
        
        
        
    