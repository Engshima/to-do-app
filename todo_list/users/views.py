from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView 
from django.contrib import messages
from django.shortcuts import render
from django.http import HttpResponse
from django.urls import reverse_lazy
from .forms import RegisterForm
from django.views.generic.edit import FormView
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from .forms import ProfileUpdateForm, UpdateUserForm
from django.contrib.auth.models import User
from django.shortcuts import redirect



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

class MyProfile(LoginRequiredMixin, View):
    def get(self,request):
        user_form = UpdateUserForm(instance=request.user)
        profile_form= ProfileUpdateForm(instance=request.user.profile)
        
        context ={
            'user_form':user_form,
            'profile_form':profile_form
        }
        
        return render(request,'registration/profile.html', context)
    
    def post(self,request):
        user_form = UpdateUserForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm(request.POST, request.FILES ,instance=request.user.profile)
        
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            messages.success(request, "your profile has been updated successfully")
            return redirect('profile')
        
        
        
        else:
            context = {
                'user_form':user_form,
                'profile_form':profile_form
                }
                         # Display form validation errors
            for field in user_form:
              if field.errors:
                    messages.error(request, f"Error in {field.label}: {', '.join(field.errors)}")
    
            for field in profile_form:
                if field.errors:
                 messages.error(request, f"Error in {field.label}: {', '.join(field.errors)}")
    
                return render(request, 'registration/profile.html', context)
            
                    
            
            messages.error(request, "Error updating you profile")
            return render(request, 'registration/profile.html', context)