
from rest_framework import generics

from .serializers import *
from .models import *
import jwt, datetime
from rest_framework.response import Response


# Showing the List
class ListTodo(generics.ListAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# fetching single todo
class DetailTodo(generics.RetrieveAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# creating one
class CreateTodo(generics.CreateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# updating one
class UpdateTodo(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# deleting one
class DeleteTodo(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


# class RegisterView(generics.CreateAPIView):
#    queryset = CustomUser.objects.all()
#    serializer_class = UserSerializer


