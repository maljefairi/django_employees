import re
import json
from pathlib import Path
from django.core.management.base import BaseCommand
from jobs.models import Job


RE_DASH_START = re.compile(r'^-')
RE_WITH_NUMS = re.compile(r'\d+\.')
RE_WITH_NUMS2 = re.compile(r'\d+\-')
RE_WITH_NUMS3 = re.compile(r'\d+\)')
RE_WITH_NUMS4 = re.compile(r'\d+\s+\)')
RE_WITH_NUMS5 = re.compile(r'\d+\s+\.\s+')


def clean_text(text: str):
    """
    Clean text by removing numbers and dashes from the start of lines
    """
    lines = []
    for line in text.splitlines():
        line = line.strip()
        if line == '':
            continue
        if RE_WITH_NUMS.search(line):
            line = RE_WITH_NUMS.sub('', line)
            lines.append(line.strip())
        elif RE_DASH_START.search(line):
            line = RE_DASH_START.sub('', line)
            lines.append(line.strip())
        elif RE_WITH_NUMS2.search(line):
            line = RE_WITH_NUMS2.sub('', line)
            lines.append(line.strip())
        elif RE_WITH_NUMS3.search(line):
            line = RE_WITH_NUMS3.sub('', line)
            lines.append(line.strip())
        elif RE_WITH_NUMS4.search(line):
            line = RE_WITH_NUMS4.sub('', line)
            lines.append(line.strip())
        elif RE_WITH_NUMS5.search(line):
            line = RE_WITH_NUMS5.sub('', line)
            lines.append(line.strip())

    if len(lines) < 2:
        return text
    return "\n".join(lines)


class Command(BaseCommand):
    help = 'Load books from a json file'

    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str)

    def handle(self, *args, **options):
        json_file = options['json_file']
        if not Path(json_file).exists():
            self.stdout.write(self.style.ERROR(
                f'File {json_file} does not exist'))
            return

        try:
            with open(json_file, 'r', encoding='utf8') as f:
                data = json.load(f)
        except json.JSONDecodeError:
            self.stdout.write(self.style.ERROR(
                f'File {json_file} is not a valid json file'))
            return

        self.load_data(data)

    def load_data(self, data: list):
        """
        Load data from a json file into the database
        """
        total_added = 0
        total_updated = 0

        for item in data:
            if item["job_title"].strip() == "":
                continue
            requirements = ""
            for r in item["job_requirements"]:
                requirements += f'{r["degree"]} ({r["experience"]})\n'

            instance, created = Job.objects.update_or_create(
                title=item["job_title"],
                description=clean_text(item["description"]),
                defaults={
                    'grade': item["grade"],
                    'code': item["code"],
                    'group_type': item["group_type"],
                    'general_group': item["general_group"],
                    'job_location': item["job_location"],
                    'job_responsibilities': clean_text(item["job_responsibilities"]),
                    'job_objectives': clean_text("\n".join(item["job_objectives"])),
                    'job_requirements': requirements,
                    'generated': clean_text(item["generated"]),
                    'objectives': clean_text(item["objectives"]),
                    'skills': clean_text(item["skills"]),
                    'training': clean_text(item["training"])
                }
            )
            if created:
                total_added += 1
            else:
                total_updated += 1

        total_available = Job.objects.count()
        self.stdout.write(self.style.HTTP_INFO(
            f"{total_added} new job descriptions added."))
        self.stdout.write(self.style.HTTP_INFO(
            f"{total_updated} job descriptions updated."))
        self.stdout.write(self.style.HTTP_INFO(
            f"Total available job descriptions: {total_available}"))
