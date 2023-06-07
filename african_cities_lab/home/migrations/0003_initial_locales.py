# Generated by Django 4.0.8 on 2023-02-22 14:54

# from django.core.management import call_command
from django.db import migrations


def load_fixture(apps, schema_editor):
    # call_command("loaddata", "initial_locales", app_label="home")
    # create french locale and sync it from english
    Locale = apps.get_model("wagtailcore", "locale")
    en_locale = Locale.objects.first()
    fr_locale = Locale.objects.create(language_code="fr")
    LocaleSynchronization = apps.get_model("wagtail_localize", "localesynchronization")
    LocaleSynchronization.objects.create(locale=fr_locale, sync_from=en_locale)


def unload_fixture(apps, schema_editor):
    Locale = apps.get_model("wagtailcore", "locale")
    en_locale = Locale.objects.first()
    fr_locale = Locale.objects.get(language_code="fr").delete()
    LocaleSynchronization = apps.get_model("wagtail_localize", "localesynchronization")
    LocaleSynchronization.objects.get(locale=fr_locale, sync_from=en_locale).delete()


class Migration(migrations.Migration):
    dependencies = [
        ("home", "0002_homepage_body"),
        ("wagtail_localize", "0012_localesynchronization"),
    ]

    operations = [
        migrations.RunPython(load_fixture, reverse_code=unload_fixture),
    ]
