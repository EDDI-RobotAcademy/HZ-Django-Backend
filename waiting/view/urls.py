from django.urls import path, include
from rest_framework.routers import DefaultRouter

from view.controller.view import ViewView

router = DefaultRouter()
router.register(r'view', ViewView, basename='view')

urlpatterns = [
    path('', include(router.urls)),
    path('create', ViewView.as_view({'post': 'create'}), name='view-create'),
]
