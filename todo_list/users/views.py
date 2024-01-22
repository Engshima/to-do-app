from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView 
from django.contrib import messages
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth import login

# Create your views here.

class MyLoginView(LoginView):
    # redirect_authenticated_user = True
    
    def get_success_url(self):
        return reverse_lazy('todo:tasks')
    
    def form_invalid(self,form):
        messages.error(self.request,"Invalid username or password")
        return self.render_to_response(self.get_context_data(form=form))

 
class RegisterView(FormView): 
    template_name = 'registration/register.html'    
    form_class =  RegisterForm
    redirect_authenticated_user = True   
    success_url = reverse_lazy('todo:tasks')
    
    def form_valid(self, form):
        user = form.save()
        if user:
            login(self.request,user)
        return super(RegisterView,self).form_valid(form)    
            