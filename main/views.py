from rest_framework import generics
from . import models
from . import serializers
from rest_framework.permissions import IsAuthenticated,IsAuthenticatedOrReadOnly
from rest_framework.authentication import TokenAuthentication

class MainListView(generics.ListCreateAPIView):
    queryset = models.Main.objects.all()
    serializer_class = serializers.MainSerializer
    permission_classes = [IsAuthenticatedOrReadOnly]
