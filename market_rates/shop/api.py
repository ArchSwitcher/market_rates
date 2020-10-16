from rest_framework import viewsets, permissions
from .models import (
    Product,
    Category,
    Quote
)
from .serializers import (
    ProductSerializer,
    CategorySerializer,
    QuoteSerializer,
)

#Product Viewset
class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = ProductSerializer


class CategoryViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]

    serializer_class = CategorySerializer