import uuid

from django.conf import settings
from django.db import models


class LinkManager(models.Manager):
    def generate_pk(self):
        return str(uuid.uuid4()).split("-")[-1]

    def create(self, *args, **kwargs):
        if "path" not in kwargs:
            kwargs["path"] = self.generate_pk()
        return super().create(*args, **kwargs)


class Link(models.Model):
    path = models.CharField(max_length=12, primary_key=True)
    original_url = models.URLField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    visits = models.PositiveIntegerField(default=0)
    created_ip = models.CharField(max_length=200, default="Unknown")
    created_location = models.CharField(max_length=200, default="Unknown")

    objects = LinkManager()

    class Meta:
        ordering = ["-created_at"]

    @property
    def redirect_url(self):
        return f"{settings.BASE_URL}/shawty/{self.path}"

    def __str__(self):
        return self.redirect_url
