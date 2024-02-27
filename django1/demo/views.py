from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response


# Create your views here.


@api_view(['get'])
def check_message(request):
    return Response("HII I  CALLED")