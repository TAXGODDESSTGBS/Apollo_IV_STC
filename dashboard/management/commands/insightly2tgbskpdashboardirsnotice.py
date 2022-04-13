from datetime import datetime
from datetime import timezone
#import datetime

from django.conf import settings
from django.core.exceptions import ObjectDoesNotExist
from django.core.management.base import BaseCommand, CommandError
from django.contrib.postgres.search import SearchQuery, SearchRank, SearchVector

from insightly.api import client
from insightly.models import Projectirsnotice, Stageirsnotice
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
#            pipeline = self.get_obj(Pipelineirsnotice, p['PIPELINE_ID'])
#            if pipeline.name != p['PIPELINE_NAME']:
#                pipeline.name = p['PIPELINE_NAME']
#                pipeline.save()

    def sync_stages(self, session):
        stages = session.get_pipeline_stages()  
        for s in stages:
            stage = self.get_obj(Stageirsnotice, s['STAGE_ID'])
            if stage.name != s['STAGE_NAME']:
                stage.name = s['STAGE_NAME']
              #  pipeline = self.get_obj(Pipelineirsnotice, s['PIPELINE_ID'])
               # pipeline.save()
               # stage.pipeline = pipeline
                stage.save()

 #   def sync_categories(self, session):
 #       categories = session.get_project_categories()
 #       for c in categories:
 #           category = self.get_obj(Categoryirsnotice, c['CATEGORY_ID'])
 #           if category.name != c['CATEGORY_NAME']:
  #              category.name = c['CATEGORY_NAME']
 #               category.save() 

#    def sync_users(self, session):
#        users = session.get_users()   
#        for u in users:
#            user = self.get_obj(UserModelirsnotice, u['USER_ID']) 
#            if user.name != u['FIRST_NAME']:
#                user.name = u['FIRST_NAME']
#                user.save()        
    
    # function that filters vowels 
#    def fun(variable): 
#        letters = ['a', 'e', 'i', 'o', 'u'] 
#        if (variable in letters): 
#            return True
#        else: 
#            return False
  
  
    # sequence 
#    sequence = ['g', 'e', 'e', 'j', 'k', 's', 'p', 'r'] 
  
    # using filter function 
#    filtered = filter(fun, sequence) 
  
