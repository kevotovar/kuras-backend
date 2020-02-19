from rest_framework.routers import DefaultRouter, SimpleRouter
from django.conf import settings
from django.conf.urls import url, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.views import refresh_jwt_token, verify_jwt_token
from kuras.users.api.views import UserViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

schema_view = get_schema_view(
    openapi.Info(
        title="Kuras API",
        default_version="v1",
        description="Test description",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,),
)

router.register("users", UserViewSet)

app_name = "api"
urlpatterns = router.urls
urlpatterns += [
    url(r"^rest-auth/", include("rest_auth.urls")),
    url(r"^swagger(?P<format>\.json|\.yaml)$", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    url(r"^swagger/$", schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    url(r"^redoc/$", schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    url(r"^api-token-refresh/", refresh_jwt_token, name="refresh-token"),
    url(r"^api-token-verify/", verify_jwt_token, name="verify_jwt_token"),
]
