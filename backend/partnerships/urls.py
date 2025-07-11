from django.urls import include, path
from rest_framework import routers
from partnerships.views import PartnershipsViewsSet

router = routers.SimpleRouter(
    trailing_slash=False,
)
router.register(prefix=r"orders", viewset=PartnershipsViewsSet, basename="orders")

app_name = "orders"

urlpatterns = [
    path("", include(router.urls)),
]
