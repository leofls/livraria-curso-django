"""livraria URL Configuration

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
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)
from rest_framework import routers

from drf_spectacular.views import SpectacularAPIView, SpectacularRedocView, SpectacularSwaggerView

from core import views

router = routers.DefaultRouter()
router.register(r"categorias", views.CategoriaViewSet)
router.register(r"editoras", views.EditoraViewSet)
router.register(r"autores", views.AutorViewSet)
router.register(r"livros", views.LivroViewSet)
router.register(r'compras', views.CompraViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),

     # OpenAPI 3
    path('api/schema/', SpectacularAPIView.as_view(), name='schema'),
    path('api/swagger/', SpectacularSwaggerView.as_view(url_name='schema'), name='swagger-ui'),
    path('api/redoc/', SpectacularRedocView.as_view(url_name='schema'), name='redoc'),
    # Autenticação
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Endpoints 
    path('teste/', views.teste),
    path('teste2/', views.teste2),
    path('categorias-class/', views.CategoriaView.as_view()),
    path('categorias-class/<int:id>/', views.CategoriaView.as_view()),
    path('categorias-apiview/', views.CategoriasList.as_view()),
    path('categorias-apiview/<int:id>/', views.CategoriaDetail.as_view()),
    path('categorias-generic/', views.CategoriasListGeneric.as_view()),
    path('categorias-generic/<int:id>/', views.CategoriaDetailGeneric.as_view()),
    path('api/', include(router.urls))
]

urlpatterns += [
   
]