from __future__ import print_function
from django.core.management.base import BaseCommand
import pickle
import os
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from django.conf import settings
import json
from datetime import datetime
from pprint import pprint
from insightly.models import Projectbookkeepingspecialprojects
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1BYBrzaQh2Wsw0pIKf27XbjybnCk4JSNvy4R1QRzCnXg'
SAMPLE_RANGE_NAME = 'A1:AA10000'
HEADERS = (
    'Project ID', 'Project Name','Start - Days in P4', 'Bookkeeping Special 0001 Input Prep - Days in P4', 'Bookkeeping Special 0002 Review - Days in P4', 'Bookkeeping 0003 Clear Review Points - Days in P4', 'Bookkeeping Special 0003 Final Review - Days in P4', 'End - Days in P4', 'user_responsible_id', 'Start Days', 'Bookkeeping Special 0001 Input Prep Days', 'Bookkeeping Special 0002 Review Days', 'Bookkeeping Special 0003 Clear Review Points - Days', 'Bookkeeping Special 0003 Final Review Days', 'End - Days' 'TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime' )

def get_credentials():
    creds = None
    if os.path.exists(os.path.join(settings.BASE_DIR, 'token.pickle')):
        with open('token.pickle', 'rb') as token:
            creds = pickle.load(token)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                os.path.join(settings.BASE_DIR, 'credentials.json'), SCOPES)
            creds = flow.run_local_server(port=0)
        with open(os.path.join(settings.BASE_DIR, 'token.pickle'), 'wb') as token:
            pickle.dump(creds, token)

    return creds



class Command(BaseCommand):

    def handle(self, *args, **options):

        try:            
            credentials = get_credentials()
            service = build('sheets', 'v4', credentials=credentials)

            project_data = list(Projectbookkeepingspecialprojects.objects.values_list('projectbookkeepingspecialprojects_id', 'name','startP4','bkpspecial0001inputprepP4','bkpspecial0002reviewP4','bkpspecial0003clearreviewpointsP4','bkpspecial0003finalreviewP4','endP4','user_responsible_id','startdays','bkpspecial0001inputprepdays','bkpspecial0002reviewdays','bkpspecial0003clearreviewpointsdays','bkpspecial0003finalreviewdays','enddays','TotalP4DaysPerStage', 'TotalDaysPerStage','TurnAroundTime' ))
            #if not Project.ProjProfileFilter:
            project_data.insert(0, HEADERS)
            sheet = service.spreadsheets()
            sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
                                 range=SAMPLE_RANGE_NAME).execute()
            response_date = sheet.values().update(
                spreadsheetId=SAMPLE_SPREADSHEET_ID,
                valueInputOption='RAW',
                range=SAMPLE_RANGE_NAME,
                body=dict(
                    majorDimension='ROWS',
                    values=project_data)
            ).execute()
            print('Sheet successfully Updated', response_date)
          
        except Exception as e:
            import traceback
            traceback.print_exc()
            print(e)



      
           



           

