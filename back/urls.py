from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from productos.urls import productos_patterns
from profiles.urls import profiles_patterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('productos/', include(productos_patterns)),
    path('', include('core.urls')),
    # autenticación
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/', include('registration.urls')),
    path('profile/', include(profiles_patterns)),


]
if settings.DEBUG:
    from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
