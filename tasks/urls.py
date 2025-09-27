from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_tasks, name='search'),
    path('create/', views.create_task, name='create-task'),
    path('<int:pk>/delete/', views.delete_task, name='delete-task'),
    path('<int:pk>/edit/', views.edit_task, name='edit-task'),
    path('<int:pk>/update/', views.update_task, name='update-task'),

]
