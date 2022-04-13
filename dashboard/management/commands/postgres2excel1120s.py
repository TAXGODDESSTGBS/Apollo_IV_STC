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
from insightly.models import Project1120S
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '10qfuN-8S3K6qXsiD-4RGuNCvu-MgEtlXYGaVvD5MJ9o'
SAMPLE_RANGE_NAME = 'A1:AM10000'
HEADERS = (
    'Project ID', 'Project Name','Proformad - 1120s - 0001 - Days in P4','Intakes - 1120s - 0002 - Days in P4','Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1120s - 0003 - Days in P4','Final Review of BK WPS - 1120s - 0004 - Days in P4','Clear Review Points for Bk - 1120s - 0005 - Days in P4','Input/Prep - 1120s - 0006 - Days in P4','Waiting on k-1 - 1120s - 0007 - Days in P4','Review - 1120s - 0008 - Days in P4','Clear Review Points - 1120s - 0009 - Days in P4','Finalize 1st Review - 1120s - 0010 - Days in P4','Final Review - 1120s - 0011 - Days in P4','Partner Signoff - 1120s - 0012 - Days in P4','Bill/Print & Assembly - 1120s - 0013 - Days in P4','Waiting for Client Signature - 1120s - 0014 - Days in P4','Close Out Tax Return - 1120s - 0015 - Days in P4','Fee Analysis - 1120s - 0016 - Days in P4','Rollover Process - 1120s - 0017 - Days in P4','Days in - Proformad - 1120s - 0001','Days in - Intakes - 1120s - 0002','Days in - Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1120s - 0003 - Days in P4','Days in - Final Review of BK WPS - 1120s - 0004','Days in - Clear Review Points for Bk - 1120s - 0005','Days in - Input/Prep - 1120s - 0006','Days in - Waiting on k-1 - 1120s - 0007','Days in - Review - 1120s - 0008','Days in - Clear Review Points - 1120s - 0009','Days in - Finalize 1st Review - 1120s - 0010','Days in - Final Review - 1120s - 0011','Days in - Partner Signoff - 1120s - 0012','Days in - Bill/Print & Assembly - 1120s','Days in - Waiting for Client Signature - 1120s - 0014','Days in - Close Out Tax Return - 1120s - 0015','Days in - Fee Analysis - 1120s - 0016','Days in - Rollover Process - 1120s - 0017','Total P4 Days Per Stage','Total Days Per Stage','Turn Around Time')

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
            project_data = list(Project1120S.objects.values_list('project1120s_id', 'name', 'Proformad1120s0001P4','Intakes1120s0002P4','BKKPNGRevTRPrintRevPreComp3P4','FinalReviewofBKWPS1120s0004P4','ClearReviewPointsforBk1120s0005P4','InputPrep1120s0006P4','Waitingonk11120s0007P4','Review1120s0008P4','ClearReviewPoints1120s0009P4','Finalize1stReview1120s0010P4','FinalReview1120s0011P4','PartnerSignoff1120s0012P4','BillPrintAssembly1120s0013P4','WaitingforClientSignature1120s0014P4','CloseOutTaxReturn1120s0015P4','FeeAnalysis1120s0016P4','RolloverProcess1120s0017P4','Proformad1120s0001','Intakes1120s0002','BKKPNGRevTRPrintRevPreComp3','FinalReviewofBKWPS1120s0004','ClearReviewPointsforBk1120s0005','InputPrep1120s0006','Waitingonk11120s0007','Review1120s0008','ClearReviewPoints1120s0009','Finalize1stReview1120s0010','FinalReview1120s0011','PartnerSignoff1120s0012','BillPrintAssembly1120s0013','WaitingforClientSignature1120s0014','CloseOutTaxReturn1120s0015','FeeAnalysis1120s0016','RolloverProcess1120s0017','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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