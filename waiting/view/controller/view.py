from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response

from oauth.service.redis_service_impl import RedisServiceImpl
from view.serializers import ViewSerializer
from view.service.view_service_impl import ViewServiceImpl


class ViewView(viewsets.ViewSet):
    viewService = ViewServiceImpl.getInstance()

    def create(self, request):
        serializer = ViewSerializer(data=request.data)

        if serializer.is_valid():
            view = self.viewService.createView(serializer.validated_data)
            return Response(ViewSerializer(view).data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)