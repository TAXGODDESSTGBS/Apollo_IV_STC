from datetime import datetime
from datetime import timezone
#import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Categorymonthlyperiodic, Projectmonthlyperiodic, Stagemonthlyperiodic, UserModelmonthlyperiodic, Pipelinemonthlyperiodic
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
        
            
    #def sync_pipelines(self, session):
    #    pipelines = session.get_pipelines()
    #    for p in pipelines:
    #        pipeline = self.get_obj(Pipelinemonthlyperiodic, p['PIPELINE_ID'])
    #        if pipeline.name != p['PIPELINE_NAME']:
     #           pipeline.name = p['PIPELINE_NAME']
    #            pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stagemonthlyperiodic, s['STAGE_ID'])
            #stage = self.get_obj(Stagemonthlyperiodic, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                #pipeline = self.get_obj(Pipelinemonthlyperiodic, s['PIPELINE_ID'])
                #pipeline.save()
                #stage.pipeline = pipeline
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Categorymonthlyperiodic, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModelmonthlyperiodic, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
 
    def sync_projects(self, session):
        #sessions = Session.objects.filter(expire_date__gte=datetime.now())
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Projectmonthlyperiodic, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipelinemonthlyperiodic, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModelmonthlyperiodic, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Categorymonthlyperiodic, p['CATEGORY_ID'])            
            project.ProjProfileFilter = p['CATEGORY_ID'] == 5726472
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.stage = self.get_obj(Stagemonthlyperiodic, p['STAGE_ID']) 
                      
            if not project.woi and project.stage_id == (1865811):
                project.startDays +=1   
            elif not project.woi and project.stage_id == (1775307):
                project.profitCentsMonthlyReports0001InputPrepdays +=1 
            elif not project.woi and project.stage_id == (1775308):
                project.profitCentsMonthlyReports0002Reviewdays +=1
            elif not project.woi and project.stage_id == (1775309):
                project.profitCentsMonthlyReports0003ClearReviewPointsdays +=1
            elif not project.woi and project.stage_id == (1865812):
                project.enddays +=1
            else:  
                print("Project not in filtered stages")
            
            
            if project.woi and project.stage_id == (1865811):
                project.startP4 +=1    
            elif project.woi and project.stage_id == (1775307):
                project.profitCentsMonthlyReports0001InputPrepP4 +=1 
            elif project.woi and project.stage_id == (1775308):
                project.profitCentsMonthlyReports0002ReviewP4  +=1
            elif project.woi and project.stage_id == (1775309):
                project.profitCentsMonthlyReports0003ClearReviewPointsP4 +=1
            elif project.woi and project.stage_id == (1865812):
                project.endP4 +=1
            else:  
                print("Project not in filtered stages")
          
           

            project.TotalP4DaysPerStage =  project.startP4 + project.profitCentsMonthlyReports0001InputPrepP4 + project.profitCentsMonthlyReports0002ReviewP4  + project.profitCentsMonthlyReports0003ClearReviewPointsP4 + project.endP4 
            project.TotalDaysPerStage =   project.startDays + project.profitCentsMonthlyReports0001InputPrepdays + project.profitCentsMonthlyReports0002Reviewdays + project.profitCentsMonthlyReports0003ClearReviewPointsdays + project.enddays
            if p['PROJECT_NAME'].__contains__('Monthly/Periodic') and p['STATUS'] == 'IN PROGRESS':
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

 