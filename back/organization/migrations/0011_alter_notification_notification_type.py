# Generated by Django 3.2.10 on 2022-02-17 22:37

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("organization", "0010_auto_20220216_2310"),
    ]

    operations = [
        migrations.AlterField(
            model_name="notification",
            name="notification_type",
            field=models.CharField(
                choices=[
                    ("added_todo", "A new to do item has been added"),
                    ("completed_todo", "To do item has been marked as completed"),
                    ("added_resource", "A new resource item has been added"),
                    ("completed_course", "Course has been completed"),
                    ("added_badge", "A new badge item has been added"),
                    ("added_introduction", "A new introduction item has been added"),
                    ("added_preboarding", "A new preboarding item has been added"),
                    ("added_new_hire", "A new hire has been added"),
                    ("added_administrator", "A new administrator has been added"),
                    ("added_admin_task", "A new admin task has been added"),
                    ("sent_email_message", "A new email has been sent"),
                    ("sent_text_message", "A new text message has been sent"),
                    ("sent_slack_message", "A new slack message has been sent"),
                    (
                        "failed_no_phone",
                        "Couldn't sent text message: number is missing",
                    ),
                ],
                default="added_todo",
                max_length=100,
            ),
        ),
    ]
