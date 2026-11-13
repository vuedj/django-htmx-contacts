from typing import ClassVar

from django import forms
from django.core.exceptions import ValidationError

from .models import Contact


class ContactForm(forms.ModelForm):
    name = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "class": "input input-bordered w-full my-2",
                "placeholder": "Name",
            }
        )
    )

    email = forms.EmailField(
        widget=forms.EmailInput(
            attrs={
                "class": "input input-bordered w-full my-2",
                "placeholder": "Email address",
            }
        )
    )

    class Meta:
        model: ClassVar[type[Contact]] = Contact
        fields: ClassVar[list[str]] = ["name", "email"]

    def clean_email(self):
        email = self.cleaned_data["email"]
        if self.Meta.model.objects.filter(
            user=self.initial.get("user"), email=email
        ).exists():
            raise ValidationError("Contact with this email address already exists!")
        return email
