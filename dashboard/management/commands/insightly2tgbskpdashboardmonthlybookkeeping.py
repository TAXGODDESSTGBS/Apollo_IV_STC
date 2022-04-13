from datetime import datetime
from datetime import timezone
#import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Categorymonthlybookkeeping, Projectmonthlybookkeeping, Stagemonthlybookkeeping, UserModelmonthlybookkeeping, Pipelinemonthlybookkeeping
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
            pipeline = self.get_obj(Pipelinemonthlybookkeeping, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stagemonthlybookkeeping, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Categorymonthlybookkeeping, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModelmonthlybookkeeping, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        #sessions = Session.objects.filter(expire_date__gte=datetime.now())
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Projectmonthlybookkeeping, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipelinemonthlybookkeeping, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModelmonthlybookkeeping, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Categorymonthlybookkeeping, p['CATEGORY_ID'])
            project.ProjProfileFilter = p['CATEGORY_ID'] == 3469859
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            
            project.stage = self.get_obj(Stagemonthlybookkeeping, p['STAGE_ID'])           

            if not project.woi and project.stage_id == (1865809):
                project.SetupDays +=1   
            elif not project.woi and project.stage_id == (1775042):
                project.MonthlyBKP0001InputReconciledays +=1 
            elif not project.woi and project.stage_id == (1775046):
                project.MonthlyBKP0002SelfReviewPrintWPSdays +=1
            elif not project.woi and project.stage_id == (2961567):
                project.MonthlyBKP0003ReviewWPSdays +=1
            elif not project.woi and project.stage_id == (1775047):
                project.MonthlyBKP0004ClearReviewPointsdays +=1              
            elif not project.woi and project.stage_id == (1775048):
                project.MonthlyBKP0005FinalReviewdays +=1
            elif not project.woi and project.stage_id == (3764286):
                project.MonthlyBKP00060BooksDonebutWOIfromClientdays +=1
            elif not project.woi and project.stage_id == (3766433):
                project.MonthlyBKP00061Rereviewwithclientsadditionalanswersdays +=1
            elif not project.woi and project.stage_id == (1775043):
                project.MonthlyBKP0006FinalCPAsignoffsendtoclientdays +=1
            elif not project.woi and project.stage_id == (1865810):
                project.MonthlyBKPENDdays +=1
            else:  
                print("Project not in filtered stages")

            
            if project.woi and project.stage_id == (1865809):
                project.SetupP4 +=1   
            elif project.woi and project.stage_id == (1775042):
                project.MonthlyBKP0001InputReconcileP4 +=1
            elif project.woi and project.stage_id == (1775046):
                project.MonthlyBKP0002SelfReviewPrintWPSP4  +=1
            elif project.woi and project.stage_id == (2961567):
                project.MonthlyBKP0003ReviewWPSP4 +=1
            elif project.woi and project.stage_id == (1775047):
                project.MonthlyBKP0004ClearReviewPointsP4 +=1              
            elif project.woi and project.stage_id == (1775048):
                project.MonthlyBKP0005FinalReviewP4 +=1
            elif project.woi and project.stage_id == (3764286):
                project.MonthlyBKP00060BooksDonebutWOIfromClientP4 +=1
            elif project.woi and project.stage_id == (3766433):
                project.MonthlyBKP00061RereviewwithclientsadditionalanswersP4 +=1
            elif project.woi and project.stage_id == (1775043):
                project.MonthlyBKP0006FinalCPAsignoffsendtoclientP4 +=1
            elif project.woi and project.stage_id == (1865810):
                project.MonthlyBKPENDP4 +=1
            else:  
                print("Project not in filtered stages")

            project.TotalP4DaysPerStage = project.SetupP4 + project.MonthlyBKP0001InputReconcileP4 + project.MonthlyBKP0002SelfReviewPrintWPSP4  + project.MonthlyBKP0003ReviewWPSP4 + project.MonthlyBKP0004ClearReviewPointsP4 + project.MonthlyBKP0005FinalReviewP4 + project.MonthlyBKP00060BooksDonebutWOIfromClientP4 + project.MonthlyBKP00061RereviewwithclientsadditionalanswersP4 + project.MonthlyBKP0006FinalCPAsignoffsendtoclientP4 + project.MonthlyBKPENDP4 
            project.TotalDaysPerStage = project.SetupDays + project.MonthlyBKP0001InputReconciledays + project.MonthlyBKP0002SelfReviewPrintWPSdays + project.MonthlyBKP0003ReviewWPSdays + project.MonthlyBKP0004ClearReviewPointsdays + project.MonthlyBKP0005FinalReviewdays + project.MonthlyBKP00060BooksDonebutWOIfromClientdays + project.MonthlyBKP00061Rereviewwithclientsadditionalanswersdays + project.MonthlyBKP0006FinalCPAsignoffsendtoclientdays + project.MonthlyBKPENDdays 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('Monthly Bookkeeping') and p['STATUS'] == 'IN PROGRESS':    
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

 