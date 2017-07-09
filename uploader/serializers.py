import os

from django.core.files.storage import default_storage
from django.core.files.images import ImageFile
from django.conf import settings
from django.core.files.uploadhandler import FileUploadHandler


class FileUploadView(APIView):
    #parser_classes = (FileUploadParser,)

    def put(self, request, filename, format=None):
        data = request.FILES['file']

        path =  default_storage.save('newUserIdPicture/'+filename, ImageFile(data))
        tmp_file = os.path.join(settings.BASE_DIR, path)

        return Response(status=204)