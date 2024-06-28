from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drinkorders.controller.views import DrinkordersView

router = DefaultRouter()
router.register(r'drinkorders', DrinkordersView, basename='drinkorders')

urlpatterns = [
    path('', include(router.urls)),
    path('create', DrinkordersView.as_view({'post': 'createDrinkorders'}), name='drinkorder-create'),
]
