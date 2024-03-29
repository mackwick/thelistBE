from rest_framework import viewsets, permissions
from .models import Show
from .serializers import ShowSerializer

# Create your views here.
class ShowViewSet(viewsets.ModelViewSet):
    queryset=Show.objects.all()
    serializer_class=ShowSerializer
    permisson_classes=[permissions.AllowAny]
