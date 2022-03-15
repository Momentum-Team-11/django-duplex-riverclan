from django import forms
from .models import FlashCard


class CardForm(forms.ModelForm):

    class Meta:
        model = FlashCard
        fields = [
            'deck',
            'title',
            'description',
            'created_at',
        ]