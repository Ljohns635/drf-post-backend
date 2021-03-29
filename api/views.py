from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet

from api.serializers import GhostPostSerializer
from ghostpost.models import GhostPost

class GhostPostViewSet(ModelViewSet):
    serializer_class = GhostPostSerializer
    queryset = GhostPost.objects.all()