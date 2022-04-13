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
    'Project ID', 'Project Name','Proformad - 1040 - 0001 - Days in P4','Intakes - 1040 - 0002 - Days in P4','Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1040 - 0003 - Days in P4','Final Review of BK WPS - 1040 - 0004 - Days in P4','Clear Review Points for Bk - 1040 - 0005 - Days in P4','Input/Prep - 1040 - 0006 - Days in P4','Waiting on k-1 - 1040 - 0007 - Days in P4','Review - 1040 - 0008 - Days in P4','Clear Review Points - TR - 1040 - 0009 - Days in P4','Finalize 1st Review - 1040 - 0010 - Days in P4','Final Review - 1040 - 0011 - Days in P4','Partner Signoff - 1040 - 0012 - Days in P4','Bill/Print (TRs) & Assembly - 1040 - 0013 - Days in P4','Waiting for Client Signature - 1040 - 0014 - Days in P4','Close Out Tax Return - 1040 - 0015 - Days in P4','Fee Analysis - 1040 - 0018 - Days in P4','Rollover Process - 1040 - 0019 - Days in P4','Days in - Proformad - 1040 - 0001','Days in - Intakes - 1040 - 0002','Days in - Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1040 - 0003','Days in - Final Review of BK WPS - 1040 - 0004','Days in - Clear Review Points for Bk - 1040 - 0005','Days in - Input/Prep - 1040 - 0006','Days in - Waiting on k-1 - 1040 - 0007','Days in - Review - 1040 - 0008','Days in - Clear Review Points - TR - 1040 - 0009','Days in - Finalize 1st Review - 1040 - 0010','Days in - Final Review - 1040 - 0011','Days in - Partner Signoff - 1040 - 0012','Days in - Bill/Print (TRs) & Assembly - 1040 - 0013','Days in - Waiting for Client Signature - 1040 - 0014','Days in - Close Out Tax Return - 1040 - 0015','Days in - Fee Analysis - 1040 - 0018','Days in - Rollover Process - 1040 - 0019',' Total P4 Days Per Stage', 'Total Days Per Stage', 'Turn Around Time')



                           
            else: 
                print("Project not in filtered stages")  



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

            project_data = list(Project.objects.values_list('project_id', 'name', 'Proformad10400001P4','Intakes10400002P4','BKKPNGRevTRPrintRevPreCompileP4','FinalReviewofBKWPS10400004P4','project.ClearReviewPointsforBk10400005P4','InputPrep10400006P4','Waitingonk110400007P4','Review10400008P4','ClearReviewPointsTR10400009P4','Finalize1stReview10400010P4','FinalReview10400011P4','PartnerSignoff10400012P4','.BillPrintTRsAssembly10400013P4','WaitingforClientSignature10400014P4','CloseOutTaxReturn10400015P4','FeeAnalysis10400018P4','RolloverProcess10400019P4','Proformad10400001','Intakes10400002','BKKPNGRevTRPrintRevPreCompile','FinalReviewofBKWPS10400004','ClearReviewPointsforBk10400005'.'InputPrep10400006','Waitingonk110400007','Review10400008','ClearReviewPointsTR10400009','Finalize1stReview10400010','FinalReview10400011','PartnerSignoff10400012','BillPrintTRsAssembly10400013','WaitingforClientSignature10400014','CloseOutTaxReturn10400015','FeeAnalysis10400018','RolloverProcess10400019', ' TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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