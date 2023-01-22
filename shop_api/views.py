from rest_framework import mixins, status
from rest_framework.generics import CreateAPIView, get_object_or_404
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from shop_api.serializers import *
from shop_api.models import *


class BrandViewSet(ModelViewSet):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


class CategoryViewSet(ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class OrderViewSet(ModelViewSet):
    queryset = Order.objects.all()
    serializer_class = OrderSerializer


class ProductInOrderViewSet(ModelViewSet):
    queryset = ProductInOrder.objects.all()
    serializer_class = ProductInOrderSerializer


class LikeAPIView(CreateAPIView):
    serializer_class = LikeSerializer

    def post(self):
        if Like.objects.get(user=self.request.user, product_id=self.kwargs['pk']):
            remote_like = Like.objects.get(user=self.request.user, product_id=self.kwargs['pk'])
            remote_like.delete()
        else:
            Like.objects.create(user=self.request.user, product_id=self.kwargs['pk'])



class ProductPhotoCreateView(APIView):
    parser_class = (MultiPartParser, FormParser)

    def post(self, request, product_id, format=None):
        product = get_object_or_404(Product, id=product_id)
        serializer = ProductPhotoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(product=product)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)




class MainPageViewSet(mixins.ListModelMixin, GenericViewSet):
    queryset = Product.objects.all()
    serializer_class = MainPageSerializer
