from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('index.urls')),
    path('joint/', include('joint.urls')),
    path('order/', include('order.urls')),
    path('curcy/', include('curcy.urls')),
    path('perso/', include('perso.urls')),
    path('cabin/', include('cabin.urls')),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
