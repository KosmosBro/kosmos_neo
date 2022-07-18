from django.urls import include, path
from rest_framework import routers
from api import views
from django.urls import path
from rest_framework_simplejwt import views as jwt_views

router = routers.DefaultRouter()
router.register(r'register', views.CreateUserAPIView, basename='MyModel')
router.register(r'product', views.ProductViewSet)
router.register(r'supplier', views.SupplierViewSet)
router.register(r'discount', views.DiscountViewSet)
router.register(r'category', views.CategoryViewSet)
router.register(r'cart', views.CartViewSet)
router.register(r'cart_content', views.CartContentViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/token/', jwt_views.TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', jwt_views.TokenRefreshView.as_view(), name='token_refresh'),
]
