# Generated by Django 4.0.3 on 2022-03-14 16:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('flash_cards', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flashcard',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='deck',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AlterField(
            model_name='flashcard',
            name='deck',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='flashcards', to='flash_cards.deck'),
        ),
    ]
