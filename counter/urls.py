from django.urls import path

from .views import word_count_view, about

urlpatterns = [
    path('', word_count_view, name='word_count'),
    path('about/', about, name='about')

]
