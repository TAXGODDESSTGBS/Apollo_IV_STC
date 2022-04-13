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
from insightly.models import Projectquarterlyestimates
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '19RoCTEZrtbcDMMLPJeZJTAeLe1vRXs5LaGwpQN8Cwng'
SAMPLE_RANGE_NAME = 'A1:AA10000'
HEADERS = (
    'Project ID', 'Project Name','Proformad QTRLY Est 0001 - Number of Days In P4', 'Client Interview QRTLY Est 0002 - Number of Days In P4','Input Prep Qtrly Est 0003 - Number of Days In P4', 'Review Qtrly Est 0004 - Number of Days in P4', 'Clear Review Points Qtrly Est 0005 - Number of Days In P4', 'Final Review Qtrly Est 0006 - Number of Days in P4', 'Deliver Qtrly Est 0007 Days in P4 - Number of Days in P4','Rollover Process Qtrly Est 0008 - Number of Days in P4','User Responsible ID','Proformad QTRLY Est 0001 - Number of Days', 'Client Interview QRTLY Est 0002 - Number of Days','Input Prep Qtrly Est 0003 - Number of Days', 'Review Qtrly Est 0004 - Number of Days', 'Clear Review Points Qtrly Est 0005 - Number of Days', 'Final Review Qtrly Est 0006 - Number of Days', 'Deliver Qtrly Est 0007 Days in P4 - Number of Days','Rollover Process Qtrly Est 0008 - Number of Days','Total Number of Days for all Stages','Total Number of P4 Days', 'Turn Around Time')

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

            project_data = list(Projectquarterlyestimates.objects.values_list('projectquarterlyestimates_id', 'name', 'ProformadQtrlyEst0001P4','ClientInterviewQtrlyEst0002P4','InputPrepQtrlyEst0003P4','ReviewQtrlyEst0004P4','ClearReviewPointsQtrlyEst0005P4','FinalReviewQtrlyEst0006P4','DeliverQtrlyEst0007P4','RolloverProcessQtrlyEst0008P4','user_responsible_id','ProformadQtrlyEst0001Days', 'ClientInterviewQtrlyEst0002days', 'InputPrepQtrlyEst0003days','ReviewQtrlyEst0004days','ClearReviewPointsQtrlyEst0005days','FinalReviewQtrlyEst0006days','DeliverQtrlyEst0007days','RolloverProcessQtrlyEst0008days', 'TotalDaysPerStage', 'TotalP4DaysPerStage', 'TurnAroundTime'))
                                                        
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



