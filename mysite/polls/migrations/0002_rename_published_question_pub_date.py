# Generated by Django 4.0.1 on 2022-01-15 20:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("polls", "0001_initial"),
    ]

    operations = [
        migrations.RenameField(
            model_name="question",
            old_name="published",
            new_name="pub_date",
        ),
    ]