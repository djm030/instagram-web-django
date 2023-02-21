# Generated by Django 4.1.7 on 2023-02-21 05:48

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Feed",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created", models.DateTimeField(auto_now_add=True)),
                ("updated", models.DateTimeField(auto_now=True)),
                ("caption", models.TextField(default="")),
                ("contenImg", models.URLField(blank=True)),
                ("likesNum", models.PositiveIntegerField(default=0)),
                ("reviewsNum", models.PositiveIntegerField(default=0)),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
