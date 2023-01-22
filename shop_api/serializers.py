from rest_framework import serializers
from shop_api.models import *


class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'


class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ('id', 'color')


class ProductPhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductPhoto
        fields = ('id', 'image')

        def create(self, validated_data):
            product = validated_data.pop('product')
            product_photo = ProductPhoto.objects.create(product=product, **validated_data)
            return product_photo


class ProductSerializer(serializers.ModelSerializer):
    category = CategorySerializer()
    brand = BrandSerializer()
    colors = ColorSerializer(many=True, read_only=True)
    photos = ProductPhotoSerializer(many=True, read_only=True)
    likes_count = serializers.SerializerMethodField()
    comments_count = serializers.SerializerMethodField()

    def get_photos(obj):
        photos = obj.photos.all()
        return [photo.image.url for photo in photos]

    def get_likes_count(self, obj):
        return obj.product_likes.count()

    def get_comments_count(self, obj):
        return obj.product_comments.count()

    class Meta:
        model = Product
        fields = ('id', 'category', 'brand', 'name', 'description', 'vendor_code', 'sex', 'new', 'is_product_in_stock',
                  'colors', 'photos', 'likes_count', 'comments_count')


class OrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = Order
        fields = '__all__'


class ProductInOrderSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductInOrder
        fields = '__all__'


class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Like
        fields = ('product',)


class MainPageSerializer(serializers.ModelSerializer):
    brand = BrandSerializer(many=False)
    category = CategorySerializer(many=False)

    class Meta:
        model = Product
        fields = '__all__'

