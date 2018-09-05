"""whatsup URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from whatsup import settings
from rest_framework import routers
from groups.views import CategoryViewSet, LinkViewSet, LinkList, CategoryWithoutPagingViewSet

router = routers.DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'links', LinkViewSet)
router.register(r'allcategories', CategoryWithoutPagingViewSet)



urlpatterns = [
    url(r'^', include(router.urls)),
    path('admin/', admin.site.urls),
    path("list/<int:cat_pk>/", LinkList.as_view(), name='items_list')
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
