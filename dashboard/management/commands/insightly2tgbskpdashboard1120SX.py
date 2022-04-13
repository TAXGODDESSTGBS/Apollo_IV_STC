from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1120SX, Project1120SX, Stage1120SX, UserModel1120SX, Pipeline1120SX
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
            pipeline = self.get_obj(Pipeline1120SX, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1120SX, s['STAGE_ID'])
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
            category = self.get_obj(Category1120SX, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1120SX, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1120SX, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline1120SX, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1120SX, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1120SX, p['CATEGORY_ID'])
            project.ProjProfileFilter = p['CATEGORY_ID'] == 6738467
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = P['STATUS'] == 'IN PROGRESS'
            project.stage = self.get_obj(Stage1120SX, p['STAGE_ID']) 

            if project.woi and project.stage_id == (1865786):
                project.STARTP4 +=1   
            elif project.woi and project.stage_id == (1774839):
                project.sx1120SX0001IntakeProcessP4 +=1 
            elif project.woi and project.stage_id == (1774850):
                project.sx1120SX0002PrintPBCFinancialStatementsforBKTRRVWP4 +=1            
            elif project.woi and project.stage_id == (1774852):
                project.sx1120SX0003BookkeepingReviewTRP4 +=1    
            elif project.woi and project.stage_id == (1774865):
                project.sx1120SX0004FinalReviewofBKWPSP4 +=1
            elif project.woi and project.stage_id == (1774866):
                project.sx1120SX0005ClearReviewPointsforBKP4 +=1 
            elif project.woi and project.stage_id == (1774870):
                project.sx1120SX0006InputPrepP4 +=1            
            elif project.woi and project.stage_id == (1774872):
                project.sx1120SX0007ReviewP4 +=1    
            elif project.woi and project.stage_id == (1774876):
                project.sx1120SX0008ClearReviewPointsForTRP4 +=1
            elif project.woi and project.stage_id == (1774877):
                project.sx1120SX0009FinalReviewP4 +=1 
            elif project.woi and project.stage_id == (1774879):
                project.sx1120SX0010PartnerSignoffP4 +=1            
            elif project.woi and project.stage_id == (1774880):
                project.sx1120SX0011BillPrintTRsP4 +=1    
            elif project.woi and project.stage_id == (1774882):
                project.sx1120SX0012AssembleP4 +=1
            elif project.woi and project.stage_id == (2678128):
                project.sx120SX0013WaitingforSignatureP4 +=1 
            elif project.woi and project.stage_id == (1865787):
                project.sx1120SX0014CloseOutTaxReturnP4 +=1            
            elif project.woi and project.stage_id == (1774840):
                project.sx1120SX0014ENDP4 +=1  

            if not project.woi and project.stage_id == (1865786)::
                project.START +=1   
            elif not project.woi and project.stage_id == (1774839):
                project.sx1120SX0001IntakeProcess +=1 
            elif not project.woi and project.stage_id == (1774850):
                project.sx1120SX0002PrintPBCFinancialStatementsforBKTRRVW +=1            
            elif not project.woi and project.stage_id == (1774852):
                project.sx1120SX0003BookkeepingReviewTR +=1    
            elif not project.woi and project.stage_id == (1774865):
                project.sx1120SX0004FinalReviewofBKWPS +=1
            elif not project.woi and project.stage_id == (1774866):
                project.sx1120SX0005ClearReviewPointsforBK +=1 
            elif not project.woi and project.stage_id == (1774870):
                project.sx1120SX0006InputPrep +=1            
            elif not project.woi and project.stage_id == (1774872):
                project.sx1120SX0007Review +=1    
            elif not project.woi and project.stage_id == (1774876):
                project.sx1120SX0008ClearReviewPointsForTR +=1
            elif not project.woi and project.stage_id == (1774877):
                project.sx1120SX0009FinalReview +=1 
            elif not project.woi and project.stage_id == (1774879):
                project.sx1120SX0010PartnerSignoff +=1            
            elif not project.woi and project.stage_id == (1774880):
                project.sx1120SX0011BillPrintTRs +=1    
            elif not project.woi and project.stage_id == (1774882):
                project.sx1120SX0012AssembleP4 +=1
            elif not project.woi and project.stage_id == (2678128):
                project.sx120SX0013WaitingforSignature +=1 
            elif not project.woi and project.stage_id == (1865787):
                project.sx1120SX0014CloseOutTaxReturn +=1            
            elif not project.woi and project.stage_id == (1774840):
                project.sx1120SX0014END +=1    
  
            else: 
                print("Project not in filtered stages") 


            project.TotalP4DaysPerStage = project.STARTP4 + project.sx1120SX0001IntakeProcessP4 + project.sx1120SX0002PrintPBCFinancialStatementsforBKTRRVWP4 + project.sx1120SX0003BookkeepingReviewTRP4 + project.sx1120SX0004FinalReviewofBKWPSP4 + project.sx1120SX0005ClearReviewPointsforBKP4 + project.sx1120SX0006InputPrepP4 + project.sx1120SX0007ReviewP4 + project.sx1120SX0008ClearReviewPointsForTRP4 + project.sx1120SX0009FinalReviewP4 + project.sx1120SX0010PartnerSignoffP4 + project.sx1120SX0011BillPrintTRsP4 + project.sx1120SX0012AssembleP4 + project.sx120SX0013WaitingforSignatureP4 + project.sx1120SX0014CloseOutTaxReturnP4 + project.sx1120SX0014ENDP4
            project.TotalDaysPerStage = project.START + project.sx1120SX0001IntakeProcess + project.sx1120SX0002PrintPBCFinancialStatementsforBKTRRVW + project.sx1120SX0003BookkeepingReviewTR + project.sx1120SX0004FinalReviewofBKWPS + project.sx1120SX0005ClearReviewPointsforBK + project.sx1120SX0006InputPrep + project.sx1120SX0007Review + project.sx1120SX0008ClearReviewPointsForTR + project.sx1120SX0009FinalReview + project.sx1120SX0010PartnerSignoff + project.sx1120SX0011BillPrintTRs + project.sx1120SX0012Assemble + project.sx120SX0013WaitingforSignature + project.sx1120SX0014CloseOutTaxReturn + project.sx1120SX0014END 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('1120SX -') and p['STATUS'] == 'IN PROGRESS':
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

 