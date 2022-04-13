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
from insightly.models import Project1099misc
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1A-WteZvfwx8-S0VJ29XcfHknwF99FBYN5tUHN49B6x0'
SAMPLE_RANGE_NAME = 'A1:AA10000'
HEADERS = (
    'Project ID', 'Project Name',"Proforma'd & Intakes - 1099 Prep - 0001 - Days in P4",'Gather Data - 1099 Prep - 0002 - Days in P4','Review - 1099 Prep - 0003 - Days in P4','CLR RVW PTS - 1099 Prep - 0004 - Days in P4','Finalize 1st Review - 1099 Prep - 0005 - Days in P4','Input to Software - 1099 Prep - 0006 - Days in P4','Client Approval - 1099 Prep - 0007 - Days in P4','Deliver - 1099 Prep - 0008 - Days in P4','E-File & Close-out - 1099 Prep - 0009 - Days in P4','Fee Analysis - 1099 Prep - 0010 - Days in P4','Rollover - 1099 Prep - 0011 - Days in P4',"Days in - Proforma'd & Intakes - 1099 Prep - 0001",'Days in - Gather Data - 1099 Prep - 0002','Days in - Review - 1099 Prep - 0003','Days in - CLR RVW PTS - 1099 Prep - 0004','Days in - Finalize 1st Review - 1099 Prep - 0005','Days in - Input to Software - 1099 Prep - 0006','Days in - Client Approval - 1099 Prep - 0007','Days in - Deliver - 1099 Prep - 0008','Days in - E-File & Close-out - 1099 Prep - 0009','Days in - Fee Analysis - 1099 Prep - 0010','Days in - Rollover - 1099 Prep - 0011','Total P4 Days Per Stage','Total Days Per Stage')

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

            project_data = list(Project1099misc.objects.values_list('project1099misc_id', 'name', 'ProformadIntakes1099Prep0001P4','GatherData1099Prep0002P4','Review1099Prep0003P4','CLRRVWPTS1099Prep0004P4','Finalize1stReview1099Prep0005P4','InputtoSoftware1099Prep0006P4','ClientApproval1099Prep0007P4','Deliver1099Prep0008P4','EFileCloseout1099Prep0009P4','FeeAnalysis1099Prep0010P4','Rollover1099Prep0011P4','ProformadIntakes1099Prep0001','GatherData1099Prep0002','Review1099Prep0003','CLRRVWPTS1099Prep0004','Finalize1stReview1099Prep0005','InputtoSoftware1099Prep0006','ClientApproval1099Prep0007','Deliver1099Prep0008','EFileCloseout1099Prep0009','FeeAnalysis1099Prep0010','Rollover1099Prep0011','TotalP4DaysPerStage','TotalDaysPerStage', 'TurnAroundTime'))
                        
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
