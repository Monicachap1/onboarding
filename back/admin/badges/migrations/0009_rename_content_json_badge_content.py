# Generated by Django 3.2.10 on 2022-02-01 17:04

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("badges", "0008_alter_badge_content_json"),
    ]

    operations = [
        migrations.RenameField(
            model_name="badge",
            old_name="content_json",
            new_name="content",
        ),
    ]
