from django.urls import path
from .views import redirect_user

app_name = 'redirect'

urlpatterns = [
    path('<str:short_code>/', redirect_user, name='redirect'),
]
