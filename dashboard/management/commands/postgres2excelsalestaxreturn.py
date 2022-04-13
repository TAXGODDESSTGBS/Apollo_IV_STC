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
from insightly.models import Projectsalestaxreturn
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1mk4_WVIOxxUqtJje-QNVvnAXKd6OtyJ8jOVTcwlSZP4'
SAMPLE_RANGE_NAME = 'A1:Z10000'
HEADERS = (
    'Project ID', 'Project Name',"Proforma'd - Sales Tax - 0001 - Days in P4",'Input/Prep - Sales Tax - 0002 - Days in P4','Review Process - Sales Tax - 0003 - Days in P4','Rollover Process - Sales Tax - 0004 - Days in P4',"Days in - Proforma'd - Sales Tax - 0001",'Days in - Input/Prep - Sales Tax - 0002','Days in - Review Process - Sales Tax - 0003','Days in - Rollover Process - Sales Tax - 0004','Total Number of Days for all Stages','Total Number of P4 Days')

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

            project_data = list(Projectsalestaxreturn.objects.values_list('projectsalestaxreturn_id', 'name','ProformadSalesTax0001Days','InputPrepSalesTax0002days','ReviewProcessSalesTax0003days','RolloveProcessSaleTax0004days','ProformadSalesTax0001P4','InputPrepSalesTax0002P4','ReviewProcessSalesTax0003P4','RolloveProcessSaleTax0004P4', 'TotalP4DaysPerStage', 'TotalDaysPerStage'))
                                                       
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





           

        
