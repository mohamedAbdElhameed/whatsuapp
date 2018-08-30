from rest_framework import viewsets
from .models import Category, Link
from .serializers import CategorySerializer, LinkSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
# Create your views here.


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LinkViewSet(viewsets.ModelViewSet):
    queryset = Link.objects.all()
    serializer_class = LinkSerializer


class LinkList(generics.ListAPIView):
    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['cat_pk'])
        query_set = Link.objects.filter(category=category)
        return query_set

    serializer_class = LinkSerializer
