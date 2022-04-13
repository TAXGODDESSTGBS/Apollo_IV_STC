from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category709gift, Project709gift, Stage709gift, UserModel709gift, Pipeline709gift
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
            pipeline = self.get_obj(Pipeline709gift, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage709gift, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Category709gift, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel709gift, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project709gift, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline709Gift, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel709gift, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category709gift, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.stage = self.get_obj(Stage709gift, p['STAGE_ID'])  

            
            if project.woi and project.stage_id == (1865792):
                project.STARTP4 +=1   
            elif project.woi and project.stage_id == (1774986):
                project.g7090001ProformadP4 +=1 
            elif project.woi and project.stage_id == (1774987):
                project.g7090002IntakeProcessP4 +=1
            elif project.woi and project.stage_id == (1774989):
                project.g7090003BookkeepingReviewTRP4 +=1    
            elif project.woi and project.stage_id == (1774993):
                project.g7090004FinalReviewofBKWPSP4  +=1
            elif project.woi and project.stage_id == (1774994):
                project.g7090005ClearReviewPointsforBKP4 +=1
            elif project.woi and project.stage_id == (1774998):
                project.g7090006InputPrepP4 +=1    
            elif project.woi and project.stage_id == (1774999):
                project.g7090007ReviewP4  +=1
            elif project.woi and project.stage_id == (1775002):
                project.g7090008ClearReviewPointsForTRP4 +=1 
            elif project.woi and project.stage_id == (1775003):
                project.g7090009FinalReviewP4 +=1            
            elif project.woi and project.stage_id == (1775004):
                project.g7090010PartnerSignoffP4 +=1    
            elif project.woi and project.stage_id == (1775005):
                project.g7090011BillPrintTRsP4  +=1 
            elif project.woi and project.stage_id == (1775006):
                project.g7090012AssembleP4 +=1 
            elif project.woi and project.stage_id == (2678149):
                project.g7090013WaitingforSignatureP4 +=1
            elif project.woi and project.stage_id == (1865793):
                project.g7090014CloseOutTaxReturnP4 +=1    
            elif project.woi and project.stage_id == (1774988):
                project.ENDP4  +=1
                           
            else: 
                print("Project not in filtered stages")               
            

            if not project.woi and project.stage_id == (1865792):
                project.START +=1   
            elif not project.woi and project.stage_id == (1774986):
                project.g7090001Proformad +=1 
            elif not project.woi and project.stage_id == (1774987):
                project.g7090002IntakeProcess +=1
            elif not project.woi and project.stage_id == (1774989):
                project.g7090003BookkeepingReviewTR +=1    
            elif not project.woi and project.stage_id == (1774993):
                project.g7090004FinalReviewofBKWPS  +=1
            elif not project.woi and project.stage_id == (1774994):
                project.g7090005ClearReviewPointsforBK +=1
            elif not project.woi and project.stage_id == (1774998):
                project.g7090006InputPrep +=1    
            elif not project.woi and project.stage_id == (1774999):
                project.g7090007Review  +=1
            elif not project.woi and project.stage_id == (1775002):
                project.g7090008ClearReviewPointsForTR +=1 
            elif not project.woi and project.stage_id == (1775003):
                project.g7090009FinalReview +=1            
            elif not project.woi and project.stage_id == (1775004):
                project.g7090010PartnerSignoff +=1    
            elif not project.woi and project.stage_id == (1775005):
                project.g7090011BillPrintTRs  +=1 
            elif not project.woi and project.stage_id == (1775006):
                project.g7090012Assemble +=1 
            elif not project.woi and project.stage_id == (2678149):
                project.g7090013WaitingforSignature +=1
            elif not project.woi and project.stage_id == (1865793):
                project.g7090014CloseOutTaxReturn +=1    
            elif not project.woi and project.stage_id == (1774988):
                project.END  +=1
                           
            else: 
                print("Project not in filtered stages")      


    
            project.TotalP4DaysPerStage = project.STARTP4 + project.g7090001ProformadP4 + project.g7090002IntakeProcessP4 + project.g7090003BookkeepingReviewTRP4 + project.g7090004FinalReviewofBKWPSP4 + project.g7090005ClearReviewPointsforBKP4 + project.g7090006InputPrepP4 + project.g7090007ReviewP4 + project.g7090008ClearReviewPointsForTRP4 + project.g7090009FinalReviewP4 + project.g7090010PartnerSignoffP4 + project.g7090011BillPrintTRsP4 + project.g7090012AssembleP4 + project.g7090013WaitingforSignatureP4 + project.g7090014CloseOutTaxReturnP4 + project.ENDP4 
            project.TotalDaysPerStage = project.START + project.g7090001Proformad + project.g7090002IntakeProcess + project.g7090003BookkeepingReviewTR + project.g7090004FinalReviewofBKWPS + project.g7090005ClearReviewPointsforBK + project.g7090006InputPrep + project.g7090007Review + project.g7090008ClearReviewPointsForTR + project.g7090009FinalReview + project.g7090010PartnerSignoff + project.g7090011BillPrintTRs + project.g7090012Assemble + project.g7090013WaitingforSignature + project.g7090014CloseOutTaxReturn + project.END 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('- 709 Gift -') and p['STATUS'] == 'IN PROGRESS':                 
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

 