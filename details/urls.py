from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    path('',views.login,name='login'),
    path('books/',views.Books_Details,name='book'),
 
    path('details/',views.Library_Member,name='LibraryMember'),
    path('img/',views.allimages,name='image')
    
]

