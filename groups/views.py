from rest_framework import viewsets
from .models import Category, Link
from .serializers import CategorySerializer, LinkSerializer
from rest_framework import generics
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
# Create your views here.


class CategoryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


class LinkViewSet(viewsets.ModelViewSet):
    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            self.perform_create(serializer)
            return Response({
                'status': 'ok',
                'msg': 'The link has been added and will show after admin accepting'
            })
        else:
            return Response({
                'status': 'fail',
                'msg': 'The link has not been added!'
            })

    queryset = Link.objects.filter(active=True).order_by('-modified')
    serializer_class = LinkSerializer


class LinkList(generics.ListAPIView):
    def get_queryset(self):
        category = get_object_or_404(Category, pk=self.kwargs['cat_pk'])
        query_set = Link.objects.filter(category=category, active=True).order_by('-modified')
        return query_set

    serializer_class = LinkSerializer
