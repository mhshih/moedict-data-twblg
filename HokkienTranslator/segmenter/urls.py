from segmenter import views
from django.urls import path

urlpatterns = [
    path("", views.home),
    path("translate", views.translate)
]
