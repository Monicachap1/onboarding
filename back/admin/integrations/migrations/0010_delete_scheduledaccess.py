# Generated by Django 3.2.10 on 2022-02-09 21:38

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0009_remove_accesstoken_name"),
    ]

    operations = [
        migrations.DeleteModel(
            name="ScheduledAccess",
        ),
    ]
