from django.shortcuts import render

from django.http import HttpResponse, JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .models import User
from .serializers import UserSerializer

import json


@api_view(['GET'])
def get_users(request):

    if request.method == 'GET':
        users = User.objects.all()

        serializer = UserSerializer(users, many=True)

        return Response(serializer.data)

    return Response(status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
def get_by_nick(request, nick):

    try:

        user = User.objects.get(pk=nick)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)

    if request.metho == 'GET':

        serialier = UserSerializer(user)

        return Response(serialier.data)
    
    if request.method == 'PUT':

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():
            serializer.save()

            return Response(serializer.data, status=status.HTTP_200_ok)

        return Response(status=status.HTTP_400_BAD_REQUEST)

    # CRUD Da massa

@api_view(['GET', 'POST', 'PUT', 'DELETE'])
def user_manager(request):

    if request.method == 'GET':

        try:
            if request.GET['user']:

                user_nickname = request.GET['user']

                try:
                    user = User.objects.get(pk=user_nickname)
                except:
                    return Response(status=status.HTTP_404_NOT_FOUND)

                user = User.objects.get(pk=user_nickname)

                serializer = UserSerializer(user)

                return Response(serializer.data)

            else:
                return Response(status=status.HTTP_400_BAD_REQUEST)
# Compare this snippet from api_rest/views.py:
        except:
                    return Response(status=status.HTTP_400_BAD_REQUEST)
            
# Criando Dados 
    if request.method == 'POST':
    
        new_user =  request.data
        
        serializer = UserSerializer(data=new_user)
        
        if serializer.is_valid():
                
                serializer.save()
                
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            
        return Response(status=status.HTTP_400_BAD_REQUEST)           


# Editando Dados

    if request.method == 'PUT':

        user_nickname = request.GET['user']

        try:
            user = User.objects.get(pk=user_nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user = User.objects.get(pk=user_nickname)

        serializer = UserSerializer(user, data=request.data)

        if serializer.is_valid():

            serializer.save()

            return Response(serializer.data)

        return Response(status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        user_nickname = request.GET['user']

        try:
            user = User.objects.get(pk=user_nickname)
        except:
            return Response(status=status.HTTP_404_NOT_FOUND)

        user.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)





# def databaseEmDjango():

#   data = User.objects.get(pk='Rodrgi')

#   data =User.objects.filter(user_age='28')

#   data = User.objects.exclude(user_age='25')


#   data.save()

#   data.delete()
