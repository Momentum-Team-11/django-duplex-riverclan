# Generated by Django 4.0.3 on 2022-03-16 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flash_cards', '0005_alter_flashcard_correct'),
    ]

    operations = [
        migrations.AlterField(
            model_name='deck',
            name='slug',
            field=models.SlugField(blank=True, max_length=75, null=True, unique=True),
        ),
    ]
