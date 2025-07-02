from django.urls import path, include
from rest_framework import routers
from rest_framework.permissions import AllowAny
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

# from users.apps import UsersConfig
from counterparties.views import CounterpartiesViewsSet



router = routers.SimpleRouter(
    trailing_slash=False,
)
router.register(prefix=r"partner", viewset=CounterpartiesViewsSet, basename="partner")




app_name = "partner"

urlpatterns = [
    # habit_tracker
    path("", include(router.urls)),
    #path("partner/", CounterpartiesViewsSet.as_view(), name="partner"),
]