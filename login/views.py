from django.shortcuts import render

from quickstart.models import IDUser
from quickstart.serializers import IDUserSerializer
from rest_framework import generics

class IDUserList(generics.ListAPIView):
    serializer_class = IDUserSerializer

    def get_queryset(self):
        login_email = self.kwargs['email']
        return IDUser.objects.filter(email=login_email)