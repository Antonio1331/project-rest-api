from django.urls import path

from .views import ProductAPIView, ProductDetailAPIView

urlpatterns = [
    path('products/', ProductAPIView.as_view()),
    path('products/<int:pk>/', ProductDetailAPIView.as_view()),
]
