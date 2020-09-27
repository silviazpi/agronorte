from django.contrib import admin
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path
from gestionProductos.views import (
    home,
    productos, 
    producto,
    contacto,
    about,
    ocasion,
    chollo,
    aviso)

    
admin.site.site_header = "Agro Importaciones Norte"
admin.site.site_title = "Agro Importaciones Norte"
admin.site.index_title = "Bienvenido"


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name='home'),
    path('index/', home, name='home'),
    path('productos/', productos, name='productos'),
    path('productos/<slug>/', producto, name='producto'),
    path('about/', about, name='about'),      
    path('contacto/', contacto, name='contacto'),   
    path('ocasion/', ocasion, name='ocasion'),
    path('ocasion/<slug>/', chollo, name='chollo'),
    path('aviso/', aviso, name='aviso'),
]


if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
