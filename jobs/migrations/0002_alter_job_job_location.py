# Generated by Django 4.2.4 on 2023-08-12 16:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("jobs", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="job",
            name="job_location",
            field=models.CharField(db_index=True, max_length=512),
        ),
    ]
