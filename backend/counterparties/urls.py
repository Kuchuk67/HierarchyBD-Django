from django.urls import path, include
from rest_framework import routers
from counterparties.views import CounterpartiesViewsSet

router = routers.SimpleRouter(
    trailing_slash=False,
)
router.register(prefix=r"partner", 
                viewset=CounterpartiesViewsSet, 
                basename="partner"
                )

app_name = "partner"

urlpatterns = [path("", include(router.urls))]
