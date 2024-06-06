from django.urls import path
from api.views import LinkRedirect

urlpatterns = [
    path("<str:uuid>", LinkRedirect.as_view(), name="link-redirect"),
]
