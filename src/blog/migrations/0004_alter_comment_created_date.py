# Generated by Django 5.0.4 on 2024-04-06 20:05

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blog", "0003_alter_comment_created_date_alter_post_created_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="created_date",
            field=models.DateTimeField(
                default=datetime.datetime(
                    2024, 4, 6, 20, 5, 45, 863483, tzinfo=datetime.timezone.utc
                )
            ),
        ),
    ]
