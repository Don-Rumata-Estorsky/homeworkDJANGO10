


from django.contrib import admin
from django.urls import path, re_path
from app.views import *
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('create/', views.book_create, name='book_create'),
    path('', views.allbook, name='allbook'), 
]



