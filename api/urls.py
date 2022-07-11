from django.urls import path
# from . import views


# urlpatterns = [
#     path('', views.apiOverview, name="api-overview"),
#     path('task-list/', views.taskList, name="task-list"),
#     path('task-detail/<str:pk>/', views.taskDetail, name="task-Detail"),
#     path('task-create/', views.taskCreate, name="task-Create"),
#     path('task-update/<str:pk>/', views.taskUpdate, name="task-update"),
#     path('task-delete/<str:pk>/', views.taskDelete, name="task-delete"),
# ]

from .views import *


urlpatterns = [
    path('<int:pk>/', DetailTodo.as_view()),
    path('', ListTodo.as_view()),
    path('create', CreateTodo.as_view()),
    path('update/<int:pk>/', UpdateTodo.as_view()),
    path('delete/<int:pk>/', DeleteTodo.as_view()),
    # path('register', RegisterView.as_view()),
    # path('login', LoginView.as_view())


]