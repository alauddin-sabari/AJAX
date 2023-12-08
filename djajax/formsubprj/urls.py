from django.urls import path
from .views import index, create_user
urlpatterns = [
    path('', index, name='index'),
    path('create_user/',create_user, name='create_user'),
]
