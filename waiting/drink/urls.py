from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drink.controller.views import DrinkView

router = DefaultRouter()
router.register(r'drink', DrinkView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', DrinkView.as_view({'get': 'list'}), name='drink-list'),
    path('register', DrinkView.as_view({'post': 'register'}), name='drink-register'),
    path('read/<int:pk>', DrinkView.as_view({'get': 'readDrink'}), name='drink-read'),
    path('delete/<int:pk>', DrinkView.as_view({'delete': 'removeDrink'}), name='drink-remove'),
    path('modify/<int:pk>', DrinkView.as_view({'put': 'modifyDrink'}), name='drink-modify'),
]

# localhost:8000/drink/list