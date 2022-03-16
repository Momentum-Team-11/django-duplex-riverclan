from django import forms
from .models import Deck, FlashCard


class CardForm(forms.ModelForm):

    class Meta:
        model = FlashCard
        fields = [
            'deck',
            'title',
            'description',
        ]

class DeckForm(forms.ModelForm):

    class Meta:
        model = Deck
        fields = [
            'title'
        ]