from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1040, Project1040, Stage1040, UserModel1040, Pipeline1040
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
            pipeline = self.get_obj(Pipeline1040, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1040, s['STAGE_ID'])
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
            category = self.get_obj(Category1040, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1040, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1040, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1040, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1040, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'

            project.stage = self.get_obj(Stage1040, p['STAGE_ID'])

            if project.woi and project.stage_id == (1865743):
                project.Proformad10400001P4 +=1   
            elif project.woi and project.stage_id == (3235444):
                project.Intakes10400002P4 +=1 
            elif project.woi and project.stage_id == (3235445):
                project.BKKPNGRevTRPrintRevPreCompileP4 +=1   
            elif project.woi and project.stage_id == (3235490):
                project.FinalReviewofBKWPS10400004P4 +=1    
            elif project.woi and project.stage_id == (3235491):
                project.ClearReviewPointsforBk10400005P4  +=1
            elif project.woi and project.stage_id == (3235492):
                project.InputPrep10400006P4 +=1 
            elif project.woi and project.stage_id == (3235493):
                project.Waitingonk110400007P4 +=1   
            elif project.woi and project.stage_id == (3235494):
                project.Review10400008P4 +=1    
            elif project.woi and project.stage_id == (3235495):
                project.ClearReviewPointsTR10400009P4  +=1
            elif project.woi and project.stage_id == (3235496):
                project.Finalize1stReview10400010P4 +=1 
            elif project.woi and project.stage_id == (3235497):
                project.FinalReview10400011P4 +=1   
            elif project.woi and project.stage_id == (3235507):
                project.PartnerSignoff10400012P4 +=1    
            elif project.woi and project.stage_id == (3235508):
                project.BillPrintTRsAssembly10400013P4 +=1
            elif project.woi and project.stage_id == (3235509):
                project.WaitingforClientSignature10400014P4 +=1 
            elif project.woi and project.stage_id == (3235510):
                project.CloseOutTaxReturn10400015P4 +=1   
            elif project.woi and project.stage_id == (3235511):
                project.FeeAnalysis10400018P4 +=1    
            elif project.woi and project.stage_id == (3235512):
                project.RolloverProcess10400019P4  +=1
                           
            else: 
                print("Project not in filtered stages")   

            if not project.woi and project.stage_id == (1865743):
                project.Proformad10400001 +=1   
            elif not project.woi and project.stage_id == (3235444):
                project.Intakes10400002 +=1 
            elif not project.woi and project.stage_id == (3235445):
                project.BKKPNGRevTRPrintRevPreCompile +=1   
            elif not project.woi and project.stage_id == (3235490):
                project.FinalReviewofBKWPS10400004 +=1    
            elif not project.woi and project.stage_id == (3235491):
                project.ClearReviewPointsforBk10400005  +=1
            elif not project.woi and project.stage_id == (3235492):
                project.InputPrep10400006 +=1 
            elif not project.woi and project.stage_id == (3235493):
                project.Waitingonk110400007 +=1   
            elif not project.woi and project.stage_id == (3235494):
                project.Review10400008 +=1    
            elif not project.woi and project.stage_id == (3235495):
                project.ClearReviewPointsTR10400009  +=1
            elif not project.woi and project.stage_id == (3235496):
                project.Finalize1stReview10400010 +=1 
            elif not project.woi and project.stage_id == (3235497):
                project.FinalReview10400011 +=1   
            elif not project.woi and project.stage_id == (3235507):
                project.PartnerSignoff10400012 +=1    
            elif not project.woi and project.stage_id == (3235508):
                project.BillPrintTRsAssembly10400013 +=1
            elif not project.woi and project.stage_id == (3235509):
                project.WaitingforClientSignature10400014 +=1 
            elif not project.woi and project.stage_id == (3235510):
                project.CloseOutTaxReturn10400015 +=1   
            elif not project.woi and project.stage_id == (3235511):
                project.FeeAnalysis10400018 +=1    
            elif not project.woi and project.stage_id == (3235512):
                project.RolloverProcess10400019  +=1
                           
            else: 
                print("Project not in filtered stages")  

   
            project.TotalP4DaysPerStage = project.Proformad10400001P4 + project.Intakes10400002P4 + project.BKKPNGRevTRPrintRevPreCompileP4 + project.FinalReviewofBKWPS10400004P4 + project.ClearReviewPointsforBk10400005P4 + project.InputPrep10400006P4 + project.Waitingonk110400007P4 + project.Review10400008P4 + project.ClearReviewPointsTR10400009P4 + project.Finalize1stReview10400010P4 + project.FinalReview10400011P4 + project.PartnerSignoff10400012P4 + project.BillPrintTRsAssembly10400013P4 + project.WaitingforClientSignature10400014P4 + project.CloseOutTaxReturn10400015P4 + project.FeeAnalysis10400018P4 + project.RolloverProcess10400019P4 
            project.TotalDaysPerStage = project.Proformad10400001 + project.Intakes10400002 + project.BKKPNGRevTRPrintRevPreCompile + project.FinalReviewofBKWPS10400004 + project.ClearReviewPointsforBk10400005 + project.InputPrep10400006 + project.Waitingonk110400007 + project.Review10400008 + project.ClearReviewPointsTR10400009 + project.Finalize1stReview10400010 + project.FinalReview10400011 + project.PartnerSignoff10400012 + project.BillPrintTRsAssembly10400013 + project.WaitingforClientSignature10400014 + project.CloseOutTaxReturn10400015 + project.FeeAnalysis10400018 + project.RolloverProcess10400019 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage
            if p['PROJECT_NAME'].__contains__('- 1040 -') and p['STATUS'] == 'IN PROGRESS':
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

 