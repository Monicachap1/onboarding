# Generated by Django 3.2.10 on 2022-01-13 21:46

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ("sequences", "0012_auto_20220111_1917"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="sequence",
            name="appointments",
        ),
        migrations.RemoveField(
            model_name="sequence",
            name="preboarding",
        ),
        migrations.RemoveField(
            model_name="sequence",
            name="resources",
        ),
        migrations.RemoveField(
            model_name="sequence",
            name="to_do",
        ),
    ]
