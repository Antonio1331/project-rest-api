from rest_framework import serializers
from django.core.validators import MinValueValidator
from .models import Brand, Color, Product


class BrandSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)

    def create(self, validated_data):
        return Brand.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ColorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)

    def create(self, validated_data):
        return Color.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance


class ProductSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=255)
    description = serializers.CharField(required=False, allow_blank=True)
    price = serializers.IntegerField(validators=[MinValueValidator(0)])
    quantity = serializers.IntegerField(default=10)
    make_date = serializers.DateTimeField()
    date_to = serializers.IntegerField(default=7)
    category_id = serializers.IntegerField()
    brand_id = serializers.IntegerField(required=False, allow_null=True)
    color_id = serializers.IntegerField(required=False, allow_null=True)

    def create(self, validated_data):
        return Product.objects.create(**validated_data)

    def update(self, instance, validated_data):
        for key, value in validated_data.items():
            setattr(instance, key, value)
        instance.save()
        return instance
