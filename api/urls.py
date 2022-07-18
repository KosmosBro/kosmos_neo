from django.urls import include, path
from rest_framework import routers
from api import views

router = routers.DefaultRouter()
router.register(r'register', views.CreateUserAPIView, basename='MyModel')
router.register(r'product', views.ProductViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'discount', views.DiscountViewSet)
router.register(r'category', views.CategoryViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))
]
