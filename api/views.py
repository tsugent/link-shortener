from django.shortcuts import get_object_or_404, redirect
from django.views.generic.base import View

from links.models import Link


class LinkRedirect(View):
    def get(self, *args, **kwargs):
        uuid = kwargs["uuid"]
        link = get_object_or_404(Link, path=uuid)
        link.visits += 1
        link.save()
        return redirect(link.original_url)
