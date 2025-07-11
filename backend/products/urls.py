from django.urls import include, path
from rest_framework import routers
from products.views import ProductsViewsSet

router = routers.SimpleRouter(
    trailing_slash=False,
)
router.register(prefix=r"products", viewset=ProductsViewsSet, basename="products")

app_name = "products"

urlpatterns = [
    path("", include(router.urls)),
]
