from django.urls import path, include
from rest_framework import routers
from shop_api.views import *

router = routers.SimpleRouter()
router.register('products', ProductViewSet)
router.register('main-page', MainPageViewSet)

urlpatterns = [
    path('', include(router.urls))
]
