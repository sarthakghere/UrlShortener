from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('shorten/', views.shorten, name='shorten'),
    path('retrieve/', views.retrive, name='retrive'),
    path('update/', views.update, name='update'),
    path('delete/', views.delete, name='delete'),
]
