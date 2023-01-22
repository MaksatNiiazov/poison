from rest_framework import serializers
from shop_api.models import *


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class MainPageSerializer(serializers.ModelSerializer):
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = '__all__'

