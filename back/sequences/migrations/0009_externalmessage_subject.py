# Generated by Django 3.1.7 on 2021-03-17 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('sequences', '0008_sequence_auto_add'),
    ]

    operations = [
        migrations.AddField(
            model_name='externalmessage',
            name='subject',
            field=models.CharField(blank=True, max_length=78),
        ),
    ]
