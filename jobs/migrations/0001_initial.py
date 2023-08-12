# Generated by Django 4.2.4 on 2023-08-12 17:19

from django.db import migrations, models
import django.utils.timezone
import uuid


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Job",
            fields=[
                (
                    "id",
                    models.UUIDField(
                        default=uuid.uuid4,
                        editable=False,
                        primary_key=True,
                        serialize=False,
                    ),
                ),
                ("title", models.CharField(db_index=True, max_length=255)),
                ("grade", models.CharField(db_index=True, max_length=512)),
                ("code", models.JSONField(blank=True, db_index=True, default=list)),
                ("group_type", models.CharField(db_index=True, max_length=255)),
                ("general_group", models.CharField(db_index=True, max_length=255)),
                ("job_location", models.CharField(db_index=True, max_length=512)),
                ("job_responsibilities", models.TextField(db_index=True)),
                ("job_objectives", models.TextField(db_index=True)),
                ("description", models.TextField(db_index=True)),
                ("generated", models.TextField(db_index=True)),
                ("objectives", models.TextField(db_index=True)),
                ("skills", models.TextField(db_index=True)),
                ("training", models.TextField(db_index=True)),
                ("job_requirements", models.TextField(db_index=True)),
                (
                    "created_at",
                    models.DateTimeField(
                        db_index=True, default=django.utils.timezone.now
                    ),
                ),
            ],
            options={
                "verbose_name": "Job",
                "verbose_name_plural": "Jobs",
                "db_table": "jobs",
                "ordering": ["title"],
                "indexes": [
                    models.Index(
                        fields=[
                            "title",
                            "grade",
                            "group_type",
                            "general_group",
                            "job_location",
                            "job_responsibilities",
                            "job_objectives",
                            "job_requirements",
                            "description",
                            "generated",
                            "objectives",
                            "skills",
                            "training",
                        ],
                        name="jobs_title_062b45_idx",
                    )
                ],
            },
        ),
    ]
