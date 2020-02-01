from django.urls import path
from .views import home

app_name = 'storage'

urlpatterns = [
    path('', home, name='home'),
]
