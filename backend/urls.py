"""backend URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Cadmium Backend API",
        default_version="v1",
        description="Part of project cadium",
        terms_of_service="https://github.com/project-cadmium/cadmium-backend/blob/main/LICENSE.txt",
        contact=openapi.Contact(email="kartimothy@gmail.com"),
        license=openapi.License(name="AGPL-3.0-or-later"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

urlpatterns = [
    path('admin/', admin.site.urls),

    # auth
    path('api-auth/', include('rest_framework.urls')),
    path('api/v1/auth/', include('dj_rest_auth.urls')),
    path('api/v1/auth/registration/', include('dj_rest_auth.registration.urls')),

    # apps
    path('api/v1/instructors/', include('instructors.urls')),
    path('api/v1/courses/', include('courses.urls')),

    # docs
    path('swagger/', schema_view.with_ui(
        'swagger', cache_timeout=0), name="schema-swagger-ui"),
    path('redoc/', schema_view.with_ui(
        'redoc', cache_timeout=0), name="schema-redoc"),
]
