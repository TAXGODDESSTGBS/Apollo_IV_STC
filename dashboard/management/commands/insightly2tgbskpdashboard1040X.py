from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1040X, Project1040X, Stage1040X, UserModel1040X, Pipeline1040X
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
            pipeline = self.get_obj(Pipeline1040X, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1040X, s['STAGE_ID'])
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
            category = self.get_obj(Category1040X, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1040X, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1040x, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1040X, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1040X, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            project.stage = self.get_obj(Stage1040X, p['STAGE_ID'])  
          
            if project.woi and project.stage_id == (3240583):
                project.Proformad1040X0001P4 +=1   
            elif project.woi and project.stage_id == (3240584):
                project.Intakes1040X0002P4 +=1 
            elif project.woi and project.stage_id == (3240585):
                project.BKKPNGRFORTRPRINTReviewPreCompile40XP4 +=1            
            elif project.woi and project.stage_id == (3240586):
                project.FinalReviewofBKWPS1040X0004P4 +=1    
            elif project.woi and project.stage_id == (3240587):
                project.ClearReviewPointsforBk1040X0005P4 +=1   
            elif project.woi and project.stage_id == (3240587):
                project.InputPrep1040X0006P4 +=1 
            elif project.woi and project.stage_id == (3240588):
                project.Waitingonk11040X0007P4 +=1 
            elif project.woi and project.stage_id == (3240589):
                project.Review1040X0008P4 +=1         
            elif project.woi and project.stage_id == (3240588):
                project.ClearReviewPointsTR1040X0009P4 +=1 
            elif project.woi and project.stage_id == (3240589):
                project.Finalize1stReview1040X0010P4 +=1            
            elif project.woi and project.stage_id == (3240590):
                project.FinalReview1040X0011P4 +=1    
            elif project.woi and project.stage_id == (3240591):
                project.PartnerSignoff1040X0012P4  +=1            
            elif project.woi and project.stage_id == (3240592):
                project.BillPrintTRsAssembly1040X0013P4 +=1 
            elif project.woi and project.stage_id == (3240593):
                project.WaitingforClientSignature1040X0014P4 +=1            
            elif project.woi and project.stage_id == (3240594):
                project.CloseOutTaxReturn1040X0015P4 +=1    
            elif project.woi and project.stage_id == (3240595):
                project.FeeAnalysis1040X0016P4 +=1
            elif project.woi and project.stage_id == (3240596):
                project.RolloverProcess1040X0017P4  +=1
            elif project.woi and project.stage_id == (3240606):
                project.FeeAnalysis1040X0016P4 +=1
            elif project.woi and project.stage_id == (3240607):
                project.RolloverProcess1040X0017P4  +=1
            elif project.woi and project.stage_id == (3240608):
                project.RolloverProcess1040X0017P4  +=1
                           
            else: 
                print("Project not in filtered stages")   

            if not project.woi and project.stage_id == (3240583):
                project.Proformad1040X0001 +=1   
            elif not project.woi and project.stage_id == (3240584):
                project.Intakes1040X0002 +=1 
            elif not project.woi and project.stage_id == (3240585):
                project.BKKPNGRFORTRPRINTReviewPreCompile40X +=1            
            elif not project.woi and project.stage_id == (3240586):
                project.FinalReviewofBKWPS1040X0004 +=1    
            elif not project.woi and project.stage_id == (3240587):
                project.ClearReviewPointsforBk1040X0005 +=1 
            elif not project.woi and project.stage_id == (3240588):
                project.InputPrep1040X0006 +=1 
            elif not project.woi and project.stage_id == (3240588):
                project.Waitingonk11040X0007 +=1 
            elif not project.woi and project.stage_id == (3240589):
                project.Review1040X0008 +=1            
            elif not project.woi and project.stage_id == (3240590):
                project.ClearReviewPointsTR1040X0009 +=1    
            elif not project.woi and project.stage_id == (3240591):
                project.Finalize1stReview1040X0010  +=1            
            elif not project.woi and project.stage_id == (3240592):
                project.FinalReview1040X0011 +=1 
            elif not project.woi and project.stage_id == (3240593):
                project.PartnerSignoff1040X0012 +=1            
            elif not project.woi and project.stage_id == (3240594):
                project.BillPrintTRsAssembly1040X0013 +=1    
            elif not project.woi and project.stage_id == (3240595):
                project.FeeAnalysis1040X0016 +=1
            elif not project.woi and project.stage_id == (3240596):
                project.WaitingforClientSignature1040X0014  +=1
            elif not project.woi and project.stage_id == (3240607):
                project.CloseOutTaxReturn1040X0015 +=1    
            elif not project.woi and project.stage_id == (3240595):
                project.FeeAnalysis1040X0016 +=1
            elif not project.woi and project.stage_id == (3240608):
                project.RolloverProcess1040X0017  +=1
                           
            else: 
                print("Project not in filtered stages")   

            project.TotalP4DaysPerStage = project.Proformad1040X0001P4 + project.Intakes1040X0002P4 + project.BKKPNGRFORTRPRINTReviewPreCompile40XP4 + project.FinalReviewofBKWPS1040X0004P4 + project.ClearReviewPointsforBk1040X0005P4 + project.InputPrep1040X0006P4 + project.Waitingonk11040X0007P4 + project.Review1040X0008P4 + project.ClearReviewPointsTR1040X0009P4 + project.Finalize1stReview1040X0010P4 + project.FinalReview1040X0011P4 + project.PartnerSignoff1040X0012P4 + project.BillPrintTRsAssembly1040X0013P4 + project.WaitingforClientSignature1040X0014P4 + project.CloseOutTaxReturn1040X0015P4 + project.eeAnalysis1040X0016P4 + project.RolloverProcess1040X0017P4
            project.TotalDaysPerStage = project.Proformad1040X0001 + project.Intakes1040X0002 + project.BKKPNGRFORTRPRINTReviewPreCompile40X + project.FinalReviewofBKWPS1040X0004 + project.ClearReviewPointsforBk1040X0005 + project.InputPrep1040X0006 + project.Waitingonk11040X0007 + project.Review1040X0008 + project.ClearReviewPointsTR1040X0009 + project.Finalize1stReview1040X0010 + project.FinalReview1040X0011 + project.PartnerSignoff1040X0012 + project.BillPrintTRsAssembly1040X0013 + project.WaitingforClientSignature1040X0014 + project.CloseOutTaxReturn1040X0015 + project.eeAnalysis1040X0016 + project.RolloverProcess1040X0017
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('- 1040X') and p['STATUS'] == 'IN PROGRESS':
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

 