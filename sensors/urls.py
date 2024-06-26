from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import SensorViewSet, DataViewSet, AlertViewSet, UserRegistrationView


router = DefaultRouter()
router.register(r'sensors', SensorViewSet)
router.register(r'data', DataViewSet)
router.register(r'alerts', AlertViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('register/', UserRegistrationView.as_view(), name='user-register'),
]
