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
from insightly.models import Project706estate
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1IgdslIfNzRifVIUMFVmLH3X6Q65Ju6qn6l5nfUtwcB8'
SAMPLE_RANGE_NAME = 'A1:AJ10000'
HEADERS = (
    'Project ID','Project Name','START','706 - 0001 - Proformad - Days in P4','706 - 0002 - Intake Process - Days in P4','706 - 0003 - Bookkeeping Review - TR - Days in P4','706 - 0004 - Final Review of BK WPS - Days in P4','706 - 0005 - Clear Review Points for BK - Days in P4','706 - 0006 - Input/Prep - Days in P4','706 - 0007 - Review - Days in P4','706 - 0008 - Clear Review Points For TR - Days in P4','706 - 0009 - Final Review - Days in P4','706 - 0010 - Partner Signoff - Days in P4','706 - 0011 - Bill/Print (TRs) - Days in P4','706 - 0012 - Assemble - Days in P4','706 - 0013 - Waiting for Signature - Days in P4','706 - 0014 - Close Out Tax Return - Days in P4','END - Days in P4', 'Days in - START','Days in - 706 - 0001 - Proformad','Days in - 706 - 0002 - Intake Process','Days in - 706 - 0003 - Bookkeeping Review - TR','Days in - 706 - 0004 - Final Review of BK WPS','Days in - 706 - 0005 - Clear Review Points for BK','Days in - 706 - 0006 - Input/Prep','Days in - 706 - 0007 - Review','Days in - 706 - 0008 - Clear Review Points For TR','Days in - 706 - 0009 - Final Review','Days in - 706 - 0010 - Partner Signoff','Days in - 706 - 0011 - Bill/Print (TRs)','Days in - 706 - 0012 - Assemble','Days in - 706 - 0013 - Waiting for Signature','Days in - 706 - 0014 - Close Out Tax Return','Days in - END','Total Days Per Stage','Turn Around Time')

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

            project_data = list(Project706estate.objects.values_list('project706estate_id', 'name', 'STARTP4','e7060001ProformadP4','e7060002IntakeProcessP4','e7060003BookkeepingReviewTRP4','e7060004FinalReviewofBKWPSP4','e7060005ClearReviewPointsforBKP4','e7060006InputPrepP4','e7060007ReviewP4','e7060008ClearReviewPointsForTRP4','e7060009FinalReviewP4','e7060010PartnerSignoffP4','e7060011BillPrintTRsP4','e7060012AssembleP4','e7060013WaitingforSignatureP4','e7060014CloseOutTaxReturnP4','ENDP4','START','e7060001Proformad','e7060002IntakeProcess','e7060003BookkeepingReviewTR','e7060004FinalReviewofBKWPS','e7060005ClearReviewPointsforBK','e7060006InputPrep','e7060007Review','e7060008ClearReviewPointsForTR','e7060009FinalReview','e7060010PartnerSignoff','e7060011BillPrintTRs','e7060012Assemble','e7060013WaitingforSignature','e7060014CloseOutTaxReturn','END','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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