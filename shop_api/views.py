from rest_framework.viewsets import ModelViewSet
from shop_api.serializers import ProductSerializer, MainPageSerializer
from shop_api.models import *


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class MainPageViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = MainPageSerializer
