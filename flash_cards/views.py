from django.shortcuts import render,  redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test 
from .models import FlashCard, Deck
from .forms import CardForm, DeckForm
# Create your views here.

def index(request):
    
    return render(request, "flash_cards/homepage.html")
    
def add_card(request):
    if request.method =='GET':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_decks')
    return render(request, "flash_cards/add_card.html", {"form": form})

def edit_card(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    card = get_object_or_404(FlashCard, pk=pk)
    if request.method == 'GET':
        form = CardForm(instance=card)
    else:
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect(to='list_decks')
    return render(request, "flash_cards/edit_card.html", {"form": form, "card": card})

def delete_card(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    card = get_object_or_404(FlashCard, pk=pk)
    if request.method == 'POST':
        card.delete()
        return redirect(to='list_decks')

    return render(request, "flash_cards/delete_card.html", {"card": card})

# deck below

def add_deck (request):
    if request.method =='GET':
        form = DeckForm()
    else:
        form = DeckForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_decks')
    return render(request, "flash_cards/add_deck.html", {"form": form})

def edit_deck (request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == 'GET':
        form = DeckForm(instance=deck)
    else:
        form = DeckForm(data=request.POST, instance=deck)
        if form.is_valid():
            form.save()
            return redirect(to='list_decks')
    return render(request, "flash_cards/edit_deck.html", {"form": form, "deck": deck})

def delete_deck (request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == 'POST':
        deck.delete()
        return redirect(to='list_decks')

    return render(request, "flash_cards/delete_card.html", {"deck": deck})
