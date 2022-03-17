from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import FlashCard, Deck
from .forms import CardForm, DeckForm
import random
# Create your views here.

def home_page(request):
    if request.user.is_authenticated:
        return redirect("list_decks")
    else:
        return render(request, "flash_cards/homepage.html")


@login_required
def list_decks(request):
    decks = Deck.objects.all()
    sort_by = request.GET.get("sort") or "title"
    return render( 
        request, "flash_cards/list_decks.html", {"decks": decks, "sort_by": sort_by} )


@login_required
def list_cards(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    flashcards = FlashCard.objects.all().filter(deck_id=deck.id)
    sort_by = request.GET.get("sort") or "title"
    return render(
        request, "flash_cards/list_cards.html", {"deck":deck, "flashcards": flashcards, "sort_by": sort_by}
    )


@login_required
def quiz(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    incomplete = FlashCard.objects.filter(deck_id=deck.id).filter(correct=False)
    if incomplete:
        random_card = list(incomplete)
        flashcard = random.choice(random_card)
        return render(request, "flash_cards/quiz.html", {"deck": deck, "flashcard": flashcard})
    else:
        return redirect(to="results", slug=slug)


@login_required
def answer(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    return render(request, "flash_cards/answer.html", {"flashcard": flashcard, "deck": deck})


@login_required
def correct(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == "GET":
        correct = FlashCard
    else:
        correct = FlashCard(request.method == "POST")
        FlashCard.objects.filter(pk=pk).update(correct=True),
        return redirect(to="quiz", slug=deck.slug)

    return render(request, "flash_cards/correct.html", {"deck": deck, "flashcard": flashcard, "correct": correct},)


@login_required
def incorrect(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == "GET":
        incorrect = FlashCard
    else:
        incorrect = FlashCard(request.method == "POST")
        FlashCard.objects.filter(pk=pk).update(correct=False),
        return redirect(to="quiz", slug=deck.slug)

    return render(request, "correct.html", {"deck": deck, "flashcard": flashcard, "incorrect": incorrect},)


@login_required
def results(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    flashcard = FlashCard.objects.filter(deck_id=deck.id).filter(correct=False)
    random_card = list(FlashCard.objects.filter(deck_id=deck.id))
    random_card = random.choice(random_card)
    return render(request, "flash_cards/results.html", {"deck":deck, "flashcard":flashcard, "random_card":random_card})


@login_required
def start_over(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == "GET":
        clear = FlashCard
    else:
        clear = FlashCard(request.method == "POST")
        FlashCard.objects.filter(deck_id=deck.id).update(correct=False),
        return redirect(to="quiz", slug=deck.slug)

    return render(request, "start_over.html", {"deck": deck, "flashcard": flashcard, "clear": clear},)


@login_required
def clear(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == "GET":
        clear = FlashCard
    else:
        clear = FlashCard(request.method == "POST")
        FlashCard.objects.filter(deck_id=deck.id).update(correct=False),
        return redirect(to="list_decks")

    return render(request, "clear.html", {"deck": deck, "flashcard": flashcard, "clear": clear},)


@login_required
def add_card(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    if request.method =='GET':
        form = CardForm()
    else:
        form = CardForm(data=request.POST)
        if form.is_valid():
            flashcard = form.save(commit=False)
            flashcard.deck_id = deck.id
            flashcard.save()
            return redirect(to='list_cards', slug=deck.slug)
    return render(request, "flash_cards/add_card.html", {"form": form, "deck":deck})


@login_required
def edit_card(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    card = get_object_or_404(FlashCard, pk=pk)
    if request.method == 'GET':
        form = CardForm(instance=card)
    else:
        form = CardForm(data=request.POST, instance=card)
        if form.is_valid():
            form.save()
            return redirect(to='list_cards', slug=deck.slug)
    return render(request, "flash_cards/edit_card.html", {"form": form, "deck":deck, "card": card})


@login_required
def delete_card(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    card = get_object_or_404(FlashCard, pk=pk)
    if request.method == 'POST':
        card.delete()
        return redirect(to='list_cards', slug=deck.slug)

    return render(request, "flash_cards/delete_card.html", {"deck":deck, "card": card})

# deck below


@login_required
def add_deck (request):
    if request.method =='GET':
        form = DeckForm()
    else:
        form = DeckForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect(to='list_decks')
    return render(request, "flash_cards/add_deck.html", {"form": form})


@login_required
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


@login_required
def delete_deck (request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == 'POST':
        deck.delete()
        return redirect(to='list_decks')

    return render(request, "flash_cards/delete_deck.html", {"deck": deck})
