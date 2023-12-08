from django.urls import path

from . import views

urlpatterns = [
    path('',views.home, name='home'),
    path('savedata/',views.save_data, name='save'),
    path("delete-data/", views.delete_data, name='delete'),
    path("edit-data/", views.edit_data, name='edit')
]
