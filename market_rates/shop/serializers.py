from rest_framework import serializers

from .models import (
    Product,
    Category,
    Quote,
)

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = (
            'id',
            'name',
            'price',
            'category',
            'description'
        )


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = (
            'id',
            'name',
        )


class QuoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Quote
        fields = ('__all__')