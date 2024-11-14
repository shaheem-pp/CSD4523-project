from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path
from django.urls.conf import include

urlpatterns = [
    path('admin/dashboard/', admin.site.urls),
    # Add your app URLs here
    # path('', include('my_app.urls')),  # Example for including app URLs

    # Include API URLs if using Django REST Framework
    path('api/', include('api.urls')),  # Uncomment if you have an `api` app
]

# Serve static and media files during development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
