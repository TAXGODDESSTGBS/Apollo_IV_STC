from datetime import datetime
from datetime import timezone
#import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Projectctcstcproject, Stagectcstcproject
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

   # def sync_pipelines(self, session):
   #     pipelines = session.get_pipelines()
   #     for p in pipelines:
   #         pipeline = self.get_obj(Pipelinectcstcproject, p['PIPELINE_ID'])
   #         if pipeline.name != p['PIPELINE_NAME']:
   #             pipeline.name = p['PIPELINE_NAME']
   #             pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stagectcstcproject, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                stage.save()

    #def sync_categories(self, session):
    #    categories = session.get_project_categories()
    #    for c in categories:
    #        category = self.get_obj(Categoryctcstcproject, c['CATEGORY_ID'])
    #        if category.name != c['CATEGORY_NAME']:
    #            category.name = c['CATEGORY_NAME']
    #            category.save() 

#    def sync_users(self, session):
#        users = session.get_users()   
#        for u in users:
#            user = self.get_obj(UserModelctcstcproject, u['USER_ID']) 
#            if user.name != u['FIRST_NAME']:
#                user.name = u['FIRST_NAME']
#                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Projectctcstcproject, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipelinectcstcproject, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.starteddate = p['DATE_CREATED_UTC']
            #project.user_responsible = self.get_obj(UserModelctcstcproject, p['RESPONSIBLE_USER_ID'])
            #project.category = self.get_obj(Categoryctcstcproject, p['CATEGORY_ID'])
            project.stage = self.get_obj(Stagectcstcproject, p['STAGE_ID'])  
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            #project.stage = self.get_obj(Stagectcstcproject, p['STAGE_ID']) 
            
            
            if not project.woi and project.stage_id == (3860697):
                project.ProformadSTCCTC0001 +=1 
            elif not project.woi and project.stage_id == (3860698):
                project.IntakesSTCCTC0002 +=1 
            elif not project.woi and project.stage_id == (3860699):
                project.CreateIdeasforClientSTCCTC0003 +=1
            elif not project.woi and project.stage_id == (3860709):
                project.InputPrepSTCCTC0004 +=1
            elif not project.woi and project.stage_id == (3860710):
                project.ReviewProjectSTCCTC0006 +=1
            elif not project.woi and project.stage_id == (3871142):
                project.ClearReviewPointsSTCCTC0007 +=1
            elif not project.woi and project.stage_id == (3860711):
                project.FinalReviewSTCCTC0008 +=1
            elif not project.woi and project.stage_id == (3860712):
                project.AssembleSTCCTC0009 +=1
            elif not project.woi and project.stage_id == (3860713):
                project.WrapupSTCCTC0010 +=1
            elif not project.woi and project.stage_id == (3860714):
                project.CSFUPALLSTCCTC0011 +=1
            elif not project.woi and project.stage_id == (3860715):
                project.SalesFUPALLSTCCTC0012 +=1
            elif not project.woi and project.stage_id == (3860716):
                project.RolloverSTCCTC0013 +=1
            elif not project.woi and project.stage_id == (3870230):
                project.QAwithClientSTCCTC0005 +=1
            else:  
                print("Project not in filtered stages")
            
            
            if project.woi and project.stage_id == (3860697):
                project.ProformadSTCCTC0001P4 +=1   
            elif project.woi and project.stage_id == (3860698):
                project.IntakesSTCCTC0002P4 +=1 
            elif project.woi and project.stage_id == (3860699):
                project.CreateIdeasforClientSTCCTC0003P4  +=1
            elif project.woi and project.stage_id == (3860709):
                project.InputPrepSTCCTC0004P4 +=1
            elif project.woi and project.stage_id == (3860710):
                project.ReviewProjectSTCCTC0006P4 +=1
            elif project.woi and project.stage_id == (3871142):
                project.ClearReviewPointsSTCCTC0007P4 +=1
            elif project.woi and project.stage_id == (3860711):
                project.FinalReviewSTCCTC0008P4 +=1
            elif project.woi and project.stage_id == (3860712):
                project.AssembleSTCCTC0009P4 +=1
            elif project.woi and project.stage_id == (3860713):
                project.WrapupSTCCTC0010P4 +=1
            elif project.woi and project.stage_id == (3860714):
                project.CSFUPALLSTCCTC0011P4 +=1
            elif project.woi and project.stage_id == (3860715):
                project.SalesFUPALLSTCCTC0012P4 +=1
            elif project.woi and project.stage_id == (3860716):
                project.RolloverSTCCTC0013P4 +=1
            elif project.woi and project.stage_id == (3870230):
                project.QAwithClientSTCCTC0005 +=1
            else:  
                print("Project not in filtered stages")
        
            project.TotalP4DaysPerStage = project.ProformadSTCCTC0001P4 + project.IntakesSTCCTC0002P4 + project.CreateIdeasforClientSTCCTC0003P4 + project.InputPrepSTCCTC0004P4 + project.ReviewProjectSTCCTC0006P4 + project.ClearReviewPointsSTCCTC0007P4 + project.FinalReviewSTCCTC0008P4 + project.AssembleSTCCTC0009P4 + project.WrapupSTCCTC0010P4 + project.CSFUPALLSTCCTC0011P4 + project.SalesFUPALLSTCCTC0012P4 + project.RolloverSTCCTC0013P4 + project.QAwithClientSTCCTC0005P4
            project.TotalDaysPerStage = project.ProformadSTCCTC0001 + project.IntakesSTCCTC0002 + project.CreateIdeasforClientSTCCTC0003 + project.InputPrepSTCCTC0004 + project.ReviewProjectSTCCTC0006 + project.ClearReviewPointsSTCCTC0007 + project.FinalReviewSTCCTC0008 + project.AssembleSTCCTC0009 + project.WrapupSTCCTC0010 + project.CSFUPALLSTCCTC0011 + project.SalesFUPALLSTCCTC0012 + project.RolloverSTCCTC0013 + project.QAwithClientSTCCTC0005
            #project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage
            if p['PROJECT_NAME'].__contains__('STC') and p['STATUS'] == 'IN PROGRESS' or p['PROJECT_NAME'].__contains__('CTC') and p['STATUS'] == 'IN PROGRESS' or p['PROJECT_NAME'].__contains__('CTC') and p['STATUS'] == 'DEFERRED':
                project.stage = self.get_obj(Stagectcstcproject, p['STAGE_ID'])
                project.save()

   
    def handle(self, *args, **options):
        initial = options['initial']
        with client.Session(settings.INSIGHTLY_API_KEY) as session:
            #self.sync_pipelines(session)
            #self.stdout.write(self.style.SUCCESS('Pipelines synced up...'))            
            self.sync_stages(session)
            self.stdout.write(self.style.SUCCESS('Stages synced up...'))
            #self.sync_categories(session)
            #self.stdout.write(self.style.SUCCESS('Categories synced up...'))
            #self.sync_users(session)
            #self.stdout.write(self.style.SUCCESS('Users synced up...'))
            self.sync_projects(session)
            self.stdout.write(self.style.SUCCESS('Projects synced up...'))
        self.stdout.write(self.style.SUCCESS('Done!'))

 
