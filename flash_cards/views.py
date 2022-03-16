from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test
from flash_cards.models import FlashCard, Deck
# Create your views here.

def list_decks(request):
    decks = Deck.objects.all()
    sort_by = request.GET.get("sort") or "title"
    return render( 
        request, "flash_cards/list_decks.html", {"decks": decks, "sort_by": sort_by} )
    
    
def list_cards(request, pk):
        cards = FlashCard.objects.all(deck=pk)
        sort_by = request.GET.get("sort") or "title"
        return render(
            request, "flash_cards/list_cards.html", {"cards": cards, "sort_by": sort_by}
        )
        
def index(request):
    
    return render(request, "flash_cards/homepage.html")
    