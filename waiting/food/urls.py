from django.urls import path, include
from rest_framework.routers import DefaultRouter

from food.controller.views import FoodView

router = DefaultRouter()
router.register(r'food', FoodView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', FoodView.as_view({'get': 'list'}), name='food-list'),
    path('register', FoodView.as_view({'post': 'register'}), name='food-register'),
    path('read/<int:pk>', FoodView.as_view({'get': 'readFood'}), name='food-read'),
    path('delete/<int:pk>', FoodView.as_view({'delete': 'removeFood'}), name='food-remove'),
    path('modify/<int:pk>', FoodView.as_view({'put': 'modifyFood'}), name='food-modify'),
]

# localhost:8000/food/list