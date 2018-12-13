# coding: utf8
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from .mixins import (CreateModelMixin, ListModelMixin, UpdateModelMixin, DestroyModelMixin)
from .schemas import PaginationResponse
from .authentication import CustomTokenAuthentication


class CreateAPIView(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    #authentication_classes = (CustomTokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)


class UpdateAPIView(UpdateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    #authentication_classes = (CustomTokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def put(self, request, *args, **kwargs):
        return self.update(request, *args, **kwargs)


class DestroyAPIView(DestroyModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance.
    """
    #authentication_classes = (CustomTokenAuthentication,)
    #permission_classes = (IsAuthenticated,)
    def delete(self, request, pk,*args, **kwargs):
        return self.destroy(request, pk,*args, **kwargs)


class ListAPIView(ListModelMixin, GenericAPIView):
    """
    Concrete view for listing a queryset.
    """
    #authentication_classes = (CustomTokenAuthentication,)
    #permission_classes = (IsAuthenticated,)

    pagination_class = PaginationResponse

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)


class ListCreateView(CreateAPIView, ListAPIView, UpdateAPIView, DestroyAPIView):
    pass


