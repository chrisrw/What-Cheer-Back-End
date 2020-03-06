from django.urls import path,include
from . import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
    TokenVerifyView
)

urlpatterns = [
    path('entries/', views.EntryList.as_view(), name='entry_list'),
    path('entries/<int:pk>/', views.EntryDetail.as_view(), name='entry_detail'),
    # path('entries/<int:pk>/edit/', views.EntryDetail.as_view(), name='entry_edit'),
    # path('entries/create/', views.EntryDetail.as_view(), name='entry_create'),
    # path('entries/<int:pk>/', views.EntryDetail.as_view(), name='entry_delete'),
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('signup/', views.UserList.as_view(), name='user_create')
    
]