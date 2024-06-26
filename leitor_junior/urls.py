from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path("", include('livro.urls')),
    path("admin/", admin.site.urls),
    path("livro/", include('livro.urls')),
    path("auth/", include('usuarios.urls'))
]

urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
