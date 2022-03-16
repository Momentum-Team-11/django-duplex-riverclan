from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required, user_passes_test
from .models import FlashCard, Deck
import random
# Create your views here.

def index(request):
    return render(request, "flash_cards/homepage.html")


def quiz(request, slug, pk):
    deck = get_object_or_404(Deck, slug=slug)
    incomplete = FlashCard.objects.filter(deck_id=deck.id)
    incomplete = FlashCard.objects.filter(correct=False)
    if incomplete:
        random_card = list(incomplete)
        flashcard = random.choice(random_card)
        return render(request, "flash_cards/quiz.html", {"deck": deck, "flashcard": flashcard})
    else:
        return redirect(to="results", slug=slug)


def answer(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    return render(request, "flash_cards/answer.html", {"flashcard": flashcard, "deck": deck})


def correct(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == "GET":
        correct = FlashCard
    else:
        correct = FlashCard(request.method == "POST")
        FlashCard.objects.filter(pk=pk).update(correct=True),
        return redirect(to="quiz", slug=deck.slug, pk=pk)

    return render(request, "flash_cards/correct.html", {"deck": deck, "flashcard": flashcard, "correct": correct},)


def incorrect(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == "GET":
        incorrect = FlashCard
    else:
        incorrect = FlashCard(request.method == "POST")
        FlashCard.objects.filter(pk=pk).update(correct=False),
        return redirect(to="quiz", slug=deck.slug, pk=pk)

    return render(request, "correct.html", {"deck": deck, "flashcard": flashcard, "incorrect": incorrect},)


def results(request, slug):
    deck = get_object_or_404(Deck, slug=slug)
    flashcard = FlashCard.objects.all().filter(deck_id=deck.id)
    flashcard = FlashCard.objects.all().filter(correct=False)
    random_card = list(FlashCard.objects.filter(deck_id=deck.id))
    random_card = random.choice(random_card)
    return render(request, "flash_cards/results.html", {"deck":deck, "flashcard":flashcard, "random_card":random_card})


def start_over(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == "GET":
        clear = FlashCard
    else:
        clear = FlashCard(request.method == "POST")
        FlashCard.objects.filter(deck_id=deck.id).update(correct=False),
        return redirect(to="quiz", slug=deck.slug, pk=pk)

    return render(request, "start_over.html", {"deck": deck, "flashcard": flashcard, "clear": clear},)

def clear(request, slug, pk):
    flashcard = get_object_or_404(FlashCard, pk=pk)
    deck = get_object_or_404(Deck, slug=slug)
    if request.method == "GET":
        clear = FlashCard
    else:
        clear = FlashCard(request.method == "POST")
        FlashCard.objects.filter(deck_id=deck.id).update(correct=False),
        return render(request, "flash_cards/homepage.html")

    return render(request, "clear.html", {"deck": deck, "flashcard": flashcard, "clear": clear},)