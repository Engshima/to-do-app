from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView
from django.contrib.auth.views import (
    LogoutView,
    PasswordResetView,
    PasswordResetDoneView,
    PasswordResetConfirmView,
    PasswordResetCompleteView

)



app_name='users'

urlpatterns = [
    path('login/',MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'),name='logout'),#The next_page argument specifies the URL that the users will be redirected to once they log out successfully.
    path('register/', RegisterView.as_view(),name='register'),
    path('password-reset/',PasswordResetView.as_view(template_name='registration/password_reset.html' ,html_email_template_name='users/password_reset_email.html'), name='password-reset'),
    path('password-reset/done/',PasswordResetDoneView.as_view(template_name='registration/password_reset_done.html'), name='password-reset-done'),
    path('password-reset-confirm/<uidb64>/<token>/',PasswordResetConfirmView.as_view(template_name='registration/password_reset_confirm.html'), name='password-reset-confirm'),
    path('password-reset-complete/',PasswordResetCompleteView.as_view(template_name='registration/password_reset_complete.html'), name='password-reset-complete')
    
    
]