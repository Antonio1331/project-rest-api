from rest_framework import generics, permissions
from .models import Brand, Color, Product
from .serializers import BrandSerializer, ColorSerializer, ProductSerializer


class BrandAPIView(generics.ListCreateAPIView):
    queryset = Brand.objects.order_by('-id')
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = self.queryset.all()
        return q

    def get_serializer_class(self):
        if self.request.user.is_staff:
            s = BrandSerializer
        else:
            s = self.serializer_class
        return s


class BrandDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer
    permission_classes = [permissions.IsAuthenticated]


class ColorAPIView(generics.ListCreateAPIView):
    queryset = Color.objects.order_by('-id')
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = self.queryset.all()
        return q

    def get_serializer_class(self):
        if self.request.user.is_staff:
            s = ColorSerializer
        else:
            s = self.serializer_class
        return s


class ColorDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Color.objects.all()
    serializer_class = ColorSerializer
    permission_classes = [permissions.IsAuthenticated]


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        q = self.queryset.all()
        return q

    def get_serializer_class(self):
        if self.request.user.is_staff:
            s = ProductSerializer
        else:
            s = self.serializer_class
        return s


class ProductDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.IsAuthenticated]
