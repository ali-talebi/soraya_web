# Generated by Django 5.1.1 on 2024-09-05 19:45

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Country",
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
                (
                    "country_name",
                    models.CharField(max_length=50, verbose_name="نام کشور"),
                ),
            ],
            options={
                "verbose_name_plural": "نام کشور های موجود",
                "db_table": "Country",
            },
        ),
        migrations.CreateModel(
            name="City",
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
                ("name_city", models.CharField(max_length=100, verbose_name="نام شهر")),
                (
                    "main_country",
                    models.OneToOneField(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="main_country",
                        to="country_city.country",
                        verbose_name="نام کشور ",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "نام شهر هاي موجود",
                "db_table": "City",
            },
        ),
    ]
