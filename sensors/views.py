from rest_framework import viewsets, generics
from rest_framework.permissions import IsAuthenticated
from .models import Sensor, Data, Alert
from .serializers import SensorSerializer, DataSerializer, AlertSerializer, UserRegistrationSerializer
from django.contrib.auth.models import User
from rest_framework.permissions import AllowAny


class UserRegistrationView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]

class SensorViewSet(viewsets.ModelViewSet):
    queryset = Sensor.objects.all()
    serializer_class = SensorSerializer
    permission_classes = [IsAuthenticated]

class DataViewSet(viewsets.ModelViewSet):
    queryset = Data.objects.all()
    serializer_class = DataSerializer
    permission_classes = [IsAuthenticated]

class AlertViewSet(viewsets.ModelViewSet):
    queryset = Alert.objects.all()
    serializer_class = AlertSerializer
    permission_classes = [IsAuthenticated]
