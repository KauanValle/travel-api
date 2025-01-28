from django.contrib import admin
from django.urls import path
from .api import api

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Travel API",
        default_version='v1',
        description="Documentação da API",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="kauanvalle3@gmail.com"),
        license=openapi.License(name="Licença BSD"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', api.urls),
]
