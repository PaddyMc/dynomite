from django.conf.urls import url, include
from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static

from rest_framework import routers

from quickstart import views
from uploader import views as uploader_views
from quickstart.models import IDUser, NewIDUser

router = routers.DefaultRouter()
router.register(r'idusers', views.IDUserViewSet)
router.register(r'newidusers', views.NewIDUserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^upload/(?P<filename>[^/]+)$', uploader_views.FileUploadView.as_view()),
] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
