import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.core.files.storage import default_storage
from django.core.files.images import ImageFile
from django.conf import settings

from quickstart.models import IDUser

class FileUploadView(APIView):

    def put(self, request, filename, format=None):
        data = request.FILES['file']

        path =  default_storage.save('uploader/newUserIdPicture/'+filename, ImageFile(data))
        tmp_file = os.path.join(settings.BASE_DIR, path)

        return Response(status=204)

class ListUsers(APIView):
    def post(self, request, format=None):
        message = request.data
        print(message)
        return Response(status=204)