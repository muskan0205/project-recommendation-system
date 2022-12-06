from django.urls import path
#from django.views.generic import RedirectView
#from django.conf.urls import url
from .views import home,profile, RegisterView
from . import views

urlpatterns = [
    path('', home, name='users-home'),
    path('register/', RegisterView.as_view(), name='users-register'),
    path('profile/', profile, name='users-profile'),
    
]
