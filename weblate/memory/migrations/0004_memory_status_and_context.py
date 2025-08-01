# Copyright © Michal Čihař <michal@weblate.org>
#
# SPDX-License-Identifier: GPL-3.0-or-later

# Generated by Django 5.2.1 on 2025-06-26 16:28

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("memory", "0003_drop_hash_index"),
    ]

    operations = [
        migrations.AddField(
            model_name="memory",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Pending"), (1, "Active")], default=1
            ),
        ),
        migrations.AddField(
            model_name="memory",
            name="context",
            field=models.TextField(blank=True, default=""),
        ),
        migrations.AlterField(
            model_name="memory",
            name="status",
            field=models.IntegerField(
                choices=[(0, "Pending"), (1, "Active")], default=0
            ),
        ),
    ]
