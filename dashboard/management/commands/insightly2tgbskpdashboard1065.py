from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1065, Project1065, Stage1065, UserModel1065, Pipeline1065
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
            pipeline = self.get_obj(Pipeline1065, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1065, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                #pipeline = self.get_obj(Pipeline13WCF, s['PIPELINE_ID'])
                #pipeline.save()
                #stage.pipeline = pipeline
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Category1065, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1065, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1065, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline1065, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1065, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1065, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            project.stage = self.get_obj(Stage1065, p['STAGE_ID'])   

            if project.woi and project.stage_id == (3387173):
                project.Proformad10650001P4 +=1   
            elif project.woi and project.stage_id == (3387176):
                project.Intakes10650002P4 +=1 
            elif project.woi and project.stage_id == (3387191):
                project.BKPNGRevTRPrintRevPreCompileP4 +=1            
            elif project.woi and project.stage_id == (3387221):
                project.FinalReviewofBKWPS10650004P4 +=1    
            elif project.woi and project.stage_id == (3387571):
                project.ClearReviewPointsforBKWPS10650005P4  +=1
            elif project.woi and project.stage_id == (3387572):
                project.InputPrep10650006P4 +=1   
            elif project.woi and project.stage_id == (3387644):
                project.WaitingonK110650007P4 +=1 
            elif project.woi and project.stage_id == (3387645):
                project.Review10650008P4 +=1            
            elif project.woi and project.stage_id == (3387646):
                project.ClearReviewPointsforTR10650009P4 +=1    
            elif project.woi and project.stage_id == (3387656):
                project.Finalize1stReview10650010P4 +=1
            elif project.woi and project.stage_id == (3387666):
                project.FinalReview10650011P4 +=1   
            elif project.woi and project.stage_id == (3387667):
                project.PartnerSignoff10650012P4 +=1 
            elif project.woi and project.stage_id == (3387668):
                project.BillPrintAssembly10650013P4 +=1            
            elif project.woi and project.stage_id == (3387680):
                project.WaitingforClientSignature10650014P4 +=1    
            elif project.woi and project.stage_id == (3387690):
                project.CloseOutTR10650015P4 +=1
            if project.woi and project.stage_id == (3387692):
                project.FeeAnalysis10650016P4 +=1   
            elif project.woi and project.stage_id == (3387696):
                project.Rollover10650017P4 +=1 
            
            else:
                print("Project does not meet criteria")
            
            if not project.woi and project.stage_id == (3387173):
                project.Proformad10650001 +=1   
            elif not project.woi and project.stage_id == (3387176):
                project.Intakes10650002 +=1 
            elif not project.woi and project.stage_id == (3387191):
                project.BKPNGRevTRPrintRevPreCompile +=1            
            elif not project.woi and project.stage_id == (3387221):
                project.FinalReviewofBKWPS10650004 +=1    
            elif not project.woi and project.stage_id == (3387571):
                project.ClearReviewPointsforBKWPS10650005  +=1
            elif not project.woi and project.stage_id == (3387572):
                project.InputPrep10650006 +=1   
            elif not project.woi and project.stage_id == (3387644):
                project.WaitingonK110650007 +=1 
            elif not project.woi and project.stage_id == (3387645):
                project.Review10650008 +=1            
            elif not project.woi and project.stage_id == (3387646):
                project.ClearReviewPointsforTR10650009 +=1    
            elif not project.woi and project.stage_id == (3387656):
                project.Finalize1stReview10650010 +=1
            elif not project.woi and project.stage_id == (3387666):
                project.FinalReview10650011 +=1   
            elif not project.woi and project.stage_id == (3387667):
                project.PartnerSignoff10650012 +=1 
            elif not project.woi and project.stage_id == (3387668):
                project.BillPrintAssembly10650013 +=1            
            elif not project.woi and project.stage_id == (3387680):
                project.WaitingforClientSignature10650014 +=1    
            elif not project.woi and project.stage_id == (3387690):
                project.CloseOutTR10650015 +=1
            if not project.woi and project.stage_id == (3387692):
                project.FeeAnalysis10650016 +=1   
            elif not project.woi and project.stage_id == (3387696):
                project.Rollover10650017 +=1

            else:
                print("Project does not meet criteria") 


            project.TotalP4DaysPerStage = project.Proformad10650001P4 + project.Intakes10650002P4 + project.BKPNGRevTRPrintRevPreCompileP4 + project.FinalReviewofBKWPS10650004P4 + project.ClearReviewPointsforBKWPS10650005P4 + project.InputPrep10650006P4 + project.WaitingonK110650007P4 + project.Review10650008P4 + project.ClearReviewPointsforTR10650009P4 + project.Finalize1stReview10650010P4 + project.FinalReview10650011P4 + project.PartnerSignoff10650012P4 + project.BillPrintAssembly10650013P4 + project.WaitingforClientSignature10650014P4 + project.CloseOutTR10650015P4 + project.FeeAnalysis10650016P4 + project.Rollover10650017P4  
            project.TotalDaysPerStage = project.Proformad10650001 + project.Intakes10650002 + project.BKPNGRevTRPrintRevPreCompile + project.FinalReviewofBKWPS10650004 + project.ClearReviewPointsforBKWPS10650005 + project.InputPrep10650006 + project.WaitingonK110650007 + project.Review10650008 + project.ClearReviewPointsforTR10650009 + project.Finalize1stReview10650010 + project.FinalReview10650011 + project.PartnerSignoff10650012 + project.BillPrintAssembly10650013 + project.WaitingforClientSignature10650014 + project.CloseOutTR10650015 + project.FeeAnalysis10650016 + project.Rollover10650017
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('- 1065 -') and p['STATUS'] == 'IN PROGRESS':
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

 