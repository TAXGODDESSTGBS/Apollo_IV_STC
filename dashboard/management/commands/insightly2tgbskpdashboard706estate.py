from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category706estate, Project706estate, Stage706estate, UserModel706estate, Pipeline706estate
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
            pipeline = self.get_obj(Pipeline706estate, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage706estate, s['STAGE_ID'])
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
            category = self.get_obj(Category706estate, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel706estate, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project706estate, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel706estate, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category706estate, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            project.stage = self.get_obj(Stage706estate, p['STAGE_ID'])    

            if project.woi and project.stage_id == (1865790):
                project.STARTP4 +=1   
            elif project.woi and project.stage_id == (1774943):
                project.e7060001ProformadP4 +=1 
            elif project.woi and project.stage_id == (1774944):
                project.e7060002IntakeProcessP4 +=1
            elif project.woi and project.stage_id == (1774955):
                project.e7060003BookkeepingReviewTRP4 +=1 
            elif project.woi and project.stage_id == (1774959):
                project.e7060004FinalReviewofBKWPSP4 +=1
            elif project.woi and project.stage_id == (1774960):
                project.e7060005ClearReviewPointsforBKP4 +=1 
            elif project.woi and project.stage_id == (1774964):
                project.e7060006InputPrepP4 +=1
            elif project.woi and project.stage_id == (1774965):
                project.e7060007ReviewP4 +=1 
            elif project.woi and project.stage_id == (1774968):
                project.e7060008ClearReviewPointsForTRP4 +=1
            elif project.woi and project.stage_id == (1774969):
                project.e7060009FinalReviewP4 +=1 
            elif project.woi and project.stage_id == (1774970):
                project.e7060010PartnerSignoffP4 +=1
            elif project.woi and project.stage_id == (1774971):
                project.e7060011BillPrintTRsP4 +=1
            elif project.woi and project.stage_id == (1774972):
                project.e7060012AssembleP4 +=1
            elif project.woi and project.stage_id == (2678148):
                project.e7060013WaitingforSignatureP4 +=1
            elif project.woi and project.stage_id == (1865791):
                project.e7060014CloseOutTaxReturnP4 +=1            
            elif project.woi and project.stage_id == (1774954):
                project.ENDP4 +=1
            else:  
                print("Project not in filtered stages")
            

            if not project.woi and project.stage_id == (1865790):
                project.START +=1   
            elif not project.woi and project.stage_id == (1774943):
                project.e7060001Proformad +=1 
            elif not project.woi and project.stage_id == (1774944):
                project.e7060002IntakeProcess +=1
            elif not project.woi and project.stage_id == (1774955):
                project.e7060003BookkeepingReviewTR +=1 
            elif not project.woi and project.stage_id == (1774959):
                project.e7060004FinalReviewofBKWPS +=1
            elif not project.woi and project.stage_id == (1774960):
                project.e7060005ClearReviewPointsforBK +=1 
            elif not project.woi and project.stage_id == (1774964):
                project.e7060006InputPrep +=1
            elif not project.woi and project.stage_id == (1774965):
                project.e7060007Review +=1 
            elif not project.woi and project.stage_id == (1774968):
                project.e7060008ClearReviewPointsForTR +=1
            elif not project.woi and project.stage_id == (1774969):
                project.e7060009FinalReview +=1 
            elif not project.woi and project.stage_id == (1774970):
                project.e7060010PartnerSignoff +=1
            elif not project.woi and project.stage_id == (1774971):
                project.e7060011BillPrintTRs +=1
            elif not project.woi and project.stage_id == (1774972):
                project.e7060012Assemble +=1
            elif not project.woi and project.stage_id == (2678148):
                project.e7060013WaitingforSignature +=1
            elif not project.woi and project.stage_id == (1865791):
                project.e7060014CloseOutTaxReturn +=1            
            elif not project.woi and project.stage_id == (1774954):
                project.END +=1    
            else:  
                print("Project not in filtered stages")

   
            project.TotalP4DaysPerStage = project.STARTP4 + project.e7060001ProformadP4 + project.e7060002IntakeProcessP4 + project.e7060003BookkeepingReviewTRP4 + project.e7060004FinalReviewofBKWPSP4 + project.e7060005ClearReviewPointsforBKP4 + project.e7060006InputPrepP4 + project.e7060007ReviewP4 + project.e7060008ClearReviewPointsForTRP4 + project.e7060009FinalReviewP4 + project.e7060010PartnerSignoffP4 + project.e7060011BillPrintTRsP4 + project.e7060012AssembleP4 + project.e7060013WaitingforSignatureP4 + project.e7060014CloseOutTaxReturnP4 + project.ENDP4 
            project.TotalDaysPerStage = project.START + project.e7060001Proformad + project.e7060002IntakeProcess + project.e7060003BookkeepingReviewTR + project.e7060004FinalReviewofBKWPS + project.e7060005ClearReviewPointsforBK + project.e7060006InputPrep + project.e7060007Review + project.e7060008ClearReviewPointsForTR + project.e7060009FinalReview + project.e7060010PartnerSignoff + project.e7060011BillPrintTRs + project.e7060012Assemble + project.e7060013WaitingforSignature + project.e7060014CloseOutTaxReturn + project.END 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('- 706 Estate -') and p['STATUS'] == 'IN PROGRESS':
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

 