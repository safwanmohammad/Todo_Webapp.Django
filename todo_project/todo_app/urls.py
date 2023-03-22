from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_todo, name='add_todo'),
    # path('details', views.details, name='details'),
    path('delete/<int:task_id>/', views.delete_todo, name='delete_todo'),
    path('update/<int:task_id>/', views.update_todo, name='update_todo'),
    path('cbvhome/', views.TasklistView.as_view(), name='cbvhome'),
    path('cbvdetails/<int:pk>/', views.TaskDetailView.as_view(), name='cbvdetails'),
    path('cbvupdate/<int:pk>/', views.TaskUpdateView.as_view(), name='cbvupdate'),
    path('cbvdelete/<int:pk>/', views.TaskDeleteView.as_view(), name='cbvdelete'),

]