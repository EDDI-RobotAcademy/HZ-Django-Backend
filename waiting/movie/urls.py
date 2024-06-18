from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie.controller.views import MovieView

router = DefaultRouter()
router.register(r'movie', MovieView)

urlpatterns = [
    path('', include(router.urls)),
    path('list/', MovieView.as_view({'get': 'list'}), name='movie-list'),
    path('register', MovieView.as_view({'post': 'register'}), name='movie-register'),
    path('read/<int:pk>', MovieView.as_view({'get': 'readMovie'}), name='movie-read'),
    path('delete/<int:pk>', MovieView.as_view({'delete': 'removeMovie'}), name='movie-remove'),
    path('modify/<int:pk>', MovieView.as_view({'put': 'modifyMovie'}), name='movie-modify'),
]

# localhost:8000/movie/list