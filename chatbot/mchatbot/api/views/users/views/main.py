from django.db.models import Q
from rest_framework import (permissions, status)
from rest_framework.viewsets import ModelViewSet
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import action
from rest_framework.filters import OrderingFilter, SearchFilter
from rest_framework.pagination import PageNumberPagination, LimitOffsetPagination
from chat.models.users.main import UserChatModel
from api.views.users.serializers.main import UserChatReadModelSerializer
from api.views.users.serializers.write import UserChatWriteSerializer


class UserChatViewSet(ModelViewSet):
    # permission_classes = [permissions.IsAuthenticated, ]
    permission_classes = [permissions.AllowAny, ]
    model = UserChatModel
    queryset = model.objects.all()
    pagination_class = None
    filter_backends = (SearchFilter, OrderingFilter,)
    filterset_fields = model.MetaDb.fields
    ordering_fields = filterset_fields  # - for highest

    def get_serializer_class(self):
        if self.action in ('list', 'retrieve'):
            return UserChatReadModelSerializer
        return UserChatWriteSerializer

    def retrieve(self, request: Request, pk=None):
        RES = super().retrieve(request, pk)
        _data = RES.data
        DATA = {} if _data is None else _data

        # print({"DATA": DATA})

        return Response({"message": "", "data": DATA}, status=RES.status_code)

    def list(self, request: Request):      
        queryset = self.filter_queryset(self.get_queryset())
        page = self.paginate_queryset(queryset=queryset)

        if page is not None:
            serializer = self.get_serializer(page, many=True)
            DATA = serializer.data
            return self.get_paginated_response(data=DATA)

        serializer = self.get_serializer(queryset, many=True)
        DATA = serializer.data
        return Response({"message": "", "data": DATA}, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        print({"args": args, "kwargs": kwargs})
        return super().create(request, *args, **kwargs)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return super().destroy(request, *args, **kwargs)
