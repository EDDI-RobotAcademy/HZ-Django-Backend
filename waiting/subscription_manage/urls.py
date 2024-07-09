from django.urls import path, include
from rest_framework.routers import DefaultRouter

from subscription_manage.controller.views import SubscriptionManageView

router = DefaultRouter()
router.register(r'subscription_manage', SubscriptionManageView, basename='subscription_manage')

urlpatterns = [
    path('', include(router.urls)),
    path('list/', SubscriptionManageView.as_view({'get': 'list'}), name='subscription_manage-list'),
    path('register', SubscriptionManageView.as_view({'post': 'register'}), name='subscription_manage-register'),
    path('read/<int:pk>', SubscriptionManageView.as_view({'get': 'readSubscriptionManage'}), name='subscription_manage-read'),
    path('delete/<int:pk>', SubscriptionManageView.as_view({'delete': 'removeSubscriptionManage'}), name='subscription_manage-remove'),
    path('modify/<int:pk>', SubscriptionManageView.as_view({'put': 'modifySubscriptionManage'}), name='subscription_manage-modify'),
]
