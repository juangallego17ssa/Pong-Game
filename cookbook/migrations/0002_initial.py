# Generated by Django 4.1.7 on 2023-03-16 09:04

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("recipe", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ("cookbook", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="cookbook",
            name="created_by_user",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                related_name="added_cookbooks",
                to=settings.AUTH_USER_MODEL,
            ),
        ),
        migrations.AddField(
            model_name="cookbook",
            name="favourite_by_user",
            field=models.ManyToManyField(
                blank=True, related_name="fav_cookbooks", to=settings.AUTH_USER_MODEL
            ),
        ),
        migrations.AddField(
            model_name="cookbook",
            name="recipes",
            field=models.ManyToManyField(
                related_name="in_cookbooks", to="recipe.recipe"
            ),
        ),
    ]
