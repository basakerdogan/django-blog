from django.urls import path
from blog.views import contacts_view

urlpatterns = [
    path('contact', contacts_view, name="contact"), 
]
