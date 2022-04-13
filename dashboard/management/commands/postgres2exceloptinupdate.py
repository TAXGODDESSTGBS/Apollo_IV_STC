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
from insightly.models import Projectoptinupdate
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1JBJ8mJbk8lLdJTfbl0ftfBYtIpUVV7MNidAX_LWv7Sc'
SAMPLE_RANGE_NAME = 'A1:AA10000'
HEADERS = (
    'Project ID', 'Project Name','START','OPT-IN Update Proc - 0001 - Create OPT-IN update letter','OPT-IN Update Proc - 0002 - Send OPT-IN update letter','OPT-IN Update Proc - 0003 - Update Processing','END','START','OPT-IN Update Proc - 0001 - Create OPT-IN update letter','OPT-IN Update Proc - 0002 - Send OPT-IN update letter','OPT-IN Update Proc - 0003 - Update Processing','END','Total Number of Days for all Stages','Total Number of P4 Days', 'Turn Around Time')

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

            project_data = list(Projectoptinupdate.objects.values_list('projectoptinupdate_id', 'name','startDays','OPTINUpdateProc0001CreateOPTINupdateletterdays','OPTINUpdateProc0002SendOPTINupdateletterdays','OPTINUpdateProc0003UpdateProcessingdays','enddays','startP4','OPTINUpdateProc0001CreateOPTINupdateletterP4','OPTINUpdateProc0002SendOPTINupdateletterP4','OPTINUpdateProc0003UpdateProcessingP4','endP4','TotalDaysPerStage', 'TotalP4DaysPerStage', 'TurnAroundTime'))
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





            

            
