from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1041trust, Project1041trust, Stage1041trust, UserModel1041trust, Pipeline1041trust
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
            pipeline = self.get_obj(Pipeline1041trust, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1041trust, s['STAGE_ID'])
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
            category = self.get_obj(Category1041trust, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1041trust, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1041trust, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline1041Trust, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1041trust, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1041trust, p['CATEGORY_ID'])
            project.ProjProfileFilter = p['CATEGORY_ID'] == 6738467
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'

            project.stage = self.get_obj(Stage1041trust, p['STAGE_ID']) 

            if project.woi and project.stage_id == (1865754):
                project.STARTP4 +=1   
            elif project.woi and project.stage_id == (1774471):
                project.trust1041Trust0001ProformadP4 +=1 
            elif project.woi and project.stage_id == (1774474):
                project.trust1041Trust0002IntakeProcessP4 +=1            
            elif project.woi and project.stage_id == (1774478):
                project.trust1041Trust0003BookkeepingReviewTRP4 +=1    
            elif project.woi and project.stage_id == (1774482):
                project.trust1041Trust0004FinalReviewofBKWPSP4  +=1
            elif project.woi and project.stage_id == (1774483):
                project.trust1041Trust0005ClearReviewPointsforBKP4 +=1 
            elif project.woi and project.stage_id == (1774496):
                project.trust1041Trust0006InputPrepP4 +=1            
            elif project.woi and project.stage_id == (1774497):
                project.trust1041Trust0007ReviewP4 +=1    
            elif project.woi and project.stage_id == (1774500):
                project.trust1041Trust0008ClearReviewPointsForTRP4 +=1
            elif project.woi and project.stage_id == (1774501):
                project.trust1041Trust0009FinalReviewP4 +=1 
            elif project.woi and project.stage_id == (1774502):
                project.trust1041Trust0010PartnerSignoffP4 +=1            
            elif project.woi and project.stage_id == (1774503):
                project.trust1041Trust0011BillPrintTRsP4 +=1    
            elif project.woi and project.stage_id == (1774504):
                project.trust1041Trust0012AssembleP4 +=1
            elif project.woi and project.stage_id == (2678105):
                project.trust1041Trust0013WaitingforSignatureP4  +=1
            elif project.woi and project.stage_id == (1865755):
                project.trust1041Trust0014CloseOutTaxReturnP4 +=1 
            elif project.woi and project.stage_id == (1774476):
                project.ENDP4 +=1 
                           
            else: 
                print("Project not in filtered stages")               

            if not project.woi and project.stage_id == (1865754)
                project.START +=1   
            elif not project.woi and project.stage_id == (1774471)
                project.trust1041Trust0001Proformad +=1 
            elif not project.woi and project.stage_id == (1774474)
                project.trust1041Trust0002IntakeProcess +=1            
            elif not project.woi and project.stage_id == (1774478)
                project.trust1041Trust0003BookkeepingReviewTR +=1    
            elif not project.woi and project.stage_id == (1774482)
                project.trust1041Trust0004FinalReviewofBKWPS +=1
            elif not project.woi and project.stage_id == (1774483)
                project.trust1041Trust0005ClearReviewPointsforBK +=1 
            elif not project.woi and project.stage_id == (1774496)
                project.trust1041Trust0006InputPrep +=1            
            elif not project.woi and project.stage_id == (1774497)
                project.trust1041Trust0007Review +=1    
            elif not project.woi and project.stage_id == (1774500)
                project.trust1041Trust0008ClearReviewPointsForTR +=1
            elif not project.woi and project.stage_id == (1774501)
                project.trust1041Trust0009FinalReview +=1 
            elif not project.woi and project.stage_id == (1774502)
                project.trust1041Trust0010PartnerSignoff +=1            
            elif not project.woi and project.stage_id == (1774503)
                project.trust1041Trust0011BillPrintTRs +=1    
            elif not project.woi and project.stage_id == (1774504)
                project.trust1041Trust0012Assemble +=1
            elif not project.woi and project.stage_id == (2678105)
                project.trust1041Trust0013WaitingforSignature +=1
            elif not project.woi and project.stage_id == (1865755)
                project.trust1041Trust0014CloseOutTaxReturn +=1 
            elif not project.woi and project.stage_id == (1774476)
                project.END +=1 
                           
            else: 
                print("Project not in filtered stages")    


            project.TotalP4DaysPerStage = project.STARTP4 + project.trust1041Trust0001ProformadP4 + project.trust1041Trust0002IntakeProcessP4 + project.trust1041Trust0003BookkeepingReviewTRP4 + project.trust1041Trust0004FinalReviewofBKWPSP4 + project.trust1041Trust0005ClearReviewPointsforBKP4 + project.trust1041Trust0006InputPrepP4 + project.trust1041Trust0007ReviewP4 + project.trust1041Trust0008ClearReviewPointsForTRP4 + project.trust1041Trust0009FinalReviewP4 + project.trust1041Trust0010PartnerSignoffP4 + project.trust1041Trust0011BillPrintTRsP4 + project.trust1041Trust0012AssembleP4 + project.trust1041Trust0013WaitingforSignatureP4 + project.trust1041Trust0014CloseOutTaxReturnP4 + project.ENDP4 
            project.TotalDaysPerStage = project.START + project.trust1041Trust0001Proformad + project.trust1041Trust0002IntakeProcess + project.trust1041Trust0003BookkeepingReviewTR + project.trust1041Trust0004FinalReviewofBKWPS + project.trust1041Trust0005ClearReviewPointsforBK + project.trust1041Trust0006InputPrep + project.trust1041Trust0007Review + project.trust1041Trust0008ClearReviewPointsForTR + project.trust1041Trust0009FinalReview + project.trust1041Trust0010PartnerSignoff + project.trust1041Trust0011BillPrintTRs + project.trust1041Trust0012Assemble + project.trust1041Trust0013WaitingforSignature + project.trust1041Trust0014CloseOutTaxReturn + project.END  
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage
            if p['PROJECT_NAME'].__contains__('- 1041 Trust') and p['STATUS'] == 'IN PROGRESS':
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

 