#    print('The filtered letters are:') 
#    for s in filtered: 
#        print(s) 

    def sync_projects(self, session):
        #sessions = Session.objects.filter(expire_date__gte=datetime.now())
        projects = session.get_projects()      
        for p in projects:
            project = self.get_obj(Projectirsnotice, p['PROJECT_ID'])
            if project.name != p['PROJECT_NAME']:
                project.name = p['PROJECT_NAME']          
            project.woi = p['TAGS'].__contains__({'TAG_NAME':'P4'}) 
            #project.pipeline = self.get_obj(Pipelineirsnotice, p['PIPELINE_ID'])
            project.project_status = p['STATUS'] 
            project.starteddate = p['DATE_CREATED_UTC']
            #project.user_responsible = self.get_obj(UserModelirsnotice, p['RESPONSIBLE_USER_ID'])
            #project.category = self.get_obj(Categoryirsnotice, p['CATEGORY_ID'])
            project.projectstatuscancelled = p['STATUS'] == 'CANCELLED'
            project.projectstatuscompleted = p['STATUS'] == 'COMPLETED'   
            project.projectstatusinprogress = p['STATUS'] == 'IN PROGRESS'
            #project.stage = self.get_obj(Stageirsnotice, p['STAGE_ID'])
             
            if project.woi and project.stage_id == (2718328):
                project.startP4 +=1   
            elif project.woi and project.stage_id == (2718329):
                project.irsnotice0001intakesforirsnoticeadminP4 +=1    
            elif project.woi and project.stage_id == (2718331):
                project.irsnotice00021streviewCPAleveltaxteammemberP4  +=1
            elif project.woi and project.stage_id == (2718332):
                project.irsnotice0003clearreviewpointsP4 +=1
            elif project.woi and project.stage_id == (3678053):
                project.irsnotice00032ndreviewmanagerleveldeptheadP4 +=1
            elif project.woi and project.stage_id == (3514023):
                project.irsnotice0004mailingphysicalazadminP4 +=1    
            elif project.woi and project.stage_id == (3514024):
                project.irsnotice0005followupmanagerleveldeptheadP4 +=1
            elif project.woi and project.stage_id == (2718333):
                project.irsnotice0006followupadminP4 +=1
            elif project.woi and project.stage_id == (2718334):
                project.irsnotice0007followupCPAP4 +=1
            elif project.woi and project.stage_id == (2718335):
                project.irsnotice0008closeoutnoticeAdminP4 +=1
            elif project.woi and project.stage_id == (2718336):
                project.endP4 +=1
              
            else: 
                    print("Project not in filtered stages") 

            if not project.woi and project.stage_id == (1865807):
                project.startDays +=1   
            elif not project.woi and project.stage_id == (1775280):
                project.irsnotice0001intakesforirsnoticeadmindays +=1 
            elif not project.woi and project.stage_id == (1775281):
                project.irsnotice00021streviewCPAleveltaxteammemberdays +=1
            elif not project.woi and project.stage_id == (3397465):
                project.irsnotice0003clearreviewpointsdays +=1
            elif not project.woi and project.stage_id == (1775282):
                project.irsnotice00032ndreviewmanagerleveldeptheaddays +=1              
            elif not project.woi and project.stage_id == (1775283):
                project.irsnotice0004mailingphysicalazadmindays +=1
            elif not project.woi and project.stage_id == (1775284):
                project.irsnotice0005followupmanagerleveldeptheaddays +=1
            elif not project.woi and project.stage_id == (2887514):
                project.irsnotice0006followupadmindays +=1
            elif not project.woi and project.stage_id == (2887524):
                project.irsnotice0007followupCPAdays +=1
            elif not project.woi and project.stage_id == (1775285):
                project.irsnotice0008closeoutnoticeAdmindays +=1
            elif not project.woi and project.stage_id == (1865808):
                project.enddays +=1
            else:  
                print("Project not in filtered stages")


            project.TotalP4DaysPerStage = project.startP4 + project.irsnotice0001intakesforirsnoticeadminP4 + project.irsnotice00021streviewCPAleveltaxteammemberP4 + project.irsnotice0003clearreviewpointsP4 + project.irsnotice00032ndreviewmanagerleveldeptheadP4 + project.irsnotice0004mailingphysicalazadminP4 + project.irsnotice0005followupmanagerleveldeptheadP4 + project.irsnotice0006followupadminP4 + project.irsnotice0007followupCPAP4 + project.irsnotice0008closeoutnoticeAdminP4 + project.endP4 
            project.TotalDaysPerStage = project.startDays + project.irsnotice0001intakesforirsnoticeadmindays + project.irsnotice00021streviewCPAleveltaxteammemberdays + project.irsnotice0003clearreviewpointsdays + project.irsnotice00032ndreviewmanagerleveldeptheaddays + project.irsnotice0004mailingphysicalazadmindays + project.irsnotice0005followupmanagerleveldeptheaddays + project.irsnotice0006followupadmindays + project.irsnotice0007followupCPAdays + project.irsnotice0008closeoutnoticeAdmindays + project.enddays 
            #project.TurnAroundTime = project.TotalDaysPerStage - project.TotalP4DaysPerStage 
            
            if p['PROJECT_NAME'].__contains__('IRS Notice') and p['STATUS'] == 'IN PROGRESS' or p['PROJECT_NAME'].__contains__('IRS Notice') and p['STATUS'] == 'DEFERRED': 
                project.stage = self.get_obj(Stageirsnotice, p['STAGE_ID'])
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

 


