from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test

from flash_cards.models import FlashCard 
# Create your views here.

def list_cards(request, pk):
    
    cards = FlashCard.objects.all(deck=pk)
    sort_by = request.GET.get("sort")
    return render( 
        request, "FlashCard/list_cards.html", {"cards": cards, "sort_by": sort_by} )
    
    
    #def add_card(request, pk):
        
def index(request):
    
    return render(request, "flash_cards/homepage.html")
    