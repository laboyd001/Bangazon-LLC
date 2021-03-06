from django.urls import path
from . import views

app_name = 'Website'
urlpatterns = [
  path('', views.index, name='index'),
  path('employees/', views.employees, name='employees'),
  path('employees/detail/<int:employee_id>/', views.employees_detail, name='employees_detail'),
  path('employees/add/', views.employees_add, name='employees_add'),
  path('employees/edit/<int:employee_id>/', views.employees_edit, name='employees_edit'),
  path('employees/edit/<int:employee_id>/computer/', views.employees_edit_computer, name='employees_edit_computer'),
  path('departments/', views.departments, name='departments'),
  path('departments/add', views.departments_add, name='departments_add'),
  path('departments/detail/<int:department_id>/', views.departments_detail, name='departments_detail'),
  path('computers/', views.computers, name='computers'),
  path('computers/detail/<int:computer_id>/', views.computers_detail, name='computers_detail'),
  path('computers/add/', views.computers_add, name='computers_add'),
  path('computers/delete/<int:computer_id>', views.computers_delete, name='computers_delete'),
  path('training/', views.training, name='training'),
  path('training/add', views.training_add, name='training_add'),
]