from django.urls import include, path
from rest_framework import routers
from api import api_views

router = routers.DefaultRouter()
router.register(r'register', api_views.CreateUserAPIView, basename='MyModel')
router.register(r'product', api_views.ProductViewSet)
router.register(r'supplier', api_views.SupplierViewSet)
router.register(r'discount', api_views.DiscountViewSet)
router.register(r'category', api_views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
