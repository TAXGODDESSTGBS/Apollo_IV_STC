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
    'Project ID','Days in P4 - START','Days in P4 - 1041 Estate Income - 0001 - Proforma’d','Days in P4 - 1041 Estate Income - 0002 - Intake Process','Days in P4 - Estate Income - 0003 - Bookkeeping Review - TR','Days in P4 - 1041 Estate Income - 0004 - Final Review of BK WPS','Days in P4 - 1041 Estate Income - 0005 - Clear Review Points for BK','Days in P4 - 1041 Estate Income - 0006 - Input/Prep','Days in P4 - 1041 Estate Income - 0007 - Review','Days in P4 - 1041 Estate Income - 0008 - Clear Review Points For TR','Days in P4 - Estate Income - 0009 - Final Review','Days in P4 - Estate Income - 0010 - Partner Signoff','Days in P4 - 1041 Estate Income - 0012 - Assemble','Days in P4 - 1041Estate Income - 0013 - Waiting for Signature','Days in P4 - 1041 Estate Income - 0014 - Close Out Tax Return','Days in P4 - END','Days in - START','Days in - 1041 Estate Income - 0001 - Proforma’d','Days in - 1041 Estate Income - 0002 - Intake Process','Days in - Estate Income - 0003 - Bookkeeping Review - TR','Days in - 1041 Estate Income - 0004 - Final Review of BK WPS','Days in - 1041 Estate Income - 0005 - Clear Review Points for BK','Days in - 1041 Estate Income - 0006 - Input/Prep','Days in - 1041 Estate Income - 0007 - Review','Days in - 1041 Estate Income - 0008 - Clear Review Points For TR ','Days in - Estate Income - 0009 - Final Review','Days in - Estate Income - 0010 - Partner Signoff','Days in - 1041 Estate Income - 0012 - Assemble','Days in - 1041Estate Income - 0013 - Waiting for Signature','Days in - 1041 Estate Income - 0014 - Close Out Tax Return','Days in - END',' Total P4 Days Per Stage', 'Total Days Per Stage', 'Turn Around Time')

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

            project_data = list(Project.objects.values_list('project_id', 'name', 'STARTP4','estateincome1041EstateIncome0001ProformadP4','estateincome1041EstateIncome0002IntakeProcessP4','EstateIncome0003BookkeepingReviewTRP4','estateincome1041EstateIncome0004FinalReviewofBKWPSP4','estateincome1041EstateIncome0005ClearReviewPointsforBKP4','estateincome1041EstateIncome0006InputPrepP4','estateincome1041EstateIncome0007ReviewP4','estateincome1041EstateIncome0008ClearReviewPointsForTRP4','EstateIncome0009FinalReviewP4','EstateIncome0010PartnerSignoffP4','estateincome1041EstateIncome0012AssembleP4','estateincome1041EstateIncome0013WaitingforSignatureP4','estateincome1041EstateIncome0014CloseOutTaxReturnP4','ENDP4','START','estateincome1041EstateIncome0001Proformad','estateincome1041EstateIncome0002IntakeProcess','EstateIncome0003BookkeepingReviewTR','estateincome1041EstateIncome0004FinalReviewofBKWPS','estateincome1041EstateIncome0005ClearReviewPointsforBK','estateincome1041EstateIncome0006InputPrep','estateincome1041EstateIncome0007Review','estateincome1041EstateIncome0008ClearReviewPointsForTR','EstateIncome0009FinalReview','EstateIncome0010PartnerSignoff','estateincome1041EstateIncome0012Assemble','estateincome1041EstateIncome0013WaitingforSignature','estateincome1041EstateIncome0014CloseOutTaxReturn','END','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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