from django.urls import path
from . import views

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    #ex: //localHost:8080
    path('', views.index, name = 'index'),

    #ex: //localhost:8080/2
    path('<int:project_id>', views.detail, name = 'detail'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)