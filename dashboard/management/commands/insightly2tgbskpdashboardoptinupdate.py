from datetime import datetime
from datetime import timezone
#import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Categoryoptinupdate, Projectoptinupdate, Stageoptinupdate, UserModeloptinupdate, Pipelineoptinupdate
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
        
            
    #def sync_pipelines(self, session):
    #    pipelines = session.get_pipelines()
    #    for p in pipelines:
    #        pipeline = self.get_obj(Pipelineoptinupdate, p['PIPELINE_ID'])
    #        if pipeline.name != p['PIPELINE_NAME']:
    #            pipeline.name = p['PIPELINE_NAME']
    #            pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stageoptinupdate, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
                stage.save()

    def sync_categories(self, session):
        categories = session.get_project_categories()
        for c in categories:
            category = self.get_obj(Categoryoptinupdate, c['CATEGORY_ID'])
            if category.name != c['CATEGORY_NAME']:
                category.name = c['CATEGORY_NAME']
                category.save() 

    def sync_users(self, session):
        users = session.get_users()   
        for u in users:
            user = self.get_obj(UserModeloptinupdate, u['USER_ID']) 
            if user.name != u['FIRST_NAME']:
                user.name = u['FIRST_NAME']
                user.save()        
    

    def sync_projects(self, session):
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Projectoptinupdate, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME'] 
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'})             
            project.project_status = p['STATUS'] 
            project.datecreated = p['DATE_CREATED_UTC']
            project.user_responsible = self.get_obj(UserModeloptinupdate, p['RESPONSIBLE_USER_ID'])
            project.category = self.get_obj(Categoryoptinupdate, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'        
            project.stage = self.get_obj(Stageoptinupdate, p['STAGE_ID'])

            
            if project.woi and project.stage_id == (1865813):
                project.startDays +=1   
            elif project.woi and project.stage_id == (1774790):
                project.OPTINUpdateProc0001CreateOPTINupdateletterdays +=1 
            elif project.woi and project.stage_id == (1774801):
                project.OPTINUpdateProc0002SendOPTINupdateletterdays +=1
            elif project.woi and project.stage_id == (1774802):
                project.OPTINUpdateProc0003UpdateProcessingdays +=1      
            elif project.woi and project.stage_id == (1865814):
                project.enddays +=1
            else:  
                print("Project not in filtered stages")

            if not project.woi and project.stage_id == (1865813):
                project.startP4 +=1   
            elif not project.woi and project.stage_id == (1774790):
                project.OPTINUpdateProc0001CreateOPTINupdateletterP4 +=1   
            elif not project.woi and project.stage_id == (1774801):
                project.OPTINUpdateProc0002SendOPTINupdateletterP4  +=1
            elif not project.woi and project.stage_id == (1774802):
                project.OPTINUpdateProc0003UpdateProcessingP4 +=1      
            elif not project.woi and project.stage_id == (1865814):
                project.endP4 +=1
            else:  
                print("Project not in filtered stages")

            project.TotalP4DaysPerStage = project.startP4 + project.OPTINUpdateProc0001CreateOPTINupdateletterP4 + project.OPTINUpdateProc0002SendOPTINupdateletterP4 + project.OPTINUpdateProc0003UpdateProcessingP4 + project.endP4 
            project.TotalDaysPerStage =  project.startDays + project.OPTINUpdateProc0001CreateOPTINupdateletterdays + project.OPTINUpdateProc0002SendOPTINupdateletterdays + project.OPTINUpdateProc0003UpdateProcessingdays + project.enddays 
            project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage
            if p['PROJECT_NAME'].__contains__('OPT-IN Update') and p['STATUS'] == 'IN PROGRESS':
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

 

