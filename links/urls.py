from django.urls import path
from links.views import CreateLink, LinkSuccess

urlpatterns = [
    path("", CreateLink.as_view(), name="link-create"),
    path(
        "success/<str:path>",
        LinkSuccess.as_view(),
        name="link_success",
    ),
]
