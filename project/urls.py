# project/urls.py
from django.contrib import admin
from django.urls import path, include


from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from .views import UserStatus

schema_view = get_schema_view(
    openapi.Info(
        title="xSidra Forums API",
        default_version='v1',
        description="xSidra Forums API ",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@xsidra.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/', include('jobs.routes')),
    path('api/user/status/', UserStatus.as_view(), name='user-status'),
]


urlpatterns += [
    path('api/swagger/', schema_view.with_ui('swagger',
         cache_timeout=0), name='schema-swagger-ui'),
    path('api/docs/', schema_view.with_ui('redoc',
                                          cache_timeout=0), name='schema-redoc'),
]
