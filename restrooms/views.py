from .models import Toilet
from rest_framework import viewsets, permissions
from .serializers import ToiletSerializer

class ToiletViewSet(viewsets.ModelViewSet):
    queryset=Toilet.objects.all()
    serializer_class=ToiletSerializer
    permission_classes=[permissions.AllowAny]