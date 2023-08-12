import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_employees.settings')
django.setup()

from jobs.models import JobTitle, JobDescription  # Import the models after Django has been setup

def load_data():
    with open('new_descriptions.json', 'r') as file:
        data = json.load(file)
        
        total_added = 0
        total_updated = 0
        
        for item in data:
            # Get or create a JobTitle instance
            job_title_instance, title_created = JobTitle.objects.get_or_create(title=item["job_title"])
            
            job_requirements_list = []
            for req in item["job_requirements"]:
                if "description" in req:
                    job_requirements_list.append(req["description"])

            job_requirements = ",".join(job_requirements_list)

            # Attempt to retrieve an existing job description based on job title and some other unique identifier (I'm using 'description' as an example)
            job_description_instance, created = JobDescription.objects.get_or_create(
                job_title=job_title_instance,
                description=item["description"],
                defaults={
                    'grade': item["grade"],
                    'code': ",".join(item["code"]),
                    'group_type': item["group_type"],
                    'general_group': item["general_group"],
                    'job_location': item["job_location"],
                    'job_responsibilities': item["job_responsibilities"],
                    'job_objectives': ",".join(item["job_objectives"]),
                    'job_requirements': job_requirements,
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
        
        total_available = JobDescription.objects.count()
        print(f"{total_added} new job descriptions added.")
        print(f"{total_updated} job descriptions updated.")
        print(f"Total available job descriptions: {total_available}")

if __name__ == "__main__":
    load_data()
