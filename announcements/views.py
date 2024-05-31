from django.shortcuts import render
from .models import Announcement
from .serializers import AnnouncementSerializer
from rest_framework import status
from rest_framework.response import Response  
from rest_framework import generics 
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticatedOrReadOnly
from posts.permissions import IsOwnerOrReadOnly
from accounts.models import UserProfile
from django.db.models import Q
from django.utils.translation import gettext_lazy as _  

# Create your views here.
class ListCreateAnnouncement(generics.ListCreateAPIView):
    queryset = Announcement.objects.all()  
    serializer_class = AnnouncementSerializer  
    permission_classes = [IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        user_profile = self.request.user.user_profile
        serializer.save(creator=user_profile)  


class AnnouncementDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Announcement.objects.all()  
    serializer_class = AnnouncementSerializer  
    permission_classes = [IsOwnerOrReadOnly]


@api_view(['GET'])
@permission_classes([IsAuthenticatedOrReadOnly])
def search_announcements(request):
    query = request.GET.get('q', '')

    if not query:
        return Response({'error': _('Query parameter "q" is required.')}, status=status.HTTP_400_BAD_REQUEST)

    announcement_results = Announcement.objects.filter(  
        Q(title__icontains=query) | 
        Q(creator__user__username__icontains=query) |  
        Q(content__icontains=query)
    )

    announcement_serializer = AnnouncementSerializer(announcement_results, many=True)

    return Response({'Announcements': announcement_serializer.data})
    
