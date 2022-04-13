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
from insightly.models import Project
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1XhFBrWLlEzohqZUJRb605-b1jF5iD0-sE7W9bNLxlN0'
SAMPLE_RANGE_NAME = 'A1:AB10000'
HEADERS = (
    'Project ID', 'Project Name','Start - Days in P4','Billable dmt project 0001 setup client tasks - Days in P4','Billable dmt project 0002 create ideas for client - Days in P4','Billable dmt project 0003 Input Prep Billable Input Prep - Days in P4','Billable dmt project 00031 qa with the client - Days in P4','Billable dmt project 1st review - Days in P4','Billable dmt project clrrvwpts - Days in P4','Billable dmt project 0004 final review - Days in P4','Billable dmt project 0005 assemble ctc plan - Days in P4','Billable dmt project 0006 admin wrap up - Days in P4','End - Days in P4','Start Days','Billable dmt project 0001 setup client tasks days','Billable dmt project 0002 create ideas for client days','Billable dmt project 0003 input prep Billable Input Prep Days','Billable dmt project 00031 qa with the client Days','Billable dmt project 1st review Days','Billable dmt project clrrvwpts Days','Billable dmt project 0004 final review Days','Billable dmt project 0005 assemble ctc plan Days','Billable dmt project 0006 admin wrapup Days','End Days', 'TotalP4DaysPerStage', 'TotalDaysPerStage')

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

            project_data = list(Project.objects.values_list('project_id', 'name', 'startP4','billabledmtproject0001setupclienttasksP4','billabledmtproject0002createideasforclientP4','billabledmtproject0003inputprepbillableinputprepP4','billabledmtproject00031qawiththeclientP4','billabledmtproject1streviewP4','billabledmtprojectclrrvwptsP4','billabledmtproject0004finalreviewP4','billabledmtproject0005assemblectcplanP4','billabledmtproject0006adminwrapupP4','endP4','startDays','billabledmtproject0001setupclienttasksdays','billabledmtproject0002createideasforclientdays','billabledmtproject0003inputprepbillableinputprepdays','billabledmtproject00031qawiththeclientdays','billabledmtproject1streviewdays','billabledmtprojectclrrvwptsdays','billabledmtproject0004finalreviewdays','billabledmtproject0005assemblectcplandays','billabledmtproject0006adminwrapupdays','enddays', 'TotalP4DaysPerStage', 'TotalDaysPerStage'))
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



