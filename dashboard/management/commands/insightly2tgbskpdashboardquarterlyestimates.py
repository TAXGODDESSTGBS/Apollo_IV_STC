from datetime import datetime
from datetime import timezone
#import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Categoryquarterlyestimates, Projectquarterlyestimates, Stagequarterlyestimates, UserModelquarterlyestimates, Pipelinequarterlyestimates
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
            pipeline = self.get_obj(Pipelinequarterlyestimates, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stagequarterlyestimates, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Categoryquarterlyestimates, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModelquarterlyestimates, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Projectquarterlyestimates, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModelquarterlyestimates, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Categoryquarterlyestimates, p['CATEGORY_ID'])
             
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            project.stage = self.get_obj(Stagequarterlyestimates, p['STAGE_ID'])
            
            if project.woi and project.stage_id == (3466358):
                project.ProformadQtrlyEst0001Days +=1   
            elif project.woi and project.stage_id == (3466359):
                project.ClientInterviewQtrlyEst0002days +=1 
            elif project.woi and project.stage_id == (3466360):
                project.InputPrepQtrlyEst0003days +=1
            elif project.woi and project.stage_id == (3466361):
                project.ReviewQtrlyEst0004days +=1
            elif project.woi and project.stage_id == (3466362):
                project.ClearReviewPointsQtrlyEst0005days +=1              
            elif project.woi and project.stage_id == (3466363):
                project.FinalReviewQtrlyEst0006days +=1
            elif project.woi and project.stage_id == (3466364):
                project.DeliverQtrlyEst0007days +=1
            elif project.woi and project.stage_id == (3466365):
                project.RolloverProcessQtrlyEst0008days +=1
            else:  
                print("Project not in filtered stages")

            if not project.woi and project.stage_id == (3466358):
                project.ProformadQtrlyEst0001P4 +=1  
            elif not project.woi and project.stage_id == (3466359):
                project.ClientInterviewQtrlyEst0002P4 +=1
            elif not project.woi and project.stage_id == (3466360):
                project.InputPrepQtrlyEst0003P4  +=1
            elif not project.woi and project.stage_id == (3466361):
                project.ReviewQtrlyEst0004P4 +=1
            elif not project.woi and project.stage_id == (3466362):
                project.ClearReviewPointsQtrlyEst0005days +=1              
            elif not project.woi and project.stage_id == (3466363):
                project.FinalReviewQtrlyEst0006P4 +=1
            elif not project.woi and project.stage_id == (3466364):
                project.DeliverQtrlyEst0007P4 +=1
            elif not project.woi and project.stage_id == (3466365):
                project.RolloverProcessQtrlyEst0008P4 +=1
            else:  
                print("Project not in filtered stages")


            project.TotalP4DaysPerStage =   project.ProformadQtrlyEst0001P4 + project.ClientInterviewQtrlyEst0002P4 + project.InputPrepQtrlyEst0003P4  + project.ReviewQtrlyEst0004P4 + project.ClearReviewPointsQtrlyEst0005P4 + project.FinalReviewQtrlyEst0006P4 + project.DeliverQtrlyEst0007P4 + project.RolloverProcessQtrlyEst0008P4 
            project.TotalDaysPerStage = project.ProformadQtrlyEst0001Days + project.ClientInterviewQtrlyEst0002days + project.InputPrepQtrlyEst0003days + project.ReviewQtrlyEst0004days + project.ClearReviewPointsQtrlyEst0005days + project.FinalReviewQtrlyEst0006days + project.DeliverQtrlyEst0007days + project.RolloverProcessQtrlyEst0008days 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage              
   
            if p['PROJECT_NAME'].__contains__('QTR') and p['STATUS'] == 'IN PROGRESS':           
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

 