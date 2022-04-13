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
    'Project ID', 'Project Name','Proformad - 1040X - 0001 - Days in P4','Intakes - 1040X - 0002 - Days in P4','Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1040X - 0003 - Days in P4','Final Review of BK WPS - 1040X - 00042 - Days in P4','Clear Review Points for Bk - 1040X - 0005 - Days in P4','Clear Review Points - TR - 1040X - 0009 - Days in P4','Finalize 1st Review - 1040X - 0010 - Days in P4','Final Review - 1040X - 0011 - Days in P4','Partner Signoff - 1040X - 0012 - Days in P4','Bill/Print (TRs) & Assembly - 1040X - 0013 - Days in P4','Waiting for Client Signature - 1040X - 0014 - Days in P4','Close Out Tax Return - 1040X - 0015 - Days in P4','Fee Analysis - 1040X - 0016 - Days in P4','Rollover Process - 1040X - 0017 - Days in P4','Day in - Proformad - 1040X - 0001','Day in - Intakes - 1040X - 0002','Day in - Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1040X - 0003','Day in - Final Review of BK WPS - 1040X - 00042','Day in - Clear Review Points for Bk - 1040X - 0005','Day in - Clear Review Points - TR - 1040X - 0009','Day in - Finalize 1st Review - 1040X - 0010','Day in - Final Review - 1040X - 0011','Day in - Partner Signoff - 1040X - 0012','Day in - Bill/Print (TRs) & Assembly - 1040X - 0013','Day in - Waiting for Client Signature - 1040X - 0014','Day in - Close Out Tax Return - 1040X - 0015','Day in - Fee Analysis - 1040X - 0016','Day in - Rollover Process - 1040X - 0017','Total P4 Days Per Stage', 'Total Days Per Stage', 'Turn Around Time')






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

            project_data = list(Project.objects.values_list('project_id', 'name', 'Proformad1040X0001P4','Intakes1040X0002P4','BKKPNGRFORTRPRINTReviewPreCompile40XP4','FinalReviewofBKWPS1040X0004P4','ClearReviewPointsforBk1040X0005P4','ClearReviewPointsTR1040X0009P4','Finalize1stReview1040X0010P4','FinalReview1040X0011P4','PartnerSignoff1040X0012P4','BillPrintTRsAssembly1040X0013P4','WaitingforClientSignature1040X0014P4','CloseOutTaxReturn1040X0015P4','FeeAnalysis1040X0016P4','RolloverProcess1040X0017P4','Proformad1040X0001','Intakes1040X0002','BKKPNGRFORTRPRINTReviewPreCompile40X','FinalReviewofBKWPS1040X0004','ClearReviewPointsforBk1040X0005','ClearReviewPointsTR1040X0009','Finalize1stReview1040X0010','FinalReview1040X0011','PartnerSignoff1040X0012','BillPrintTRsAssembly1040X0013','WaitingforClientSignature1040X0014','CloseOutTaxReturn1040X0015','FeeAnalysis1040X0016 ','RolloverProcess1040X0017', ' TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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