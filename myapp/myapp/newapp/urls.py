#from ast import patterns #deprecated
from django import views
from django.urls import path
from . import views

# to add routes to the main url
urlpatterns = [path('', views.index, name= 'index'),  #index will be defined in views.py, it will give the http response
                path('members/', views.member_names, name= 'members'),
                path('members/add/', views.add, name='add'),
                path('members/add/addrecord/', views.addrecord, name='addrecord'),
                path('members/delete/<id>', views.delete, name='delete'), #optionally <int:id> 
                path('members/update/<int:id>', views.update, name='update'),
                path('members/update/updaterecord/<int:id>', views.updaterecord, name='updaterecord')]
