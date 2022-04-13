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
from insightly.models import Project1041trust
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

#35 NUMBERS

SAMPLE_SPREADSHEET_ID = '1gX_GR24oCC6BXbsrdj3z_KN_3bzWIRHC9wjn2EXJkIU'
SAMPLE_RANGE_NAME = 'A1:AK10000'
HEADERS = (
    'Project ID','Project Name','START - Days in P4','1041 Trust - 0001 - Proforma’d - Days in P4','1041 Trust - 0003 - Bookkeeping Review - TR','1041 Trust - 0004 - Final Review of BK WPS - Days in P4','1041 Trust - 0005 - Clear Review Points for BK - Days in P4','1041 Trust - 0006 - Input/Prep - Days in P4','1041 Trust - 0007 - Review - Days in P4','1041 Trust - 0008 - Clear Review Points For TR - Days in P4','1041 Trust - 0009 - Final Review - Days in P4','1041 Trust - 0010 - Partner Signoff - Days in P4','1041 Trust - 0011 - Bill/Print (TRs) - Days in P4','1041 Trust - 0012 - Assemble - Days in P4','1041 Trust - 0013 - Waiting for Signature - Days in P4','1041 Trust - 0014 - Close Out Tax Return - Days in P4','END - Days in P4','Days in - START','Days in - 1041 Trust - 0001 - Proforma’d','Days in - 1041 Trust - 0002 - Intake Process','Days in - 1041 Trust - 0003 - Bookkeeping Review - TR','Days in - 1041 Trust - 0004 - Final Review of BK WPS','Days in - 1041 Trust - 0005 - Clear Review Points for BK','Days in - 1041 Trust - 0006 - Input/Prep','1041 Trust - 0007 - Review','1041 Trust - 0008 - Clear Review Points For TR','Days in - 1041 Trust - 0009 - Final Review','1041 Trust - 0010 - Partner Signoff','Days in - 1041 Trust - 0011 - Bill/Print (TRs)','1041 Trust - 0012 - Assemble','Days in - 1041 Trust - 0013 - Waiting for Signature','Days in 1041 Trust - 0014 - Close Out Tax Return','Days in - END','Total P4 Days Per Stage','Total Days Per Stage','Turn Around Time')

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

            project_data = list(Project1041trust.objects.values_list('project1041trust_id', 'name', 'STARTP4','trust1041Trust0001ProformadP4','trust1041Trust0002IntakeProcessP4','trust1041Trust0003BookkeepingReviewTRP4','trust1041Trust0004FinalReviewofBKWPSP4','trust1041Trust0005ClearReviewPointsforBKP4','trust1041Trust0006InputPrepP4','trust1041Trust0007ReviewP4','trust1041Trust0008ClearReviewPointsForTRP4','trust1041Trust0009FinalReviewP4','trust1041Trust0010PartnerSignoffP4','trust1041Trust0011BillPrintTRsP4','trust1041Trust0012AssembleP4','trust1041Trust0013WaitingforSignatureP4','trust1041Trust0014CloseOutTaxReturnP4','ENDP4','START','trust1041Trust0001Proformad','trust1041Trust0002IntakeProcess','trust1041Trust0003BookkeepingReviewTR','trust1041Trust0004FinalReviewofBKWPS','trust1041Trust0005ClearReviewPointsforBK','trust1041Trust0006InputPrep','trust1041Trust0007Review','trust1041Trust0008ClearReviewPointsForTR','trust1041Trust0009FinalReview','trust1041Trust0010PartnerSignoff','trust1041Trust0011BillPrintTRs','trust1041Trust0012Assemble','trust1041Trust0013WaitingforSignature','trust1041Trust0014CloseOutTaxReturn','END','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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