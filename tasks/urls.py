from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('search/', views.search_tasks, name='search'),
    path('create/', views.create_task, name='create-task'),
]
