from django.shortcuts import render

from quickstart.models import IDUser, NewIDUser
from rest_framework import viewsets
from quickstart.serializers import IDUserSerializer, NewIDUserSerializer

class IDUserViewSet(viewsets.ModelViewSet):
    queryset = IDUser.objects.all().order_by('first_name')
    serializer_class = IDUserSerializer

class NewIDUserViewSet(viewsets.ModelViewSet):
    queryset = NewIDUser.objects.all().order_by('first_name')
    serializer_class = NewIDUserSerializer