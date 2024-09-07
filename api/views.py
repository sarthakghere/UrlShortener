from django.shortcuts import render, get_object_or_404
from .models import ShortLink
from .serializers import ShortLinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .linkhandler import LinkHandler
from django.http import Http404

# Create your views here.
@api_view(['POST'])
def shorten(request):
    url = request.data.get('url')
    if not url:
        return Response({'error': 'No url provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not url.startswith(('http://', 'https://')):
        return Response({'error': 'Invalid url format'}, status=status.HTTP_400_BAD_REQUEST)

    if ShortLink.objects.filter(original_link=url).exists():
        short_code = ShortLink.objects.get(original_link=url).short_code
        return Response({
        'short_code': short_code,
        'shortened_link': f'127.0.0.1:8000/{short_code}'
        }, status=status.HTTP_200_OK)
    
    short_code = LinkHandler.shorten_link()  # Generate a short code
    ShortLink.objects.create(
        original_link=url,
        short_code=short_code
    )
    return Response({
        'short_code': short_code,
        'shortened_link': f'127.0.0.1:8000/{short_code}'
        }, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def retrive(request):
    short_code = request.data.get('short_code')
    if not short_code:
        return Response({'error': 'No short code provided'}, status=status.HTTP_400_BAD_REQUEST)
    try:
        shorten_link = ShortLink.objects.get(short_code=short_code)
    except ShortLink.DoesNotExist:
        return Response({'error': "Invalid short_code"}, status=status.HTTP_404_NOT_FOUND)
    shorten_link.save()
    serializer = ShortLinkSerializer(shorten_link)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['PATCH'])
def update(request):
    short_code = request.data.get('short_code')
    updated_url = request.data.get('updated_url')
    
    if LinkHandler.short_link_exists(short_code):
        shorten_link = ShortLink.objects.get(short_code=short_code)
    else:
        return Response({'error': 'Invalid short code'}, status=status.HTTP_404_NOT_FOUND)
    
    if not updated_url:
        return Response({'error': 'No updated url provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    if not LinkHandler.is_valid_url(updated_url):
        return Response({'error': 'Invalid url format'}, status=status.HTTP_400_BAD_REQUEST)
    
    shorten_link.original_link = updated_url
    shorten_link.accessed = 0
    shorten_link.save()
    serializer = ShortLinkSerializer(shorten_link)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
def delete(request):
    short_code = request.data.get('short_code')
    if LinkHandler.short_link_exists(short_code):
        shorten_link = ShortLink.objects.get(short_code=short_code)
    else:
        return Response({'error': 'Invalid short code'}, status=status.HTTP_404_NOT_FOUND)
    shorten_link.delete()
    return Response({'message': 'Short link deleted'}, status=status.HTTP_200_OK)