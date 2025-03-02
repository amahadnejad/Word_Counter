from django.urls import path

from .views import word_count_view

urlpatterns = [
    path('', word_count_view, name='word_count')
]
