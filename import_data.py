import os
import django
import json

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'django_employees.settings')
django.setup()

from jobs.models import JobTitle, JobDescription  # Import the models after Django has been setup

def load_data():
    with open('new_descriptions.json', 'r') as file:
        data = json.load(file)
        
        for item in data:
            # Get or create a JobTitle instance
            job_title_instance, created = JobTitle.objects.get_or_create(title=item["job_title"])
            
            job_requirements_list = []
            for req in item["job_requirements"]:
                if "description" in req:
                    job_requirements_list.append(req["description"])

            job_requirements = ",".join(job_requirements_list)
            job_description = JobDescription(
                job_title=job_title_instance,  # Assign the instance, not a string
                grade=item["grade"],
                code=",".join(item["code"]),
                group_type=item["group_type"],
                general_group=item["general_group"],
                job_location=item["job_location"],
                job_responsibilities=item["job_responsibilities"],
                job_objectives=",".join(item["job_objectives"]),
                job_requirements=job_requirements,
                description=item["description"],
                generated=item["generated"],
                objectives=item["objectives"],
                skills=item["skills"],
                training=item["training"]
            )
            job_description.save()

        print("Data imported successfully!")

if __name__ == "__main__":
    load_data()
