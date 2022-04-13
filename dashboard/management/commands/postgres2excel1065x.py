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
from insightly.models import Project1065X
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

#Number 35

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1vpqDIqOQjbFLVNg137GMk_HtCEB2a2l7TfiasoXyOHY'
SAMPLE_RANGE_NAME = 'A1:AK10000'
HEADERS = (
    'Project ID','Project Name','START','1065X - 0001 - Intake Process - Days in P4','1065X - 0002 - Print PBC Financial Statements for BK TR RVW - Days in P4','1065X - 0003 - Bookkeeping Review - TR - Days in P4','1065X - 0004 - Final Review of BK WPS - Days in P4','1065X - 0005 - Clear Review Points for BK - Days in P4','1065X - 0006 - Input/Prep - Days in P4','1065X - 0007 - Review - Days in P4','1065X - 0008 - Clear Review Points For TR - Days in P4','1065X - 0009 - Final Review - Days in P4','1065X - 0010 - Partner Signoff - Days in P4','1065X - 0011 - Bill/Print (TRs) - Days in P4','1065X - 0012 - Assemble - Days in P4','1065X - 0013 - Waiting for Signature - Days in P4','1065X - 0014 - Close Out Tax Return - Days in P4','1065X - 0015 - END - Days in P4','Days in - START','Days in - 1065X - 0001 - Intake Process','Days in - 1065X - 0002 - Print PBC Financial Statements for BK TR RVW','Days in - 1065X - 0003 - Bookkeeping Review - TR','Days in - 1065X - 0004 - Final Review of BK WPS','Days in - 1065X - 0005 - Clear Review Points for BK','Days in - 1065X - 0006 - Input/Prep','Days in - 1065X - 0007 - Review','Days in - 1065X - 0008 - Clear Review Points For TR','Days in - 1065X - 0009 - Final Review','Days in - 1065X - 0010 - Partner Signoff','Days in - 1065X - 0011 - Bill/Print (TRs)','Days in - 1065X - 0012 - Assemble','Days in - 1065X - 0013 - Waiting for Signature','Days in - 1065X - 0014 - Close Out Tax Return','Days in - 1065X - 0015 - END','Total P4 Days Per Stage','Total Days Per Stage','Turn Around Time')

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

            project_data = list(Project1065X.objects.values_list('project1065x_id', 'name', 'STARTP4','x1065X0001IntakeProcessP4','x1065X0002PrintPBCFinancialStatementsforBKTRRVWP4','x1065X0003BookkeepingReviewTRP4','x1065X0004FinalReviewofBKWPSP4','x1065X0005ClearReviewPointsforBKP4','x1065X0006InputPrepP4','x1065X0007ReviewP4','x1065X0008ClearReviewPointsForTRP4','x1065X0009FinalReviewP4','x1065X0010PartnerSignoffP4','x1065X0011BillPrintTRsP4','x1065X0012AssembleP4','x1065X0013WaitingforSignatureP4','x1065X0014CloseOutTaxReturnP4','x1065X0015ENDP4','START','x1065X0001IntakeProcess','x1065X0002PrintPBCFinancialStatementsforBKTRRVW','x1065X0003BookkeepingReviewTR','x1065X0004FinalReviewofBKWPS','x1065X0005ClearReviewPointsforBK','x1065X0006InputPrep','x1065X0007Review','x1065X0008ClearReviewPointsForTR','x1065X0009FinalReview','x1065X0010PartnerSignoff','x1065X0011BillPrintTRs','x1065X0012Assemble','x1065X0013WaitingforSignature','x1065X0014CloseOutTaxReturn','x1065X0015END','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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