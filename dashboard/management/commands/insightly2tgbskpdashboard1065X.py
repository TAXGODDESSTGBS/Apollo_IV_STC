from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1065X, Project1065X, Stage1065X, UserModel1065X, Pipeline1065X
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
            pipeline = self.get_obj(Pipeline1065X, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1065X, s['STAGE_ID'])
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
            category = self.get_obj(Category1065X, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1065X, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1065X, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline1065X, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1065X, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1065X, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            project.stage = self.get_obj(Stage1065X, p['STAGE_ID']) 

            if project.woi and project.stage_id == (1865758):
                project.STARTP4 +=1   
            elif project.woi and project.stage_id == (1774756):
                project.x1065X0001IntakeProcessP4 +=1 
            elif project.woi and project.stage_id == (1774758):
                project.x1065X0002PrintPBCFinancialStatementsforBKTRRVWP4 +=1            
            elif project.woi and project.stage_id == (1774759):
                project.x1065X0003BookkeepingReviewTRP4 +=1    
            elif project.woi and project.stage_id == (1774763):
                project.x1065X0004FinalReviewofBKWPSP4  +=1
            elif project.woi and project.stage_id == (1774764):
                project.x1065X0005ClearReviewPointsforBKP4 +=1 
            elif project.woi and project.stage_id == (1774768):
                project.x1065X0006InputPrepP4 +=1            
            elif project.woi and project.stage_id == (1774769):
                project.x1065X0007ReviewP4 +=1    
            elif project.woi and project.stage_id == (1774772):
                project.x1065X0008ClearReviewPointsForTRP4  +=1
            elif project.woi and project.stage_id == (1774773):
                project.x1065X0009FinalReviewP4 +=1 
            elif project.woi and project.stage_id == (1774774):
                project.x1065X0010PartnerSignoffP4 +=1            
            elif project.woi and project.stage_id == (1774775):
                project.x1065X0011BillPrintTRsP4 +=1    
            elif project.woi and project.stage_id == (1774776):
                project.x1065X0012AssembleP4  +=1
            elif project.woi and project.stage_id == (2678116):
                project.x1065X0013WaitingforSignatureP4 +=1 
            elif project.woi and project.stage_id == (1865768):
                project.x1065X0014CloseOutTaxReturnP4 +=1            
            elif project.woi and project.stage_id == (1774757):
                project.x1065X0015ENDP4 +=1   
            else: 
                print("Project not in filtered stages")      

            if not project.woi and project.stage_id == (1865758):
                project.START +=1   
            elif not project.woi and project.stage_id == (1774756):
                project.x1065X0001IntakeProcess +=1 
            elif not project.woi and project.stage_id == (1774758):
                project.x1065X0002PrintPBCFinancialStatementsforBKTRRVW +=1            
            elif not project.woi and project.stage_id == (1774759):
                project.x1065X0003BookkeepingReviewTR +=1    
            elif not project.woi and project.stage_id == (1774763):
                project.x1065X0004FinalReviewofBKWPS  +=1
            elif not project.woi and project.stage_id == (1774764):
                project.x1065X0005ClearReviewPointsforBK +=1 
            elif not project.woi and project.stage_id == (1774768):
                project.x1065X0006InputPrep +=1            
            elif not project.woi and project.stage_id == (1774769):
                project.x1065X0007Review +=1    
            elif not project.woi and project.stage_id == (1774772):
                project.x1065X0008ClearReviewPointsForTR  +=1
            elif not project.woi and project.stage_id == (1774773):
                project.x1065X0009FinalReview +=1 
            elif not project.woi and project.stage_id == (1774774):
                project.x1065X0010PartnerSignoff +=1            
            elif not project.woi and project.stage_id == (1774775):
                project.x1065X0011BillPrintTRs +=1    
            elif not project.woi and project.stage_id == (1774776):
                project.x1065X0012Assemble  +=1
            elif not project.woi and project.stage_id == (2678116):
                project.x1065X0013WaitingforSignature +=1 
            elif not project.woi and project.stage_id == (1865768):
                project.x1065X0014CloseOutTaxReturn +=1            
            elif not project.woi and project.stage_id == (1774757):
                project.x1065X0015END +=1 
            else: 
                print("Project not in filtered stages")      
   
            project.TotalP4DaysPerStage = project.STARTP4 + project.x1065X0001IntakeProcessP4 + project.x1065X0002PrintPBCFinancialStatementsforBKTRRVWP4 + project.x1065X0003BookkeepingReviewTRP4 + project.x1065X0004FinalReviewofBKWPSP4 + project.x1065X0005ClearReviewPointsforBKP4 + project.x1065X0006InputPrepP4 + project.x1065X0007ReviewP4 + project.x1065X0008ClearReviewPointsForTRP4 + project.x1065X0009FinalReviewP4 + project.x1065X0010PartnerSignoffP4 + project.x1065X0011BillPrintTRsP4 + project.x1065X0012AssembleP4 + project.x1065X0013WaitingforSignatureP4 + project.x1065X0014CloseOutTaxReturnP4 + project.x1065X0015ENDP4 
            project.TotalDaysPerStage = project.START + project.x1065X0001IntakeProcess + project.x1065X0002PrintPBCFinancialStatementsforBKTRRVW + project.x1065X0003BookkeepingReviewTR + project.x1065X0004FinalReviewofBKWPS + project.x1065X0005ClearReviewPointsforBK + project.x1065X0006InputPrep + project.x1065X0007Review + project.x1065X0008ClearReviewPointsForTR + project.x1065X0009FinalReview + project.x1065X0010PartnerSignoff + project.x1065X0011BillPrintTRs + project.x1065X0012Assemble + project.x1065X0013WaitingforSignature + project.x1065X0014CloseOutTaxReturn + project.x1065X0015END
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage
            if p['PROJECT_NAME'].__contains__('- 1065X') and p['STATUS'] == 'IN PROGRESS':
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

 