from django.shortcuts import render, get_object_or_404, redirect
from .models import ShortLink
from .serializers import ShortLinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .linkhandler import LinkHandler
from django.http import Http404
from django.core.exceptions import ImproperlyConfigured
from rest_framework import viewsets

class UrlShortenerViewSet(viewsets.ModelViewSet):
    queryset = ShortLink.objects.all()
    lookup_field = 'short_code'

    def create(self, request):
        url = request.data.get('url')
        if not url:
            return Response({'error': 'No url provided'}, status=status.HTTP_400_BAD_REQUEST)
        
        if not LinkHandler.is_valid_url(url):
            return Response({'error': 'Invalid url format'}, status=status.HTTP_400_BAD_REQUEST)

        if ShortLink.objects.filter(url=url).exists():
            shortened_link = ShortLink.objects.get(url=url)
            serializer = ShortLinkSerializer.RetrivalSerializer(shortened_link)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        short_code = LinkHandler.shorten_link()  # Generate a short code
        shortened_link = ShortLink.objects.create(
            url=url,
            short_code=short_code
        )
        serializer = ShortLinkSerializer.RetrivalSerializer(shortened_link)
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    
    def retrieve(self, request, short_code=None):
        try:
            short_link = ShortLink.objects.get(short_code=short_code)
        except ShortLink.DoesNotExist:
            return Response({'error': 'Short code not found'}, status=status.HTTP_404_NOT_FOUND)

        serializer = ShortLinkSerializer.RetrivalSerializer(short_link)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, short_code=None):
        updated_url = request.data.get('updated_url')

        if not updated_url:
            return Response({'error': 'No updated url provided'}, status=status.HTTP_400_BAD_REQUEST)

        if not LinkHandler.is_valid_url(updated_url):
            return Response({'error': 'Invalid url format'}, status=status.HTTP_400_BAD_REQUEST)

        try:
            short_link = ShortLink.objects.get(short_code=short_code)
        except ShortLink.DoesNotExist:
            return Response({'error': 'Short code not found'}, status=status.HTTP_404_NOT_FOUND)

        short_link.url = updated_url
        short_link.accessCount = 0  # Reset access count if needed
        short_link.save()

        serializer = ShortLinkSerializer.RetrivalSerializer(short_link)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def destroy(self, request, short_code=None):
        if LinkHandler.short_link_exists(short_code):
            short_link = ShortLink.objects.get(short_code=short_code)
        else:
            return Response({'error': 'Invalid short code'}, status=status.HTTP_404_NOT_FOUND)
        short_link.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    def stats_retrieve(self, request, short_code=None):
        if LinkHandler.short_link_exists(short_code):
            short_link = ShortLink.objects.get(short_code=short_code)
        else:
            return Response({
                'error': 'Invalid short code'
            }, status=status.HTTP_404_NOT_FOUND)
        
        serializer = ShortLinkSerializer.StatsSerializer(short_link)
        return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def redirect_to_url(request,short_code):
    try:
        short_link = ShortLink.objects.get(short_code=short_code)
    except ShortLink.DoesNotExist:
        return Response({'error': 'Invalid short_code'}, status=status.HTTP_404_NOT_FOUND)
    short_link.accessCount += 1
    short_link.save()
    return redirect(short_link.url)