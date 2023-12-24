from django.urls import path
from .views import *
from django.contrib.auth.views import LogoutView


app_name='users'

urlpatterns = [
    path('login/',MyLoginView.as_view(),name='login'),
    path('logout/', LogoutView.as_view(next_page='users:login'),name='logout'),#The next_page argument specifies the URL that the users will be redirected to once they log out successfully.
]
