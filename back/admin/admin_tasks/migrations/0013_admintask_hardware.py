# Generated by Django 4.2.6 on 2023-11-02 02:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("hardware", "0002_hardware_assigned_to_hardware_person_type"),
        ("admin_tasks", "0012_admintask_create_integration_admintask_integration"),
    ]

    operations = [
        migrations.AddField(
            model_name="admintask",
            name="hardware",
            field=models.ForeignKey(
                help_text="Only set if generated based on hardware.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="hardware.hardware",
            ),
        ),
    ]
