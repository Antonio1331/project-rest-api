from django.urls import path
from .views import (BrandAPIView, BrandDetailAPIView,ColorAPIView,
                    ColorDetailAPIView,ProductAPIView, ProductDetailAPIView
)

urlpatterns = [
    path('brands/', BrandAPIView.as_view(), name='brand-list'),
    path('brands/<int:pk>/', BrandDetailAPIView.as_view(), name='brand-detail'),
    path('colors/', ColorAPIView.as_view(), name='color-list'),
    path('colors/<int:pk>/', ColorDetailAPIView.as_view(), name='color-detail'),
    path('products/', ProductAPIView.as_view(), name='product-list'),
    path('products/<int:pk>/', ProductDetailAPIView.as_view(), name='product-detail'),
]
