import uuid

from django import forms

from links.models import Link


class LinkForm(forms.ModelForm):
    original_url = forms.CharField(
        label="",
        widget=forms.TextInput(
            attrs={
                "placeholder": "http://placeholder.com/",
                "class": "form-control",
            }
        ),
    )

    class Meta:
        model = Link
        fields = ["original_url"]

    def save(self, commit=True):
        link = super().save(commit=False)
        link.path = str(uuid.uuid4()).split("-")[-1]
        link.save()
        return link
