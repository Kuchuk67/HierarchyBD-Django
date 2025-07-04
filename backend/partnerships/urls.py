from django.urls import path, include
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from partnerships.views import PartnershipsViewsSet


router = routers.SimpleRouter(
    trailing_slash=False,
)
router.register(prefix=r"orders", viewset=PartnershipsViewsSet, basename="orders")

app_name = "orders"

urlpatterns = [
    path("", include(router.urls)),
]