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
from insightly.models import Projectctcstcproject
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1s8VUiBN_Ul-HrruVke9GjtO1x0JntqJwYmwRYum0W6I'
SAMPLE_RANGE_NAME = 'A1:AD10000'
HEADERS = (
    'Project ID','Project Name','Proformad - STC/CTC - 0001  - Days in P4','Intakes - STC/CTC - 0002 - Days in P4','Create Ideas for Client - STC/CTC - 0003 - Days in P4','Input/Prep - STC/CTC - 0004 - Days in P4','Review Project - STC/CTC - 0006 - Days in P4','Clear Review Points - STC/CTC - 0007 - Days in P4','Final Review - STC/CTC - 0008 - Days in P4','Assemble - STC/CTC - 0009 - Days in P4', 'Wrap-up - STC/CTC - 0010 - Days in P4','CS FUP - ALL - STC/CTC - 0011 - Days in P4','Sales FUP - ALL - STC/CTC - 0012 - Days in P4','Rollover - STC/CTC - 0013 - Days in P4','Q&A with Client - STC/CTC - 0005 - Days in P4 ', 'Proformad - STC/CTC - 0001 Days','Intakes - STC/CTC - 0002 days','Create Ideas for Client - STC/CTC - 0003','Input/Prep - STC/CTC - 0004 Days','Review Project - STC/CTC - 0006 Days','Clear Review Points - STC/CTC - 0007 Days','Final Review - STC/CTC - 0008 - Days','Assemble - STC/CTC - 0009 - Days','Wrap-up - STC/CTC - 0010 - Days','CS FUP - ALL - STC/CTC - 0011 - Days','Sales FUP - ALL - STC/CTC - 0012 Days','Rollover - STC/CTC - 0013 - Days','Q&A with Client - STC/CTC - 0005 - Days','TotalDaysPerStage','TotalP4DaysPerStage')

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

            project_data = list(Projectctcstcproject.objects.values_list('projectctcstcproject_id', 'name', 'ProformadSTCCTC0001P4', 'IntakesSTCCTC0002P4', 'CreateIdeasforClientSTCCTC0003P4', 'InputPrepSTCCTC0004P4', 'ReviewProjectSTCCTC0006P4', 'ClearReviewPointsSTCCTC0007P4', 'FinalReviewSTCCTC0008P4', 'AssembleSTCCTC0009P4', 'WrapupSTCCTC0010P4', 'CSFUPALLSTCCTC0011P4', 'SalesFUPALLSTCCTC0012P4', 'RolloverSTCCTC0013P4','QAwithClientSTCCTC0005P4', 'ProformadSTCCTC0001', 'IntakesSTCCTC0002', 'CreateIdeasforClientSTCCTC0003', 'InputPrepSTCCTC0004', 'ReviewProjectSTCCTC0006', 'ClearReviewPointsSTCCTC0007', 'FinalReviewSTCCTC0008', 'AssembleSTCCTC0009', 'WrapupSTCCTC0010', 'CSFUPALLSTCCTC0011', 'SalesFUPALLSTCCTC0012', 'RolloverSTCCTC0013','QAwithClientSTCCTC0005', 'TotalDaysPerStage', 'TotalP4DaysPerStage'))
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




