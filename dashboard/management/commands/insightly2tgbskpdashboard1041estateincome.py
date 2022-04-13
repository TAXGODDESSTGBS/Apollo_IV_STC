from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1041estateincome, Project1041estateincome, Stage1041estateincome, UserModel1041estateincome, Pipeline1041estateincome
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
            pipeline = self.get_obj(Pipeline1041estateincome, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1041estateincome, s['STAGE_ID'])
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
            category = self.get_obj(Category1041estateincome, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1041estateincome, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1041estateincome, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline1041EstateIncome, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1041estateincome, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1041estateincome, p['CATEGORY_ID'])
            project.ProjProfileFilter = p['CATEGORY_ID'] == 6738467
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = P['STATUS'] == 'IN PROGRESS'
            project.stage = self.get_obj(Stage1041estateincome, p['STAGE_ID'])  

            
            if project.woi and project.stage_id == (1865743):
                project.STARTP4 +=1   
            elif project.woi and project.stage_id == (1774525):
                project.estateincome1041EstateIncome0001ProformadP4 +=1 
            elif project.woi and project.stage_id == (1774535):
                project.estateincome1041EstateIncome0002IntakeProcessP4 +=1
            elif project.woi and project.stage_id == (1774537):
                project.EstateIncome0003BookkeepingReviewTRP4 +=1    
            elif project.woi and project.stage_id == (1774682):
                project.estateincome1041EstateIncome0004FinalReviewofBKWPSP4  +=1            
            elif project.woi and project.stage_id == (1774683):
                project.estateincome1041EstateIncome0005ClearReviewPointsforBKP4 +=1
            elif project.woi and project.stage_id == (1774687):
                project.estateincome1041EstateIncome0006InputPrepP4 +=1    
            elif project.woi and project.stage_id == (1774697):
                project.estateincome1041EstateIncome0007ReviewP4  +=1
            elif project.woi and project.stage_id == (1774718):
                project.estateincome1041EstateIncome0008ClearReviewPointsForTRP4 +=1
            elif project.woi and project.stage_id == (1774719):
                project.EstateIncome0009FinalReviewP4 +=1    
            elif project.woi and project.stage_id == (1774720):
                project.EstateIncome0010PartnerSignoffP4  +=1
            elif project.woi and project.stage_id == (1774722):
                project.estateincome1041EstateIncome0012AssembleP4 +=1
            elif project.woi and project.stage_id == (2678104):
                project.estateincome1041EstateIncome0013WaitingforSignatureP4 +=1    
            elif project.woi and project.stage_id == (1865744):
                project.estateincome1041EstateIncome0014CloseOutTaxReturnP4  +=1
            elif project.woi and project.stage_id == (1774536):
                project.ENDP4  +=1
            
            if not project.woi and project.stage_id == (1865743):
                project.START +=1   
            elif not project.woi and project.stage_id == (1774525):
                project.estateincome1041EstateIncome0001Proformad +=1 
            elif not project.woi and project.stage_id == (1774535):
                project.estateincome1041EstateIncome0002IntakeProcess +=1
            elif not project.woi and project.stage_id == (1774537):
                project.EstateIncome0003BookkeepingReviewTR +=1    
            elif not project.woi and project.stage_id == (1774682):
                project.estateincome1041EstateIncome0004FinalReviewofBKWPS  +=1            
            elif not project.woi and project.stage_id == (1774683):
                project.estateincome1041EstateIncome0005ClearReviewPointsforBK +=1
            elif not project.woi and project.stage_id == (1774687):
                project.estateincome1041EstateIncome0006InputPrep +=1    
            elif not project.woi and project.stage_id == (1774697):
                project.estateincome1041EstateIncome0007Review  +=1
            elif not project.woi and project.stage_id == (1774718):
                project.estateincome1041EstateIncome0008ClearReviewPointsForTR +=1
            elif not project.woi and project.stage_id == (1774719):
                project.EstateIncome0009FinalReview +=1    
            elif not project.woi and project.stage_id == (1774720):
                project.EstateIncome0010PartnerSignoff  +=1
            elif not project.woi and project.stage_id == (1774722):
                project.estateincome1041EstateIncome0012Assemble +=1
            elif not project.woi and project.stage_id == (2678104):
                project.estateincome1041EstateIncome0013WaitingforSignature +=1    
            elif not project.woi and project.stage_id == (1865744):
                project.estateincome1041EstateIncome0014CloseOutTaxReturn  +=1
            elif not project.woi and project.stage_id == (1774536):
                project.END +=1
                           
            else: 
                print("Project not in filtered stages")                 

            project.TotalP4DaysPerStage = project.STARTP4 + project.estateincome1041EstateIncome0001ProformadP4 + project.estateincome1041EstateIncome0002IntakeProcessP4 + project.EstateIncome0003BookkeepingReviewTRP4 + project.estateincome1041EstateIncome0004FinalReviewofBKWPSP4 + project.estateincome1041EstateIncome0005ClearReviewPointsforBKP4 + project.estateincome1041EstateIncome0006InputPrepP4 + project.estateincome1041EstateIncome0007ReviewP4 + project.estateincome1041EstateIncome0008ClearReviewPointsForTRP4 + project.EstateIncome0009FinalReviewP4 + project.EstateIncome0010PartnerSignoffP4 + project.estateincome1041EstateIncome0012AssembleP4 + project.estateincome1041EstateIncome0013WaitingforSignatureP4 + project.estateincome1041EstateIncome0014CloseOutTaxReturnP4 + project.ENDP4
            project.TotalDaysPerStage = project.START + project.estateincome1041EstateIncome0001Proformad + project.estateincome1041EstateIncome0002IntakeProcess + project.EstateIncome0003BookkeepingReviewTR + project.estateincome1041EstateIncome0004FinalReviewofBKWPS + project.estateincome1041EstateIncome0005ClearReviewPointsforBK + project.estateincome1041EstateIncome0006InputPrep + project.estateincome1041EstateIncome0007Review + project.estateincome1041EstateIncome0008ClearReviewPointsForTR + project.EstateIncome0009FinalReview + project.EstateIncome0010PartnerSignoff + project.estateincome1041EstateIncome0012Assemble + project.estateincome1041EstateIncome0013WaitingforSignature + project.estateincome1041EstateIncome0014CloseOutTaxReturn + project.END 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage
            if p['PROJECT_NAME'].__contains__('1041 Estate Income') and p['STATUS'] == 'IN PROGRESS':
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

 