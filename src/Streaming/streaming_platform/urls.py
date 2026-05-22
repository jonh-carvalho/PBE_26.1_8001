from django.contrib import admin
from django.urls import include, path
from drf_spectacular.views import (
   SpectacularAPIView,
   SpectacularSwaggerView,
   SpectacularRedocView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('content_app.urls')),

    # Schema OpenAPI
   path('api/schema/', SpectacularAPIView.as_view(), name='schema'),

   # UIs de documentação
   path('api/docs/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
   path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
]
