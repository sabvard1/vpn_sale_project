# Generated by Django 5.0 on 2024-01-08 09:43

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="profileModel",
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
                ("Name", models.CharField(max_length=100)),
                ("Family", models.CharField(max_length=100)),
                (
                    "ProfileImage",
                    models.ImageField(blank=True, upload_to="profileImages/"),
                ),
                ("Email", models.EmailField(max_length=254)),
                (
                    "Gender",
                    models.IntegerField(
                        choices=[(1, "Man"), (2, "Woman"), (3, "Other")], null=True
                    ),
                ),
                (
                    "user",
                    models.OneToOneField(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]