#archivo urls de django tiene que tener mi proyecto para que me deje verlo en la web
from django.contrib import admin
from django.urls import path,include
from django.conf import settings #archivo settings.py

from django.conf.urls.static import static #ubicaciones estaticas

urlpatterns = [
    path('admin/', admin.site.urls),

    #cuando alguien no escriba nada incluye la carpeta webcaosnew y trae sus urls
    path('',include('webCaosNew.urls')),
]


#FOTOS 
if settings.DEBUG:
    urlpatterns+=static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)


admin.site.site_header="NoticiasCaosNew"
admin.site.index_title="Administracion NoticiasCaosNew"
admin.site.site_title="NoticiasCaosNew"