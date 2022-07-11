# from django.shortcuts import render
# from django.http import JsonResponse


# from rest_framework.decorators import api_view
# from rest_framework.response import Response
# from .serializers import TaskSerializer
# from .models import Task

# # Create your views here.

# """
# API Overview
# """
# @api_view(['GET'])
# def apiOverview(request):
#     api_urls = {
#         'List' : '/task-list/',
#         'Detail View' : '/task-detail/<str:pk>/',
#         'Create' : '/task-create/',
#         'Update' : '/task-update/<str:pk>/',
#         'Delete' : '/task-delete/<str:pk>/',
#     }
#     return Response(api_urls)
# """
# Below Function going to display all the tasks store in the data base.
# """
# @api_view(['GET'])
# def taskList(request):
#     tasks = Task.objects.all()
#     serializer = TaskSerializer(tasks, many = True)
#     return Response(serializer.data)

# """
# This Function going to display Detailed view of one perticuler task with the help of pk.
# """
# @api_view(['GET'])
# def taskDetail(request, pk):
#     tasks = Task.objects.get(id=pk)
#     serializer = TaskSerializer(tasks, many = False)
#     return Response(serializer.data)



# @api_view(['POST'])
# def taskCreate(request):
#     serializer = TaskSerializer(data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)



# @api_view(['POST'])
# def taskUpdate(request, pk):
#     task = Task.objects.get(id = pk)
#     serializer = TaskSerializer(instance=task, data=request.data)

#     if serializer.is_valid():
#         serializer.save()
#     return Response(serializer.data)


# @api_view(['DELETE'])
# def taskDelete(request, pk):
#     task = Task.objects.get(id = pk)
#     task.delete()
#     return Response("Taks deleted successfully.")


from rest_framework import generics
from rest_framework.views import APIView

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

class UpdateTodo(generics.UpdateAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer


class DeleteTodo(generics.DestroyAPIView):
    queryset = Task.objects.all()
    serializer_class = TaskSerializer

# class RegisterView(generics.CreateAPIView):
#    queryset = CustomUser.objects.all()
#    serializer_class = UserSerializer


# class LoginView(APIView):
#     def post(self, request):
#         email = request.data['email']
#         password = request.data['password']

#         user = CustomUser.objects.filter(email=email).first()

#         if user is None:
#             # raise AuthenticationFailed('Credentials not found')
#             return JsonResponse({"error":"Email Mismatch"}, status=401)
        
#         if not user.check_password(password):
#             # raise AuthenticationFailed('Incorrect Password')
#             return JsonResponse({"error":"Incorrect passoword"}, status=401)
        
#         payload = {
#             'id': user.id,
#             'exp': datetime.datetime.utcnow() + datetime.timedelta(minutes=7200),
#             'iat': datetime.datetime.utcnow()
#         }
#         token = jwt.encode(payload, 'secret',algorithm='HS256')
        


#         response =  Response()

#         response.set_cookie(key='jwt', value=token, httponly=True)
#         response.data= {
#             'jwt' : token
#         }

#         return response

