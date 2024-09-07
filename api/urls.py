# from django.urls import path
# from . import views

# app_name = 'api'

# urlpatterns = [
#     path('<path:short_code>/', views.redirect_to_url, name='redirect'),
#     path('shorten/', views.shorten, name='shorten'),
#     path('retrieve/', views.retrive, name='retrive'),
#     path('update/', views.update, name='update'),
#     path('delete/', views.delete, name='delete'),
# ]
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import UrlShortenerViewSet, redirect_to_url

router = DefaultRouter()
router.register(r'shorten', UrlShortenerViewSet, basename='shorten')

urlpatterns = [
    path('', include(router.urls)),
    path('shorten/<str:short_code>/stats/', UrlShortenerViewSet.as_view({'get': 'stats_retrieve'}), name='shortlink-partial-update'),
    path('<str:short_code>/', redirect_to_url, name='redirect_to_url'),  # This should be last
]
