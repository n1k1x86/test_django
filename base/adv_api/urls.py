# urls.py
from django.urls import path
from .views import AdvModelListCreateAPIView, AdvModelRetrieveUpdateAPIView

urlpatterns = [
    path('adv_items/', AdvModelListCreateAPIView.as_view()),
    path('adv_items/<int:pk>/', AdvModelRetrieveUpdateAPIView.as_view()),
]
