from django.urls import path
from . import views

urlpatterns = [
    path('professionals/', views.professionals, name='professionals'),
    path('professionals/<uuid:pk>/', views.professionals_detail, name='professionals_detail')
]