from django.urls import path, include
from rest_framework import routers
from shop_api.views import *

router = routers.SimpleRouter()
router.register('brands', BrandViewSet)
router.register('category', CategoryViewSet)
router.register('products', ProductViewSet)
router.register('order', OrderViewSet)
router.register('product-in-order', ProductInOrderViewSet)
router.register('main-page', MainPageViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('like/', LikeAPIView.as_view(), name='like'),
]
