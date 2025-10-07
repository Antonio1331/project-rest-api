from rest_framework import generics, permissions, filters, throttling
from django_filters.rest_framework import DjangoFilterBackend
from .models import Brand, Color, Product
from .serializers import BrandSerializer, ColorSerializer, ProductSerializer
from .permissions import IsStaffOrReadOnly


class BrandAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.order_by('-id')
    serializer_class = BrandSerializer
    permission_classes = [
        permissions.DjangoModelPermissions | IsStaffOrReadOnly
    ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['-id']


class BrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [
        permissions.DjangoModelPermissions | IsStaffOrReadOnly
    ]


class ColorAPIView(generics.ListCreateAPIView):
    queryset = Color.objects.order_by('-id')
    serializer_class = ColorSerializer
    permission_classes = [
        permissions.DjangoModelPermissions | IsStaffOrReadOnly
    ]
    filter_backends = [filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name']
    ordering_fields = ['id', 'name']
    ordering = ['-id']


class ColorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [
        permissions.DjangoModelPermissions | IsStaffOrReadOnly
    ]


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.DjangoModelPermissions | IsStaffOrReadOnly
    ]
    filter_backends = [
        DjangoFilterBackend,
        filters.SearchFilter,
        filters.OrderingFilter
    ]
    filterset_fields = ['brand', 'color', 'category']
    search_fields = ['name', 'description']
    ordering_fields = ['price', 'make_date', 'quantity']
    ordering = ['-id']


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [
        permissions.DjangoModelPermissions | IsStaffOrReadOnly
    ]
