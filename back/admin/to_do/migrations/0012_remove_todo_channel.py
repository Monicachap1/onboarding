# Generated by Django 3.2.10 on 2022-01-31 17:17

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("to_do", "0011_todo_slack_default_channel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="todo",
            name="channel",
        ),
    ]
