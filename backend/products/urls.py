from django.urls import path, include
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from products.views import ProductsViewsSet


router = routers.SimpleRouter(
    trailing_slash=False,
)
router.register(prefix=r"products", viewset=ProductsViewsSet, basename="products")

app_name = "products"

urlpatterns = [
    # habit_tracker
    path("", include(router.urls)),
]