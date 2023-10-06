# Create a new management command, e.g., remove_duplicate_contenttype.py

from django.core.management.base import BaseCommand
from django.contrib.contenttypes.models import ContentType

class Command(BaseCommand):
    help = 'Remove duplicate ContentType records'

    def handle(self, *args, **kwargs):
        try:
            # Look up the duplicate ContentType record
            duplicate_content_type = ContentType.objects.get(app_label='account', model='emailaddress')
            
            # Delete the duplicate record
            duplicate_content_type.delete()
            
            self.stdout.write(self.style.SUCCESS('Duplicate ContentType record removed'))
        except ContentType.DoesNotExist:
            self.stdout.write(self.style.SUCCESS('No duplicate ContentType record found'))

# Save this file in your project's management/commands directory
# Then run the command:
# python manage.py remove_duplicate_contenttype
