from django.shortcuts import render
from django.contrib.auth.decorators import login_required, user_passes_test 
# Create your views here.

def index(request):
    
    return render(request, "flash_cards/homepage.html")