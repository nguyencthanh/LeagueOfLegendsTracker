from django.shortcuts import render, HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import User
from .serializer import UserSerializer

# Create your views here.
@api_view(['GET'])
def get_user(request):
    return Response(UserSerializer({'puuid': "1", 'gameName': "2", 'tagLine': "3"}).data)

def home(request):
    return render(request, "home.html")