from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status

from api.serializers import GhostPostSerializer
from ghostpost.models import GhostPost

class GhostPostViewSet(ModelViewSet):
    serializer_class = GhostPostSerializer
    queryset = GhostPost.objects.all()

    @action(detail=False)
    def boast(self, request):
        boast = GhostPost.objects.filter(post_type = "Boast").order_by('-created_at')

        serializer = self.get_serializer(boast, many=True)
        return Response(serializer.data)
    
    @action(detail=False)
    def roast(self, request):
        roast = GhostPost.objects.filter(post_type = "Roast").order_by('-created_at')
        
        serializer = self.get_serializer(roast, many=True)
        return Response(serializer.data)

    @action(detail=False)
    def highest(self, request):
        highest_rated = sorted(GhostPost.objects.all(), key=lambda t: t.score, reverse=True)
        
        serializer = self.get_serializer(highest_rated, many=True)
        return Response(serializer.data)
    
    @action(detail=True, methods=['post'])
    def upvote(self, request, pk=None):
        vote = GhostPost.objects.filter(id=pk).first()
        vote.upvote += 1
        vote.save()
        return Response({'status': ' upvote set'})

    @action(detail=True, methods=['post'])
    def downvote(self, request, pk=None):
        vote = GhostPost.objects.filter(id=pk).first()
        vote.downvote += 1
        vote.save()
        return Response({'status': ' downvote set'})
