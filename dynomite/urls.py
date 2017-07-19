from django.conf.urls import url, include
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from quickstart.models import IDUser, NewIDUser

from quickstart import views
from uploader import views as uploader_views
from login import views as login_views
from register_new_user import views as register_new_user_views

from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'idusers', views.IDUserViewSet)
router.register(r'newidusers', views.NewIDUserViewSet)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^upload/(?P<filename>[^/]+)$', uploader_views.FileUploadView.as_view()),
    url(r'^hope/$', uploader_views.ListUsers.as_view()),
    url(r'^login/(?P<email>.+)/$', login_views.IDUserList.as_view()),
    url(r'^registernewuser/', include('register_new_user.urls')),

] + static(settings.STATIC_URL, document_root=settings.MEDIA_ROOT)
