from django.urls import path

from . import views

urlpatterns = [
    path("character/<int:id>/", views.character),
]
