import os

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import authentication, permissions

from django.core.files.storage import default_storage
from django.core.files.images import ImageFile
from django.conf import settings

class FileUploadView(APIView):

    def put(self, request, filename, format=None):
        data = request.FILES['file']

        path =  default_storage.save('uploader/newUserIdPicture/'+filename, ImageFile(data))
        tmp_file = os.path.join(settings.BASE_DIR, path)

        return Response(status=204)
