from django.core.management.base import BaseCommand
from django.utils import timezone
from insightly.models import Project, Projectctcstcdmtupdate, Projectctcstcproject, Projectirsnotice, Projectsalestaxreturn, Project1099misc

class Command(BaseCommand):
    help = 'Deletes '

    def handle(self, *args, **kwargs):

        Projectctcstcproject.objects.all().delete()

        self.stdout.write("All projects deleted")
