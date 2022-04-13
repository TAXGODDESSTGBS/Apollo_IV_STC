from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1120S, Project1120S, Stage1120S, UserModel1120S, Pipeline1120S
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
            pipeline = self.get_obj(Pipeline1120S, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1120S, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Category1120S, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1120S, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1120S, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline1120S, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1120S, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1120S, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = P['STATUS'] == 'IN PROGRESS'
             
            
            if project.woi and project.stage_id == (3253317):
                project.Proformad1120s0001P4 +=1   
            elif project.woi and project.stage_id == (3253318):
                project.Intakes1120s0002P4 +=1  
            elif project.woi and project.stage_id == (3253319):
                project.BKKPNGRevTRPrintRevPreComp3P4 +=1 
            elif project.woi and project.stage_id == (3253329):
                project.FinalReviewofBKWPS1120s0004P4 +=1   
            elif project.woi and project.stage_id == (3253330):
                project.ClearReviewPointsforBk1120s0005P4  +=1 
            elif project.woi and project.stage_id == (3253331):
                project.InputPrep1120s0006P4 +=1  
            elif project.woi and project.stage_id == (3253332):
                project.Waitingonk11120s0007P4 +=1             
            elif project.woi and project.stage_id == (3253333):
                project.Review1120s0008P4 +=1     
            elif project.woi and project.stage_id == (3253334):
                project.ClearReviewPoints1120s0009P4  +=1 
            elif project.woi and project.stage_id == (3253335):
                project.Finalize1stReview1120s0010P4 +=1 
            elif project.woi and project.stage_id == (3253336):
                project.FinalReview1120s0011P4 +=1            
            elif project.woi and project.stage_id == (3253337):
                project.PartnerSignoff1120s0012P4 +=1     
            elif project.woi and project.stage_id == (3253338):
                project.BillPrintAssembly1120s0013P4 +=1 
            elif project.woi and project.stage_id == (3253340):
                project.WaitingforClientSignature1120s0014P4 +=1 
            elif project.woi and project.stage_id == (3253341):
                project.CloseOutTaxReturn1120s0015P4 +=1            
            elif project.woi and project.stage_id == (3253342):
                project.FeeAnalysis1120s0016P4 +=1  
            elif project.woi and project.stage_id == (3253352):
                project.RolloverProcess1120s0017P4 +=1 
                       
            else: 
                print("Project not in filtered stages")      

            if not project.woi and project.stage_id == (3253317):
                project.Proformad1120s0001 +=1
            elif not project.woi and project.stage_id == (3253318):
                project.Intakes1120s0002 +=1
            elif not project.woi and project.stage_id == (3253319):
                project.BKKPNGRevTRPrintRevPreComp3 +=1           
            elif not project.woi and project.stage_id == (3253329):
                project.FinalReviewofBKWPS1120s0004 +=1     
            elif not project.woi and project.stage_id == (3253330):
                project.ClearReviewPointsforBk1120s0005  +=1 
            elif not project.woi and project.stage_id == (3253331):
                project.InputPrep1120s0006 +=1 
            elif not project.woi and project.stage_id == (3253332):
                project.Waitingonk11120s0007 +=1            
            elif not project.woi and project.stage_id == (3253333):
                project.Review1120s0008 +=1     
            elif not project.woi and project.stage_id == (3253334):
                project.ClearReviewPoints1120s0009  +=1 
            elif not project.woi and project.stage_id == (3253335):
                project.Finalize1stReview1120s0010 +=1  
            elif not project.woi and project.stage_id == (3253336):
                project.FinalReview1120s0011 +=1            
            elif not project.woi and project.stage_id == (3253337):
                project.PartnerSignoff1120s0012 +=1    
            elif not project.woi and project.stage_id == (3253338):
                project.BillPrintAssembly1120s0013 +=1 
            elif not project.woi and project.stage_id == (3253340):
                project.WaitingforClientSignature1120s0014 +=1  
            elif not project.woi and project.stage_id == (3253341):
                project.CloseOutTaxReturn1120s0015 +=1            
            elif not project.woi and project.stage_id == (3253342):
                project.FeeAnalysis1120s0016 +=1   
            elif not project.woi and project.stage_id == (3253352):
                project.RolloverProcess1120s0017 +=1 
                       
            else: 
                print("Project not in filtered stages") 

            project.TotalP4DaysPerStage = project.Proformad1120s0001P4 + project.Intakes1120s0002P4 + project.BKKPNGRevTRPrintRevPreComp3P4 + project.FinalReviewofBKWPS1120s0004P4 + project.ClearReviewPointsforBk1120s0005P4 + project.InputPrep1120s0006P4 + project.Waitingonk11120s0007P4 + project.Review1120s0008P4 + project.ClearReviewPoints1120s0009P4 + project.Finalize1stReview1120s0010P4 + project.FinalReview1120s0011P4 + project.PartnerSignoff1120s0012P4 + project.BillPrintAssembly1120s0013P4 + project.WaitingforClientSignature1120s0014P4 + project.CloseOutTaxReturn1120s0015P4 + project.FeeAnalysis1120s0016P4 + project.RolloverProcess1120s0017P4 
            project.TotalDaysPerStage = project.Proformad1120s0001 + project.Intakes1120s0002 + project.BKKPNGRevTRPrintRevPreComp3 + project.FinalReviewofBKWPS1120s0004 + project.ClearReviewPointsforBk1120s0005 + project.InputPrep1120s0006 + project.Waitingonk11120s0007 + project.Review1120s0008 + project.ClearReviewPoints1120s0009 + project.Finalize1stReview1120s0010 + project.FinalReview1120s0011 + project.PartnerSignoff1120s0012 + project.BillPrintAssembly1120s0013 + project.WaitingforClientSignature1120s0014 + project.CloseOutTaxReturn1120s0015 + project.FeeAnalysis1120s0016 + project.RolloverProcess1120s0017 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('1120S -') and p['STATUS'] == 'IN PROGRESS':
                project.stage = self.get_obj(Stage1120S, p['STAGE_ID'])
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

 