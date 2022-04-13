from django.core.management.base import BaseCommand
from django.utils import timezone
from insightly.models import Project, Projectctcstcdmtupdate, Projectctcstcproject, Projectirsnotice, Projectsalestaxreturn, Project1099misc

class Command(BaseCommand):
    help = 'Deletes '

    def handle(self, *args, **kwargs):
        
        Project.objects.all().delete()
        Projectctcstcdmtupdate.objects.all().delete()
        Projectctcstcproject.objects.all().delete()
        Projectirsnotice.objects.all().delete()
        Projectsalestaxreturn.objects.all().delete()
        Project1099misc.objects.all().delete()
        
        

        self.stdout.write("All projects deleted")
