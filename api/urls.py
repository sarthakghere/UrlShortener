from django.urls import path
from . import views

app_name = 'api'

urlpatterns = [
    path('shorten/', views.shorten, name='shorten'),
    path('retrieve/', views.retrive, name='retrive'),
]
