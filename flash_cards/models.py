from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils import timezone
# from django.utils.text import slugify

# Create your models here.
class FlashCard(models.Model):
    title = models.CharField(max_length=50)
    description = models.TextField(max_length=1000, null=True, blank=True)
    deck = models.ForeignKey('deck', related_name="flashcards", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.title


class Deck(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f"<Deck name={self.name}>"
