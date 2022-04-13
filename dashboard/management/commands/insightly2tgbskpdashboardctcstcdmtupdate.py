from datetime import datetime
from datetime import timezone
#import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Projectctcstcdmtupdate, Stagectcstcdmtupdate
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
        
            
#    def sync_pipelines(self, session):
#        pipelines = session.get_pipelines()
#        for p in pipelines:
#            pipeline = self.get_obj(Pipelinectcstcdmtupdate, p['PIPELINE_ID'])
#            if pipeline.name != p['PIPELINE_NAME']:
#                pipeline.name = p['PIPELINE_NAME']
#                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stagectcstcdmtupdate, s['STAGE_ID'])
            #stage = self.get_obj(Stagectcstcdmtupdate, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
               # pipeline = self.get_obj(Pipelinectcstcdmtupdate, s['PIPELINE_ID'])
             #   pipeline.save()
              #  stage.pipeline = pipeline
                stage.save()

 #   def sync_categories(self, session):
 #       categories = session.get_project_categories()
 #       for c in categories:
 #           category = self.get_obj(Categoryctcstcdmtupdate, c['CATEGORY_ID'])
 #           if category.name != c['CATEGORY_NAME']:
 #               category.name = c['CATEGORY_NAME']
 #               category.save() 

 #   def sync_users(self, session):
 #       users = session.get_users()   
 #       for u in users:
 #           user = self.get_obj(UserModelctcstcdmtupdate, u['USER_ID']) 
 #           if user.name != u['FIRST_NAME']:
 #               user.name = u['FIRST_NAME']
 #               user.save()        
 
    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Projectctcstcdmtupdate, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipelinectcstcdmtupdate, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.starteddate = p['DATE_CREATED_UTC']
           # project.user_responsible = self.get_obj(UserModelctcstcdmtupdate, p['RESPONSIBLE_USER_ID'])
           # project.category = self.get_obj(Categoryctcstcdmtupdate, p['CATEGORY_ID'])
            #project.stage = self.get_obj(Stagectcstcdmtupdate, p['STAGE_ID'])   
            #project.ProjProfileFilter = p['CATEGORY_ID'] == 5726472
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
           # project.stage = self.get_obj(Stagectcstcdmtupdate, p['STAGE_ID'])

            if not project.woi and project.stage_id == (2088051):
                project.startDays +=1   
            elif not project.woi and project.stage_id == (2088052):
                project.billableCTCSTCProject0001SetupClientTasksdays +=1 
            elif not project.woi and project.stage_id == (2088053):
                project.billableCTCSTCProject0002AdminforCTCPlanPrepdays +=1
            elif not project.woi and project.stage_id == (2088054):
                project.billableCTCSTCProject0003CreateIdeasforClientdays +=1
            elif not project.woi and project.stage_id == (2088055):
                project.billableCTCSTCProject0005InputPrepdays +=1              
            elif not project.woi and project.stage_id == (3387176):
                project.billableCTCSTCProject00051QAwiththeclientdays +=1
            elif not project.woi and project.stage_id == (3391762):
                project.billableCTCSTCProject0006ReviewProjectdays +=1
            elif not project.woi and project.stage_id == (3606223):
                project.billableCTCSTCProject0007CLRRVWPTSdays +=1
            elif not project.woi and project.stage_id == (2088057):
                project.billableCTCSTCProject0008FinalReviewdays +=1
            elif not project.woi and project.stage_id == (2088059):
                project.billableCTCSTCProject0009AssembleCTCPlandays +=1
            elif not project.woi and project.stage_id == (2088061):
                project.billableCTCSTCProject0011AdminWrapupdays +=1
            elif not project.woi and project.stage_id == (2088062):
                project.enddays +=1
            else:  
                print("Project not in filtered stages")
            
            if project.woi and project.stage_id == (2088051):
                project.startP4 +=1  
            elif project.woi and project.stage_id == (2088052):
                project.billableCTCSTCProject0001SetupClientTasksP4 +=1 
            elif project.woi and project.stage_id == (2088053):
                project.billableCTCSTCProject0002AdminforCTCPlanPrepP4  +=1
            elif project.woi and project.stage_id == (2088054):
                project.billableCTCSTCProject0003CreateIdeasforClientP4 +=1
            elif project.woi and project.stage_id == (2088055):
                project.billableCTCSTCProject0005InputPrepP4 +=1              
            elif project.woi and project.stage_id == (3387176):
                project.billableCTCSTCProject00051QAwiththeclientP4 +=1
            elif project.woi and project.stage_id == (3391762):
                project.billableCTCSTCProject0006ReviewProjectP4 +=1
            elif project.woi and project.stage_id == (3606223):
                project.billableCTCSTCProject0007CLRRVWPTSP4 +=1
            elif project.woi and project.stage_id == (2088057):
                project.billableCTCSTCProject0008FinalReviewP4 +=1
            elif project.woi and project.stage_id == (2088059):
                project.billableCTCSTCProject0009AssembleCTCPlanP4 +=1
            elif project.woi and project.stage_id == (2088061):
                project.billableCTCSTCProject0011AdminWrapupdays +=1
            elif project.woi and project.stage_id == (2088062):
                project.endP4 +=1
            else:  
                print("Project not in filtered stages")
            
                       
            project.TotalP4DaysPerStage = project.startP4 + project.billableCTCSTCProject0001SetupClientTasksP4 + project.billableCTCSTCProject0002AdminforCTCPlanPrepP4 + project.billableCTCSTCProject0003CreateIdeasforClientP4 + project.billableCTCSTCProject0005InputPrepP4 + project.billableCTCSTCProject00051QAwiththeclientP4 + project.billableCTCSTCProject0006ReviewProjectP4 + project.billableCTCSTCProject0007CLRRVWPTSP4 + project.billableCTCSTCProject0008FinalReviewP4 + project.billableCTCSTCProject0009AssembleCTCPlanP4 + project.billableCTCSTCProject0011AdminWrapupdays + project.endP4
            project.TotalDaysPerStage = project.startDays + project.billableCTCSTCProject0001SetupClientTasksdays + project.billableCTCSTCProject0002AdminforCTCPlanPrepdays + project.billableCTCSTCProject0003CreateIdeasforClientdays + project.billableCTCSTCProject0005InputPrepdays + project.billableCTCSTCProject00051QAwiththeclientdays + project.billableCTCSTCProject0006ReviewProjectdays +  project.billableCTCSTCProject0007CLRRVWPTSdays + project.billableCTCSTCProject0008FinalReviewdays + project.billableCTCSTCProject0009AssembleCTCPlandays + project.billableCTCSTCProject0011AdminWrapupdays + project.enddays
            #project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('STC - UPDATE') and p['STATUS'] == 'IN PROGRESS' or p['PROJECT_NAME'].__contains__('STC - UPDATE') and p['STATUS'] == 'DEFERRED':
                project.stage = self.get_obj(Stagectcstcdmtupdate, p['STAGE_ID'])
                project.save()

   
    def handle(self, *args, **options):
        initial = options['initial']
        with client.Session(settings.INSIGHTLY_API_KEY) as session:
            #self.sync_pipelines(session)
            #self.stdout.write(self.style.SUCCESS('Pipelines synced up...'))            
            self.sync_stages(session)
            self.stdout.write(self.style.SUCCESS('Stages synced up...'))
            #self.sync_categories(session)
           # self.stdout.write(self.style.SUCCESS('Categories synced up...'))
           # self.sync_users(session)
           # self.stdout.write(self.style.SUCCESS('Users synced up...'))
            self.sync_projects(session)
            self.stdout.write(self.style.SUCCESS('Projects synced up...'))
        self.stdout.write(self.style.SUCCESS('Done!'))

 
