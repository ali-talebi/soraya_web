# Generated by Django 5.1.1 on 2024-09-05 21:50

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("account", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterField(
            model_name="profile",
            name="person",
            field=models.OneToOneField(
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                related_name="person",
                to=settings.AUTH_USER_MODEL,
                verbose_name="فرد مورد نظر",
            ),
        ),
    ]
