from django.urls import path, include
from rest_framework.routers import DefaultRouter

from drinkcart.controller.views import DrinkcartView

router = DefaultRouter()
router.register(r'drinkcart', DrinkcartView, basename='drinkcart')

urlpatterns = [
    path('', include(router.urls)),
    path('list', DrinkcartView.as_view({'post': 'drinkcartItemList'}), name='drinkcart-list'),
    path('register', DrinkcartView.as_view({'post': 'drinkcartRegister'}), name='drinkcart-register'),
    path('remove', DrinkcartView.as_view({'post': 'drinkcartRemove'}), name='drinkcart-remove'),
]

# localhost:8000/board/list