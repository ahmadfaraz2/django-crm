from typing import Any
from django.core.management.base import BaseCommand

from ...utils import generate_customer

# management > commands > generate_data

class Command(BaseCommand):
    help = "Generate Dummy data for Customer"

    def handle(self, *args, **kwargs):
        generate_customer(10)
        print("Completed")


# Usage

# python manage.py generate_data