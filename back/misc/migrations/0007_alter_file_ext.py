# Generated by Django 3.2.13 on 2022-05-20 01:29

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("misc", "0006_content"),
    ]

    operations = [
        migrations.AlterField(
            model_name="file",
            name="ext",
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
