
from django.urls import path
from . import views
from .views import *
from rest_framework_simplejwt.views import (
    TokenRefreshView,
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
]
