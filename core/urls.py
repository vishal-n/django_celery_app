from django.urls import path
from .views import square_view

urlpatterns = [
    path('square/', square_view),
]
