from rest_framework.views import APIView
from rest_framework.request import Request
from rest_framework.response import Response
from rest_framework import status
from rest_framework import generics
from rest_framework import mixins
from rest_framework import permissions
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import SearchFilter, OrderingFilter


from .models import Product
from .serializers import ProductSerializer
from .permissions import MyPermission


class ProductAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.order_by('-id')
    serializer_class = ProductSerializer
    permission_classes = [permissions.DjangoModelPermissions]
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]
    filterset_fields = ['price', 'quantity', 'category']
    search_fields = ['name', 'description', 'category__name']
    ordering_fields = ['id', 'price', 'quantity', 'date_to', 'category']

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
    permission_classes = [MyPermission]




    # lookup_url_kwarg = "product_id"
    # lookup_field = 'pk'


# class ProductAPIView(generics.GenericAPIView,
#                      mixins.ListModelMixin,
#                      mixins.CreateModelMixin,
#                      mixins.RetrieveModelMixin,
#                      mixins.DestroyModelMixin,
#                      mixins.UpdateModelMixin):
#
#     queryset = Product.objects.all()
#     serializer_class = ProductSerializer

    # def get(self, request, *args, **kwargs):
    #     if not self.kwargs.get("pk"):
    #         return self.list(request, *args, **kwargs)
    #     else:
    #         return self.retrieve(request, *args, **kwargs)
    #
    # def post(self, request, *args, **kwargs):
    #     return self.create(request, *args, **kwargs)
    #
    # def put(self, request, *args, **kwargs):
    #     return self.update(request, *args, **kwargs)
    #
    # def delete(self, request, *args, **kwargs):
    #     return self.destroy(request, *args, **kwargs)






# class ProductAPIView(APIView):
#     def get(self, request: Request, pk: int = None):
#         if not pk:
#             products = Product.objects.all()
#             serializer = ProductSerializer(products, many=True)
#             return Response(serializer.data)
#         else:
#             try:
#                 product = Product.objects.get(pk=pk)
#                 serializer = ProductSerializer(product)
#                 return Response(serializer.data)
#             except Exception as e:
#                 return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#
#     def post(self, request, pk: int = None):
#         if pk:
#             return Response({"message": "Method POST not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             serializer = ProductSerializer(data=request.data)
#             serializer.is_valid(raise_exception=True)
#             product = serializer.save()
#             return Response(ProductSerializer(product).data, status=status.HTTP_201_CREATED)
#
#     def put(self, request, pk: int = None):
#         if not pk:
#             return Response({"message": f"Method {request.method} not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             try:
#                 product = Product.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#
#             serializer = ProductSerializer(instance=product, data=request.data, partial=True if request.method == 'PATCH' else False)
#             serializer.is_valid(raise_exception=True)
#             product = serializer.save()
#             return Response(ProductSerializer(product).data)
#
#     def patch(self, request, pk: int = None):
#         return self.put(request, pk)
#
#     def delete(self, request: Request, pk: int = None):
#         if not pk:
#             return Response({"message": "Method DELETE not allowed"}, status=status.HTTP_405_METHOD_NOT_ALLOWED)
#         else:
#             try:
#                 product = Product.objects.get(pk=pk)
#             except Exception as e:
#                 return Response({"message": "Product not found"}, status=status.HTTP_404_NOT_FOUND)
#
#             product.delete()
#             return Response({"message": "Product deleted Successfully!!!"}, status=status.HTTP_204_NO_CONTENT)