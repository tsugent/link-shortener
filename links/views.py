from django.shortcuts import render, redirect
from django.views.generic.base import TemplateView

from links.models import Link
from links.forms import LinkForm


class CreateLink(TemplateView):
    template_name = "create_link.html"
    form = LinkForm

    def get(self, request, *args, **kwargs):
        link_form = self.form()
        return render(
            request,
            self.template_name,
            {"link_form": link_form},
        )

    def post(self, request, *args, **kwargs):
        link_form = self.form(request.POST)
        if link_form.is_valid():
            link = link_form.save()
            return redirect("link_success", path=link.path)
        return render(
            request,
            self.template_name,
            {"form": "link_form"},
        )


class LinkSuccess(TemplateView):
    template_name = "link_success.html"

    def get(self, request, *args, **kwargs):
        link = Link.objects.get(path=kwargs["path"])

        return render(
            request,
            self.template_name,
            {"link": link},
        )
