# Generated by Django 4.2.11 on 2024-03-20 01:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('integrations', '0036_remove_manifest_revoke_manifestrevoke_manifest'),
    ]

    operations = [
        migrations.AddField(
            model_name='manifest',
            name='schedule',
            field=models.CharField(default=''),
        ),
    ]
