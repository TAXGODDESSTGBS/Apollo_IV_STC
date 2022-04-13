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
from insightly.models import Project1120SX
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1hXCTBFUR-ST1f9MxJBOAU42qtCC5tAWYPMpePvPWgqs'
SAMPLE_RANGE_NAME = 'A1:AK10000'
HEADERS = (
    'Project ID', 'Project Name','START - Days in P4','1120SX - 0001 - Intake Process - Days in P4','1120SX - 0002 - Print PBC Financial Statements for BK TR RVW - Days in P4','1120SX - 0003 - Bookkeeping Review - TR - Days in P4','1120SX - 0004 - Final Review of BK WPS - Days in P4','1120SX - 0005 - Clear Review Points for BK - Days in P4','1120SX - 0006 - Input/Prep - Days in P4','1120SX - 0007 - Review - Days in P4','1120SX - 0008 - Clear Review Points For TR - Days in P4','1120SX - 0009 - Final Review - Days in P4','1120SX - 0010 - Partner Signoff - Days in P4','1120SX - 0011 - Bill/Print (TRs) - Days in P4','1120SX - 0012 - Assemble - Days in P4','1120SX - 0013 - Waiting for Signature - Days in P4','1120SX - 0014 - Close Out Tax Return - Days in P4','1120SX - 0014 - END - Days in P4','Days in - START','Days in - 1120SX - 0001 - Intake Process','Days in - 1120SX - 0002 - Print PBC Financial Statements for BK TR RVW','Days in - 1120SX - 0003 - Bookkeeping Review - TR','Days in - 1120SX - 0004 - Final Review of BK WPS','Days in - 1120SX - 0005 - Clear Review Points for BK','Days in - 1120SX - 0006 - Input/Prep','Days in - 1120SX - 0007 - Review','Days in - 1120SX - 0008 - Clear Review Points For TR','Days in - 1120SX - 0009 - Final Review','Days in - 1120SX - 0010 - Partner Signoff','Days in - 1120SX - 0011 - Bill/Print (TRs)','Days in - 1120SX - 0012 - Assemble','Days in - 1120SX - 0013 - Waiting for Signature','Days in - 1120SX - 0014 - Close Out Tax Return','Days in - 1120SX - 0014 - END','Total P4 Days Per Stage','Total Days Per Stage','Turn Around Time')

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

            project_data = list(Project1120SX.objects.values_list('project1120sx_id', 'name', 'STARTP4','sx1120SX0001IntakeProcessP4','sx1120SX0002PrintPBCFinancialStatementsforBKTRRVWP4','sx1120SX0003BookkeepingReviewTRP4','sx1120SX0004FinalReviewofBKWPSP4','sx1120SX0005ClearReviewPointsforBKP4','sx1120SX0006InputPrepP4','sx1120SX0007ReviewP4','sx1120SX0008ClearReviewPointsForTRP4','sx1120SX0009FinalReviewP4','sx1120SX0010PartnerSignoffP4','sx1120SX0011BillPrintTRsP4','sx1120SX0012AssembleP4','sx120SX0013WaitingforSignatureP4','sx1120SX0014CloseOutTaxReturnP4','sx1120SX0014ENDP4','START','sx1120SX0001IntakeProcess','sx1120SX0002PrintPBCFinancialStatementsforBKTRRVW','sx1120SX0003BookkeepingReviewTR','sx1120SX0004FinalReviewofBKWPS','sx1120SX0005ClearReviewPointsforBK','sx1120SX0006InputPrep','sx1120SX0007Review','sx1120SX0008ClearReviewPointsForTR','sx1120SX0009FinalReview','sx1120SX0010PartnerSignoff','sx1120SX0011BillPrintTRs','sx1120SX0012AssembleP4','sx120SX0013WaitingforSignature','sx1120SX0014CloseOutTaxReturn','sx1120SX0014END','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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