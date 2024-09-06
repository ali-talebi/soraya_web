# Generated by Django 5.1.1 on 2024-09-05 19:45

import ckeditor.fields
import django.db.models.deletion
import django_jalali.db.models
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("account", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Event_Information",
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
                    "picture",
                    models.FileField(upload_to="Events/", verbose_name="تصویر رویداد"),
                ),
                (
                    "event_name",
                    models.CharField(max_length=100, verbose_name="نام رویداد "),
                ),
                (
                    "event_description",
                    models.CharField(
                        max_length=500, verbose_name="توضیح مختصر در خط ۱ "
                    ),
                ),
                (
                    "creator",
                    models.CharField(max_length=200, verbose_name="نام برگزار کننده"),
                ),
                ("address", models.CharField(max_length=100, verbose_name="آدرس")),
                (
                    "date",
                    django_jalali.db.models.jDateTimeField(verbose_name="زمان برگزاری"),
                ),
                ("text", ckeditor.fields.RichTextField(verbose_name="متن رویداد")),
                ("price", models.BigIntegerField(verbose_name="میزان هزینه")),
                (
                    "frame",
                    models.CharField(
                        max_length=1000, verbose_name="لوکیشن از روی نقشه "
                    ),
                ),
                (
                    "guidance_1",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="account.profile",
                        verbose_name="فرد راهنمای شماره 1 ",
                    ),
                ),
                (
                    "guidance_2",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="guidance",
                        to="account.profile",
                        verbose_name="فرد راهنمای شماره 2 ",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "رویداد های مدرسه ",
                "db_table": "events_information",
            },
        ),
        migrations.CreateModel(
            name="Scheduleing",
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
                    "name",
                    models.CharField(
                        max_length=200,
                        verbose_name="نام زمان برگزاری به روز ( مثلا روز 1 ( چهارشنبه 1 بهمن )",
                    ),
                ),
                (
                    "time_start",
                    models.CharField(max_length=10, verbose_name="زمان برگزاری"),
                ),
                (
                    "guess",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="account.profile",
                        verbose_name="فرد مهمان و سخنران",
                    ),
                ),
            ],
        ),
    ]
