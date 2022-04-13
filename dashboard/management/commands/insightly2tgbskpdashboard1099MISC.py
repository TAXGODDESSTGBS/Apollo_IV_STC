from datetime import datetime
from datetime import timezone

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Project1099misc, Stage1099misc
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
        

#    def sync_pipelines(self, session):
#        pipelines = session.get_pipelines()
#        for p in pipelines:
#            pipeline = self.get_obj(Pipeline1099misc, p['PIPELINE_ID'])
#            if pipeline.name != p['PIPELINE_NAME']:
#                pipeline.name = p['PIPELINE_NAME']
#                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stage1099misc, s['STAGE_ID'])
           #stage = self.get_obj(Stage13WCF, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                #pipeline = self.get_obj(Pipeline13WCF, s['PIPELINE_ID'])
                #pipeline.save()
                #stage.pipeline = pipeline
                stage.save()

 #   def sync_categories(self, session):
 #       categories = session.get_project_categories()
 #       for c in categories:
 #           category = self.get_obj(Category1099misc, c['CATEGORY_ID'])
 #           if category.name != c['CATEGORY_NAME']:
 #               category.name = c['CATEGORY_NAME']
  #              category.save() 

#    def sync_users(self, session):
#        users = session.get_users()   
#        for u in users:
#            user = self.get_obj(UserModel1099misc, u['USER_ID']) 
#            if user.name != u['FIRST_NAME']:
#                user.name = u['FIRST_NAME']
#                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Project1099misc, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipeline1099misc, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.starteddate = p['DATE_CREATED_UTC']
           # project.user_responsible = self.get_obj(UserModel1099misc, p['RESPONSIBLE_USER_ID'])
           # project.category = self.get_obj(Category1099misc, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            #project.stage = self.get_obj(Stage1099misc, p['STAGE_ID'])               						

            if project.woi and project.stage_id == (1774757):
                project.ProformadIntakes1099Prep0001P4 +=1   
            elif project.woi and project.stage_id == (3221830):
                project.GatherData1099Prep0002P4 +=1 
            elif project.woi and project.stage_id == (3221831):
                project.Review1099Prep0003P4 +=1            
            elif project.woi and project.stage_id == (3221832):
                project.CLRRVWPTS1099Prep0004P4 +=1    
            elif project.woi and project.stage_id == (3221833):
                project.Finalize1stReview1099Prep0005P4 +=1
            elif project.woi and project.stage_id == (3221834):
                project.InputtoSoftware1099Prep0006P4 +=1 
            elif project.woi and project.stage_id == (3221835):
                project.ClientApproval1099Prep0007P4 +=1            
            elif project.woi and project.stage_id == (3221836):
                project.Deliver1099Prep0008P4 +=1    
            elif project.woi and project.stage_id == (3221837):
                project.EFileCloseout1099Prep0009P4 +=1
            elif project.woi and project.stage_id == (3221838):
                project.FeeAnalysis1099Prep0010P4 +=1 
            elif project.woi and project.stage_id == (3221839):
                project.Rollover1099Prep0011P4 +=1            
                           
            else: 
                print("Project not in filtered stages")     

            
            if not project.woi and project.stage_id == (1774757):
                project.ProformadIntakes1099Prep0001 +=1   
            elif not project.woi and project.stage_id == (3221830):
                project.GatherData1099Prep0002 +=1 
            elif not project.woi and project.stage_id == (3221831):
                project.Review1099Prep0003 +=1            
            elif not project.woi and project.stage_id == (3221832):
                project.CLRRVWPTS1099Prep0004 +=1    
            elif not project.woi and project.stage_id == (3221833):
                project.Finalize1stReview1099Prep0005 +=1
            elif not project.woi and project.stage_id == (3221834):
                project.InputtoSoftware1099Prep0006 +=1 
            elif not project.woi and project.stage_id == (3221835):
                project.ClientApproval1099Prep0007 +=1            
            elif not project.woi and project.stage_id == (3221836):
                project.Deliver1099Prep0008 +=1    
            elif not project.woi and project.stage_id == (3221837):
                project.EFileCloseout1099Prep0009 +=1
            elif not project.woi and project.stage_id == (3221838):
                project.FeeAnalysis1099Prep0010 +=1 
            elif not project.woi and project.stage_id == (3221839):
                project.Rollover1099Prep0011 +=1            
                           
            else: 
                print("Project not in filtered stages")  

            project.TotalP4DaysPerStage = project.ProformadIntakes1099Prep0001P4 + project.GatherData1099Prep0002P4 + project.Review1099Prep0003P4 + project.CLRRVWPTS1099Prep0004P4 + project.Finalize1stReview1099Prep0005P4 + project.InputtoSoftware1099Prep0006P4 + project.ClientApproval1099Prep0007P4 + project.Deliver1099Prep0008P4 + project.EFileCloseout1099Prep0009P4 + project.FeeAnalysis1099Prep0010P4 + project.Rollover1099Prep0011P4 
            project.TotalDaysPerStage = project.ProformadIntakes1099Prep0001 + project.GatherData1099Prep0002 + project.Review1099Prep0003 + project.CLRRVWPTS1099Prep0004 + project.Finalize1stReview1099Prep0005 + project.InputtoSoftware1099Prep0006 + project.ClientApproval1099Prep0007 + project.Deliver1099Prep0008 + project.EFileCloseout1099Prep0009 + project.FeeAnalysis1099Prep0010 + project.Rollover1099Prep0011 
            #project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage
            if p['PROJECT_NAME'].__contains__('- 1099') and p['STATUS'] == 'IN PROGRESS' or p['PROJECT_NAME'].__contains__('- 1099') and p['STATUS'] == 'DEFERRED':                 
                project.stage = self.get_obj(Stage1099misc, p['STAGE_ID'])
                project.save()

   
    def handle(self, *args, **options):
        initial = options['initial']
        with client.Session(settings.INSIGHTLY_API_KEY) as session:
            #self.sync_pipelines(session)
            #self.stdout.write(self.style.SUCCESS('Pipelines synced up...'))            
            self.sync_stages(session)
            self.stdout.write(self.style.SUCCESS('Stages synced up...'))
            #self.sync_categories(session)
           # self.stdout.write(self.style.SUCCESS('Categories synced up...'))
            #self.sync_users(session)
            #self.stdout.write(self.style.SUCCESS('Users synced up...'))
            self.sync_projects(session)
            self.stdout.write(self.style.SUCCESS('Projects synced up...'))
        self.stdout.write(self.style.SUCCESS('Done!'))

 
