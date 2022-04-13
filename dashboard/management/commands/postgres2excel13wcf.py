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
from insightly.models import Project13WCF
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1TtaHtl6oG3goFETyyx4sNLeKX1iYb5Ov4gFRQ1iRhCc'
SAMPLE_RANGE_NAME = 'A1:AA10000'
HEADERS = (
    'Project ID', 'Project Name','Proformad 13WCF 0001 - Days in P4','Setup of 13WCF 13WCF 0002 - Days in P4','Ongoing 13 WCF work 13WCF 0003 - Days in P4','user_responsible_id','Proformad 13 WCF 0001 - Days','Setup of 13WCF 13WCF 0002 - Days', 'Ongoing 13WCF work 13WCF 0003 - Days', ' Total P4 Days Per Stage', 'Total Days Per Stage', 'Turn Around Time')

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

#for idx, project_obj in enumerate(Project.objects.all()):                   
#            woi = project_obj.woi
#            stage_name = project_obj.stage    

class Command(BaseCommand):

    def handle(self, *args, **options):
        
        try:            
            credentials = get_credentials()
            service = build('sheets', 'v4', credentials=credentials)

            project_data = list(Project.objects.values_list('project_id', 'name', 'proformad13WCF0001P4',
                                                        'setupof13WCF13WCF0002P4','ongoing13WCFwork13WCF0003P4','user_responsible_id','proformad13WCF0001Days','setupof13WCF13WCF0002days', ' ongoing13WCFwork13WCF0003days', ' TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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