from django import forms
from models import *


class GeeksForm(forms.ModelForm):
    class Meta:
        model = General_provisions

        fields = [
            "title",
            "intro",
            "fount",
            "addition",
        ]


class Smth(forms.ModelForm):
    class Meta:
        model = General_provisions

        fields = [
            "add_items",
            "concl"
        ]
