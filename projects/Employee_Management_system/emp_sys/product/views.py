from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .models import Product
from .serializers import ProductSerializer

from datetime import datetime


# Create your views here.


@api_view(['post', 'get', 'patch', 'put', 'delete'])
def product_view(request):
    try:
        if request.method == 'POST':
            try:
                data = request.data
                serializer = ProductSerializer(data=data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({
                    "message": "data has been saved",
                    "data": serializer.data
                }, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    "message": "Some Error Occurs",
                    "error": e.args
                }, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'GET':
            try:
                queryset = Product.objects.all()
                serializer = ProductSerializer(queryset, many=True)
                return Response(serializer.data, status=status.HTTP_200_OK)
            except Exception as e:
                return Response({
                    "message": "Some Error Occurs",
                    "error": e.args
                }, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'PUT':
            try:
                product_id = request.data.get('product_id')
                queryset = Product.objects.filter(id=product_id)
                if queryset:
                    queryset = queryset[0]
                    queryset.product_name = request.data.get('product_name')
                    queryset.product_type = request.data.get('product_type')
                    queryset.product_price = request.data.get('product_price')
                    queryset.product_quantity = request.data.get('product_quantity')
                    queryset.product_update_time = datetime.utcnow()
                    queryset.save()
                    serializer = ProductSerializer(queryset)
                    return Response({
                        "message": "Data Updated",
                        "data": serializer.data
                    }, status=status.HTTP_200_OK)
                return Response({
                    "message": "Invalid Id",
                    "data": []
                }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({
                    "message": "Some Error Occurs",
                    "error": e.args
                }, status=status.HTTP_400_BAD_REQUEST)
        if request.method == 'DELETE':
            try:
                product_id = request.data.get('product_id')
                queryset = Product.objects.filter(id=product_id)
                if queryset:
                    queryset = queryset[0]
                    queryset.delete()
                    return Response({
                        "message": "Product has been deleted"
                    }, status=status.HTTP_200_OK)

                return Response({
                    "message": "Invalid Id",
                    "data": []
                }, status=status.HTTP_404_NOT_FOUND)
            except Exception as e:
                return Response({
                    "message": "Some Error Occurs",
                    "error": e.args
                }, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({
            "message": "Some Error Occurs",
            "error": e.args
        }, status=status.HTTP_400_BAD_REQUEST)


@api_view(['get'])
def filter_view(request):
    data = request.data.get('product_type')
    if len(data)==0:
        return Response({
            "message":"Type Is not Valid Please Enter the valid Type for product",
            "data":[]
        },status=status.HTTP_406_NOT_ACCEPTABLE)
    try:
        queryset = Product.objects.filter(product_type=data)
        if queryset:
            serializer = ProductSerializer(queryset, many=True)
            return Response({
                "message": "Filtred Data",
                "data": serializer.data
            }, status=status.HTTP_200_OK)
        return Response({
            "message": "No Item Found For this Type",
            "data": []
        }, status=status.HTTP_404_NOT_FOUND)
    except Exception as e:
        return Response({
            "message": "Some Error Occurs",
            "error": e.args
        }, status=status.HTTP_400_BAD_REQUEST)
