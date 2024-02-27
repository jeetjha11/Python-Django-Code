import json

from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from firstApi.models import UserTable
from firstApi.serializer import UserTableSerializer


# Create your views here.
#  http://127.0.0.1:8000/first_api/get_message

@api_view(['get'])
def get_greet_message(request):
    return Response("Hii this is my first api")


@api_view(['get', 'post'])
def get_user_data(request):
    print("request_data:  ", request.data)
    data = {
        "user_name": "Vikash Kumar",
        "phone_number": "1234567",
        "email": "vikash@gmail.com",
        "address": "Bhopal",
        "education": "B.tech"
    }

    # response = json.dumps(data)

    return Response(data, status.HTTP_200_OK)


@api_view(['post', 'get'])
def register_user_data(request):
    if request.method == 'POST':
        print("Method name: ", request.method)
        data = request.data
        serializer = UserTableSerializer(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Data has been successfully saved.",
            "data": serializer.data
        }, status=status.HTTP_200_OK)
    elif request.method == 'GET':
        result_data = UserTable.objects.all()
        result_serializer = UserTableSerializer(result_data, many=True)
        return Response(result_serializer.data, status=status.HTTP_200_OK)
