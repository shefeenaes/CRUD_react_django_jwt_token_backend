
from django.urls import path
from rest_framework.documentation import include_docs_urls
from rest_framework.schemas import get_schema_view
from . import views
from .views import *
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework import permissions
from rest_framework_simplejwt.views import (
    TokenRefreshView,
)
schema_view = get_schema_view(
    openapi.Info(
        title="API Documentation",
        default_version='v1',
        description="Your API description",
        terms_of_service="https://www.example.com/terms/",
        contact=openapi.Contact(email="contact@example.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)
urlpatterns = [
    path('profile/', views.get_profile),
    path('logout/', views.logout_view),
    path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('showAllProducts/', views.showAllProducts, name='show-all'),
    path('addProduct/', views.addProduct, name='add-product'),
    path('updateProduct/<int:pk>/', views.updateProduct, name='update-student'),
    path('deleteProduct/<int:pk>/', views.deleteProduct, name='delete-student'),
    path('showProduct/<int:pk>/', views.showProduct, name='show-single'),
     path('docs/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
