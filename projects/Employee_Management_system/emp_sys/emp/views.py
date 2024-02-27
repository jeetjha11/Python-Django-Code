from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import EmployeeTable
from .serializers import EmployeeSerializers


# Create your views here.


@api_view(['post', 'get', 'delete', 'put'])
def employee_view(request):
    if request.method == 'POST':
        data = request.data

        serializer = EmployeeSerializers(data=data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response({
            "message": "Employee data saved success...",
            "data": serializer.data

        }, status=status.HTTP_200_OK)

    if request.method == 'GET':
        queryset = EmployeeTable.objects.all()
        response_serializer = EmployeeSerializers(queryset, many=True)
        return Response(response_serializer.data, status=status.HTTP_200_OK)

    if request.method == 'DELETE':
        try:
            id = request.data.get('id')

            queryset = EmployeeTable.objects.filter(id=id)
            if queryset:
                queryset = queryset[0]
                queryset.delete()
                return Response({"message": "Data deleted"}, status=status.HTTP_200_OK)
            return Response({"message": "Invalid user id"})

        except Exception as e:
            raise e

    if request.method == 'PUT':
        user_id = request.data.get('id')
        queryset = EmployeeTable.objects.filter(id=user_id)
        if queryset:
            queryset = queryset[0]
            queryset.emp_id = request.data.get('emp_id')
            queryset.emp_name = request.data.get('emp_name')
            queryset.emp_phone_number = request.data.get('emp_phone_number')
            queryset.emp_email = request.data.get('emp_email')
            queryset.emp_address = request.data.get('emp_address')

            queryset.save()
            serializer = EmployeeSerializers(queryset)
            return Response({
                "message": "Data has been updated.",
                "data": serializer.data
            })
        return Response({
            "message": "Invalid User Id Provided"
        })


