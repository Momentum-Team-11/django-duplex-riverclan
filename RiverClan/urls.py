"""RiverClan URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from flash_cards import views
from RiverClan import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/', include('registration.backends.simple.urls')),
    path('', views.index, name="home"),
    path('flash_cards/', views.list_decks, name="list_decks"),
    path('flash_cards/add_deck', views.add_deck, name='add_deck'),
    path('flash_cards/<slug:slug>/edit/', views.edit_deck, name='edit_deck'),
    path('flash_cards/<slug:slug>/delete/', views.delete_deck, name='delete_deck'),
    path('flash_cards/<int:pk>/cards/', views.list_cards, name="list_cards"),
    path('flash_cards/add_card', views.add_card, name='add_card'),
    path('flash_cards/<slug:slug>/<int:pk>/edit/', views.edit_card, name='edit_card'),
    path('flash_cards/<slug:slug>/<int:pk>/delete/', views.delete_card, name='delete_card'),
    path('flash_cards/<slug:slug>/<int:pk>/quiz', views.quiz, name="quiz"),
    path('flash_cards/<slug:slug>/<int:pk>/answer', views.answer, name="answer"),  
    path('flash_cards/<slug:slug>/results', views.results, name="results"),  
    path('flash_cards/<slug:slug>/<int:pk>/answer/correct', views.correct, name="correct"),
    path('flash_cards/<slug:slug>/<int:pk>/answer/incorrect', views.incorrect, name="incorrect"),
    path('flash_cards/<slug:slug>/<int:pk>/start-over', views.start_over, name="start_over"),
    path('flash_cards/<slug:slug>/<int:pk>/clear', views.clear, name="clear"),
]
