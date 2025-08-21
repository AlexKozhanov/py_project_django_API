# Generic
from rest_framework.generics import (
    ListAPIView,
    CreateAPIView,
    RetrieveAPIView,
    UpdateAPIView,
    DestroyAPIView)
# Models
from netmodel.models import NetworkModel
from netmodel.serializers import NetworkModelSerializer

# Не знаю из какой группы
from rest_framework.permissions import AllowAny, IsAuthenticated, IsAdminUser, IsAuthenticatedOrReadOnly
from rest_framework.response import Response
from django.shortcuts import get_object_or_404
# Swagger
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema


# Generic
class NetworkModelListAPIView(ListAPIView):
    queryset = NetworkModel.objects.all()
    serializer_class = NetworkModelSerializer
    permission_classes = (IsAuthenticated,)


class NetworkModelCreateAPIView(CreateAPIView):
    queryset = NetworkModel.objects.all()
    serializer_class = NetworkModelSerializer
    permission_classes = (
        IsAuthenticated,
        ~IsModer,
    )

    @swagger_auto_schema(
        operation_summary="Создание урока",
        operation_description="Создание нового урока. Доступно только Автору урока (не из группы moder).",
        tags=["Уроки"],
        responses={201: NetworkModelSerializer, 403: "Forbidden (если пользователь — moder)", },
    )
    def post(self, request, *args, **kwargs):
        return super().post(request, *args, **kwargs)


class NetworkModelRetrieveAPIView(RetrieveAPIView):
    queryset = NetworkModel.objects.all()
    serializer_class = NetworkModelSerializer
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )

    @swagger_auto_schema(
        operation_summary="Детали урока",
        operation_description="Возвращает детали урока. Доступно Автору урока из группы moder.",
        tags=["Уроки"],
    )
    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)


class NetworkModelUpdateAPIView(UpdateAPIView):
    queryset = NetworkModel.objects.all()
    serializer_class = NetworkModelSerializer
    permission_classes = (
        IsAuthenticated,
        IsModer | IsOwner,
    )

    @swagger_auto_schema(
        operation_summary="Обновление урока",
        operation_description="Обновление урока. Доступно Автору урока из группы moder.",
        tags=["Уроки"],
    )
    def patch(self, request, *args, **kwargs):
        return super().patch(request, *args, **kwargs)

    @swagger_auto_schema(
        operation_summary="Полное обновление урока",
        operation_description="Полное обновление урока. Доступно Автору урока из группы moder.",
        tags=["Уроки"],
    )
    def put(self, request, *args, **kwargs):
        return super().put(request, *args, **kwargs)


class NetworkModelDestroyAPIView(DestroyAPIView):
    queryset = NetworkModel.objects.all()
    serializer_class = NetworkModelSerializer
    permission_classes = (
        IsAuthenticated,
        IsOwner | ~IsModer,
    )

    @swagger_auto_schema(
        operation_summary="Удаление урока",
        operation_description="Удаление урока. Доступно только Автору урока (не из группы moder).",
        tags=["Уроки"],
        responses={204: "No Content", 403: "Forbidden (если пользователь — moder)"},
    )
    def delete(self, request, *args, **kwargs):
        return super().delete(request, *args, **kwargs)
