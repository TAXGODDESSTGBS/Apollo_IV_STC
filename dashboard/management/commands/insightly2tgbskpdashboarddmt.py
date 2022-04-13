from datetime import datetime
from datetime import timezone
#import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Project, Stage
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
        
            
  #  def sync_pipelines(self, session):
   #     pipelines = session.get_pipelines()
    ##    for p in pipelines:
     #       pipeline = self.get_obj(Pipeline, p['PIPELINE_ID'])
     #       if pipeline.name != p['PIPELINE_NAME']:
     #           pipeline.name = p['PIPELINE_NAME']
     #           pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                stage.save()

    #def sync_categories(self, session):
    #    categories = session.get_project_categories()
    #    for c in categories:
    #        category = self.get_obj(Category, c['CATEGORY_ID'])
    #        if category.name != c['CATEGORY_NAME']:
    #            category.name = c['CATEGORY_NAME']
    #            category.save() 

    #def sync_users(self, session):
    #    users = session.get_users()   
    #    for u in users:
    #        user = self.get_obj(UserModel, u['USER_ID']) 
    #        if user.name != u['FIRST_NAME']:
    #            user.name = u['FIRST_NAME']
    #            user.save()        

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            project.project_status = p['STATUS'] 
            project.starteddate = p['DATE_CREATED_UTC'] 
            #project.datecreated = p['DATE_CREATED_UTC']
            project.datecompleted = p['COMPLETED_DATE']
           # project.user_responsible = self.get_obj(UserModel, p['RESPONSIBLE_USER_ID'])
           # project.category = self.get_obj(Category, p['CATEGORY_ID'])           
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'

            #project.stage = self.get_obj(Stage, p['STAGE_ID']) 

            if not project.woi and project.stage_id == (2718328):
                project.startDays +=1   
            elif not project.woi and project.stage_id == (2718329):
                project.billabledmtproject0001setupclienttasksdays +=1 
            elif not project.woi and project.stage_id == (2718331):
                project.billabledmtproject0002createideasforclientdays +=1
            elif not project.woi and project.stage_id == (2718332):
                project.billabledmtproject0003inputprepbillableinputprepdays +=1
            elif not project.woi and project.stage_id == (3678053):
                project.billabledmtproject00031qawiththeclientdays +=1              
            elif not project.woi and project.stage_id == (3514023):
                project.billabledmtproject1streviewdays +=1
            elif not project.woi and project.stage_id == (3514024):
                project.billabledmtprojectclrrvwptsdays +=1
            elif not project.woi and project.stage_id == (2718333):
                project.billabledmtproject0004finalreviewdays +=1
            elif not project.woi and project.stage_id == (2718334):
                project.billabledmtproject0005assemblectcplandays +=1
            elif not project.woi and project.stage_id == (2718335):
                project.billabledmtproject0006adminwrapupdays +=1
            elif not project.woi and project.stage_id == (2718336):
                project.enddays +=1
            else:  
                print("Project not in filtered stages")

            if project.woi and project.stage_id == (2718328):
                project.startP4 +=1   
            elif project.woi and project.stage_id == (2718329):
                project.billabledmtproject0001setupclienttasksP4 +=1 
            elif project.woi and project.stage_id == (2718331):
                project.billabledmtproject0002createideasforclientP4  +=1
            elif project.woi and project.stage_id == (2718332):
                project.billabledmtproject0003inputprepbillableinputprepP4 +=1
            elif project.woi and project.stage_id == (3678053):
                project.billabledmtproject00031qawiththeclientP4 +=1             
            elif project.woi and project.stage_id == (3514023):
                project.billabledmtproject1streviewP4 +=1 
            elif project.woi and project.stage_id == (3514024):
                project.billabledmtprojectclrrvwptsP4 +=1
            elif project.woi and project.stage_id == (2718333):
                project.billabledmtproject0004finalreviewP4 +=1
            elif project.woi and project.stage_id == (2718334):
                project.billabledmtproject0005assemblectcplanP4 +=1
            elif project.woi and project.stage_id == (2718335):
                project.billabledmtproject0006adminwrapupP4 +=1
            elif project.woi and project.stage_id == (2718336):
                project.endP4 +=1
            else:  
                print("Project not in filtered stages")

            project.TotalP4DaysPerStage = project.startP4 + project.billabledmtproject0001setupclienttasksP4 + project.billabledmtproject0002createideasforclientP4 + project.billabledmtproject0003inputprepbillableinputprepP4 + project.billabledmtproject00031qawiththeclientP4 + project.billabledmtproject1streviewP4 + project.billabledmtprojectclrrvwptsP4 + project.billabledmtproject0004finalreviewP4 + project.billabledmtproject0005assemblectcplanP4 + project.billabledmtproject0006adminwrapupP4 + project.endP4
            project.TotalDaysPerStage = project.startDays + project.billabledmtproject0001setupclienttasksdays + project.billabledmtproject0002createideasforclientdays + project.billabledmtproject0003inputprepbillableinputprepdays + project.billabledmtproject00031qawiththeclientdays + project.billabledmtproject1streviewdays + project.billabledmtprojectclrrvwptsdays + project.billabledmtproject0004finalreviewdays + project.billabledmtproject0005assemblectcplandays + project.billabledmtproject0006adminwrapupdays + project.enddays 
            #project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 

            if p['PROJECT_NAME'].__contains__('DMT') and p['STATUS'] == 'IN PROGRESS' or p['PROJECT_NAME'].__contains__('DMT') and p['STATUS'] == 'DEFERRED':
                project.stage = self.get_obj(Stage, p['STAGE_ID'])
                project.save()
    
   
    def handle(self, *args, **options):
        initial = options['initial']
        with client.Session(settings.INSIGHTLY_API_KEY) as session:
            #self.sync_pipelines(session)
            #self.stdout.write(self.style.SUCCESS('Pipelines synced up...'))            
            self.sync_stages(session)
            self.stdout.write(self.style.SUCCESS('Stages synced up...'))
            #self.sync_categories(session)
            #self.stdout.write(self.style.SUCCESS('Categories synced up...'))
            #self.sync_users(session)
            #self.stdout.write(self.style.SUCCESS('Users synced up...'))
            self.sync_projects(session)
            self.stdout.write(self.style.SUCCESS('Projects synced up...'))
        self.stdout.write(self.style.SUCCESS('Done!'))

 
