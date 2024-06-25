from django.urls import path, include
from rest_framework.routers import DefaultRouter

from foodcart.controller.views import FoodcartView

router = DefaultRouter()
router.register(r'foodcart', FoodcartView, basename='foodcart')

urlpatterns = [
    path('', include(router.urls)),
    path('list', FoodcartView.as_view({'post': 'foodcartItemList'}), name='foodcart-list'),
    path('register', FoodcartView.as_view({'post': 'foodcartRegister'}), name='foodcart-register'),
    path('remove', FoodcartView.as_view({'post': 'foodcartRemove'}), name='foodcart-remove'),
]

# localhost:8000/board/list