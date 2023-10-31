# Generated by Django 4.2.6 on 2023-10-31 22:50

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("integrations", "0022_alter_integration_manifest_and_more"),
        ("admin_tasks", "0011_admintask_based_on"),
    ]

    operations = [
        migrations.AddField(
            model_name="admintask",
            name="create_integration",
            field=models.BooleanField(
                default=False,
                help_text=(
                    "Specifies if integration has been created or removed by "
                    "completing the admin task."
                ),
            ),
        ),
        migrations.AddField(
            model_name="admintask",
            name="integration",
            field=models.ForeignKey(
                help_text="Only set if generated based on a manual integration.",
                null=True,
                on_delete=django.db.models.deletion.SET_NULL,
                to="integrations.integration",
            ),
        ),
    ]
