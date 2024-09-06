from django.shortcuts import render
from .models import ShortLink
from .serializers import ShortLinkSerializer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.http import JsonResponse
from .linkhandler import LinkHandler

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
        return JsonResponse({'error': 'No short code provided'}, status=status.HTTP_400_BAD_REQUEST)
    
    shorten_link = ShortLink.objects.get(short_code=short_code)
    if shorten_link is None:
        return Response({
            'error': 'Short code not found'
        }, status=status.HTTP_404_NOT_FOUND)

    shorten_link.accessed += 1
    shorten_link.save()
    serializer = ShortLinkSerializer(shorten_link)
    return Response(serializer.data, status=status.HTTP_200_OK)