from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category13WCF, Project13WCF, Stage13WCF, UserModel13WCF, Pipeline13WCF
from django.db.models import F, Case, Value, When


class Command(BaseCommand):
    help = 'Imports data from insightly'

    def add_arguments(self, parser):
        parser.add_argument(
            '-i', '--initial', action='store_true', help='Initial syncup')
        
    def get_obj(self, model, obj_id):
        if not obj_id:
            return None
        attr_id = f'{model.__name__}_id'.lower()
        try:
            params = {
                attr_id: obj_id,
            }
            obj = model.objects.get(**params)
        except ObjectDoesNotExist:
            obj = model()
            setattr(obj, attr_id, obj_id)
        return obj
        
            
    def sync_pipelines(self, session):
        pipelines = session.get_pipelines()
        for p in pipelines:
            pipeline = self.get_obj(Pipeline13WCF, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage13WCF, s['STAGE_ID'])
           #stage = self.get_obj(Stage13WCF, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                #pipeline = self.get_obj(Pipeline13WCF, s['PIPELINE_ID'])
                #pipeline.save()
                #stage.pipeline = pipeline
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Category13WCF, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel13WCF, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project13WCF, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel13WCF, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category13WCF, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            project.stage = self.get_obj(Stage13WCF, p['STAGE_ID'])        

            if not project.woi and project.stage_id == (3616559):
                project.proformad13WCF0001Days +=1   
            elif not project.woi and project.stage_id == (3616560):
                project.setupof13WCF13WCF0002days +=1 
            elif not project.woi and project.stage_id == (3616561):
                project.ongoing13WCFwork13WCF0003days +=1
            else:  
                print("Project not in filtered stages")

            if project.woi and project.stage_id == (3616559):
                project.proformad13WCF0001P4 +=1   
            elif project.woi and project.stage_id == (3616560):
                project.setupof13WCF13WCF0002P4 +=1    
            elif project.woi and project.stage_id == (3616561)
                project.ongoing13WCFwork13WCF0003P4  +=1
                           
            else: 
                print("Project not in filtered stages") 

            project.TotalP4DaysPerStage = project.proformad13WCF0001P4 + project.setupof13WCF13WCF0002P4 + project.ongoing13WCFwork13WCF0003P4
            project.TotalDaysPerStage = project.proformad13WCF0001Days + project.setupof13WCF13WCF0002days + project.ongoing13WCFwork13WCF0003days 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage
            if p['PROJECT_NAME'].__contains__('13WCF') and p['STATUS'] == 'IN PROGRESS':
                project.save()

   
    def handle(self, *args, **options):
        initial = options['initial']
        with client.Session(settings.INSIGHTLY_API_KEY) as session:
            #self.sync_pipelines(session)
            #self.stdout.write(self.style.SUCCESS('Pipelines synced up...'))            
            self.sync_stages(session)
            self.stdout.write(self.style.SUCCESS('Stages synced up...'))
            self.sync_categories(session)
            self.stdout.write(self.style.SUCCESS('Categories synced up...'))
            self.sync_users(session)
            self.stdout.write(self.style.SUCCESS('Users synced up...'))
            self.sync_projects(session)
            self.stdout.write(self.style.SUCCESS('Projects synced up...'))
        self.stdout.write(self.style.SUCCESS('Done!'))

 