from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Category1120, Project1120, Stage1120, UserModel1120, Pipeline1120
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
            pipeline = self.get_obj(Pipeline1120, p['PIPELINE_ID'])
            if pipeline.name != p['PIPELINE_NAME']:
                pipeline.name = p['PIPELINE_NAME']
                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1120, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Category1120, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModel1120, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1120, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline1120, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModel1120, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Category1120, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'            
            project.stage = self.get_obj(Stage1120, p['STAGE_ID']) 
            if project.woi and project.stage_id == (3391761): 
                project.Proformad11200001P4 +=1   
            elif project.woi and project.stage_id == (3391762): 
                project.intakes11200002P4 +=1 
            elif project.woi and project.stage_id == (3391763): 
                project.BKPNGRevTRPrintRevPreCompile113P4 +=1            
            elif project.woi and project.stage_id == (3391764): 
                project.FinalReviewofBKWPS11200004P4 +=1    
            elif project.woi and project.stage_id == (3391765): 
                project.ClearReviewPointsforBk11200005P4  +=1
            elif project.woi and project.stage_id == (3391766): 
                project.InputPrep11200006P4 +=1 
            elif project.woi and project.stage_id == (3391767): 
                project.Waitingonk111200007P4 +=1            
            elif project.woi and project.stage_id == (3391768): 
                project.Review11200008P4 +=1    
            elif project.woi and project.stage_id == (3391769): 
                project.ClearReviewPoints11200009P4 +=1
            elif project.woi and project.stage_id == (3391770): 
                project.Finalize1stReview11200010P4 +=1 
            elif project.woi and project.stage_id == (3391771): 
                project.FinalReview11200011P4 +=1            
            elif project.woi and project.stage_id == (3391772): 
                project.PartnerSignoff11200012P4 +=1    
            elif project.woi and project.stage_id == (3391773):
                project.BillPrintAssembly11200013P4 +=1
            elif project.woi and project.stage_id == (3391774):  
                project.WaitingforClientSignature11200014P4 +=1 
            elif project.woi and project.stage_id == (3391775): 
                project.CloseOutTaxReturn11200015P4 +=1            
            elif project.woi and project.stage_id == (3391776): 
                project.FeeAnalysis11200016P4 +=1    
            elif project.woi and project.stage_id == (3391796): 
                project.Rollover11200017P4  +=1

            else:  
                print("Project not in filtered stages")

            if not project.woi and project.stage_id == (3391761): 
                project.Proformad11200001 +=1   
            elif not project.woi and project.stage_id == (3391762): 
                project.intakes11200002 +=1 
            elif not project.woi and project.stage_id == (3391763): 
                project.BKPNGRevTRPrintRevPreCompile113 +=1            
            elif not project.woi and project.stage_id == (3391764): 
                project.FinalReviewofBKWPS11200004 +=1    
            elif not project.woi and project.stage_id == (3391765): 
                project.ClearReviewPointsforBk11200005  +=1
            elif not project.woi and project.stage_id == (3391766): 
                project.InputPrep11200006 +=1 
            elif not project.woi and project.stage_id == (3391767):  
                project.Waitingonk111200007 +=1            
            elif not project.woi and project.stage_id == (3391768):  
                project.Review11200008 +=1    
            elif not project.woi and project.stage_id == (3391769):  
                project.ClearReviewPoints11200009 +=1
            elif not project.woi and project.stage_id == (3391770): 
                project.Finalize1stReview11200010 +=1 
            elif not project.woi and project.stage_id == (3391771):  
                project.FinalReview11200011 +=1            
            elif not project.woi and project.stage_id == (3391772):  
                project.PartnerSignoff11200012 +=1    
            elif not project.woi and project.stage_id == (3391773):    
                project.BillPrintAssembly11200013  +=1
            elif not project.woi and project.stage_id == (3391774):   
                project.WaitingforClientSignature11200014 +=1 
            elif not project.woi and project.stage_id == (3391775):   
                project.CloseOutTaxReturn11200015 +=1            
            elif not project.woi and project.stage_id == (3391776):      
                project.FeeAnalysis11200016 +=1    
            elif not project.woi and project.stage_id == (3391796):    
                project.Rollover11200017 +=1

            else:  
                print("Project not in filtered stages")

                       
            project.TotalP4DaysPerStage = project.Proformad11200001P4 + project.intakes11200002P4 + project.BKPNGRevTRPrintRevPreCompile113P4 + project.FinalReviewofBKWPS11200004P4 + project.ClearReviewPointsforBk11200005P4 + project.InputPrep11200006P4 + project.Waitingonk111200007P4 + project.Review11200008P4 + project.ClearReviewPoints11200009P4 + project.Finalize1stReview11200010P4 + project.FinalReview11200011P4 + project.PartnerSignoff11200012P4 + project.BillPrintAssembly11200013P4 + project.WaitingforClientSignature11200014P4 + project.CloseOutTaxReturn11200015P4 + project.FeeAnalysis11200016P4 + project.Rollover11200017P4 
            project.TotalDaysPerStage = project.Proformad11200001 + project.intakes11200002 + project.BKPNGRevTRPrintRevPreCompile113 + project.FinalReviewofBKWPS11200004 + project.ClearReviewPointsforBk11200005 + project.InputPrep11200006 + project.Waitingonk111200007 + project.Review11200008 + project.ClearReviewPoints11200009 + project.Finalize1stReview11200010 + project.FinalReview11200011 + project.PartnerSignoff11200012 + project.BillPrintAssembly11200013 + project.WaitingforClientSignature11200014 + project.CloseOutTaxReturn11200015 + project.FeeAnalysis11200016 + project.Rollover11200017 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            if p['PROJECT_NAME'].__contains__('1120 -') and p['STATUS'] == 'IN PROGRESS':
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

 