from django.shortcuts import render

from django.contrib.auth.models import User, Group
from quickstart.models import IDUser
from rest_framework import viewsets
from quickstart.serializers import UserSerializer, GroupSerializer, IDUserSerializer


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    queryset = Group.objects.all()
    serializer_class = GroupSerializer

class IDUserViewSet(viewsets.ModelViewSet):
    queryset = IDUser.objects.all().order_by('first_name')
    serializer_class = IDUserSerializer
