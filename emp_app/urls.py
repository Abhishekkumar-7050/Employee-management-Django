from django.contrib import admin
from . import views
from django.urls import path ,include


urlpatterns = [
    path('', views.index , name='index'),
    path('add_emp/', views.add_emp , name='add_emp'),
    path('all_emp/', views.all_emp , name='all_emp'),
    path('remove_emp/', views.remove_emp , name='remove_emp'),
    path('filter_emp/', views.filter_emp , name='filter_emp'),
    path('delete-employee/<int:emp_id>/', views.delete_employee, name='delete_employee'),
    path('filter-employee/', views.filter_employee, name='filter_employee')
    

    
]
