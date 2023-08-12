from jobs.models import Job
import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_employees.settings')
django.setup()


def load_data():
    with open('new_descriptions.json', 'r') as file:
        data = json.load(file)

        total_added = 0
        total_updated = 0

        for item in data:

            job_description_instance, created = Job.objects.get_or_create(
                title=item["job_title"],
                description=item["description"],
                defaults={
                    'grade': item["grade"],
                    'code': ",".join(item["code"]),
                    'group_type': item["group_type"],
                    'general_group': item["general_group"],
                    'job_location': item["job_location"],
                    'job_responsibilities': item["job_responsibilities"],
                    'job_objectives': "\n".join(item["job_objectives"]),
                    'job_requirements': item["job_requirements"],
                    'generated': item["generated"],
                    'objectives': item["objectives"],
                    'skills': item["skills"],
                    'training': item["training"]
                }
            )

            if created:
                total_added += 1
            else:
                # Update the existing instance with any missing or new data
                # Add fields to be updated as required
                updated = False
                for key, value in item.items():
                    if not getattr(job_description_instance, key, None):
                        setattr(job_description_instance, key, value)
                        updated = True
                if updated:
                    total_updated += 1
                    job_description_instance.save()

        total_available = Job.objects.count()
        print(f"{total_added} new job descriptions added.")
        print(f"{total_updated} job descriptions updated.")
        print(f"Total available job descriptions: {total_available}")


if __name__ == "__main__":
    load_data()
