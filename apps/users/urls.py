from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path

from apps.users.views import UserViewSet

router = DefaultRouter()
router.register('user', UserViewSet, basename='api/users')

urlpatterns = [
    path('login/', TokenObtainPairView, name='api_login'),
    path('refresh/', TokenRefreshView, name='api_refresh')
]

urlpatterns = router.urls