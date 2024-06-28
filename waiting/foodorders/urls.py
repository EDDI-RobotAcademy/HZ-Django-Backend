from django.urls import path, include
from rest_framework.routers import DefaultRouter

from foodorders.controller.views import FoodordersView

router = DefaultRouter()
router.register(r'foodorders', FoodordersView, basename='foodorders')

urlpatterns = [
    path('', include(router.urls)),
    path('create', FoodordersView.as_view({'post': 'createFoodorders'}), name='foodorder-create'),
]
