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
from insightly.models import Project1065
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

#Number 38
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1MtmX4dUjk8rDF4VSy99ECKQtXElKTNPvKJ802CZQbA8'
SAMPLE_RANGE_NAME = 'A1:AM10000'
HEADERS = (
    'Project ID','Project Name','Proformad - 1065 - 0001 - Days in P4','Intakes - 1065 - 0002 - Days in P4','Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1065 - 0003 - Days in P4','Final Review of BK WPS - 1065 - 0004 - Days in P4','Clear Review Points for BK WPS - 1065 - 0005 - Days in P4','Input/Prep - 1065 - 0006 - Days in P4','Waiting on K-1 - 1065 - 0007 - Days in P4','Review - 1065 - 0008 - Days in P4','Clear Review Points for TR - 1065 - 0009 - Days in P4','Finalize 1st Review - 1065 - 0010 - Days in P4','Final Review - 1065 - 0011 - Days in P4','Partner Signoff - 1065 - 0012 - Days in P4','Bill/Print/Assembly - 1065 - 0013 - Days in P4','Waiting for Client Signature - 1065 - 0014 - Days in P4','Close Out TR - 1065 - 0015 - Days in P4','Fee Analysis - 1065 - 0016 - Days in P4','Rollover - 1065 - 0017 - Days in P4','Days in - Proformad - 1065 - 0001','Days in - Intakes - 1065 - 0002','Days in - Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1065 - 0003','Days in - Final Review of BK WPS - 1065 - 0004','Days in - Clear Review Points for BK WPS - 1065 - 0005','Days in - Input/Prep - 1065 - 0006','Days in - Waiting on K-1 - 1065 - 0007','Days in - Review - 1065 - 0008','Days in - Clear Review Points for TR - 1065 - 0009','Days in - Finalize 1st Review - 1065 - 0010','Days in - Final Review - 1065 - 0011','Days in - Partner Signoff - 1065 - 0012','Days in - Bill/Print/Assembly - 1065 - 0013','Days in - Waiting for Client Signature - 1065 - 0014','Days in - Close Out TR - 1065 - 0015','Days in - Fee Analysis - 1065 - 0016','Days in - Rollover - 1065 - 0017','Total P4 Days Per Stage','Total Days Per Stage','Turn Around Time')


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

            project_data = list(Project1065.objects.values_list('project1065_id', 'name', 'Proformad10650001P4','Intakes10650002P4','BKPNGRevTRPrintRevPreCompileP4','FinalReviewofBKWPS10650004P4','ClearReviewPointsforBKWPS10650005P4','InputPrep10650006P4','WaitingonK110650007P4','Review10650008P4','ClearReviewPointsforTR10650009P4','Finalize1stReview10650010P4','FinalReview10650011P4','PartnerSignoff10650012P4','BillPrintAssembly10650013P4','WaitingforClientSignature10650014P4','CloseOutTR10650015P4','FeeAnalysis10650016P4','Rollover10650017P4','Proformad10650001','Intakes10650002','BKPNGRevTRPrintRevPreCompile','FinalReviewofBKWPS10650004','ClearReviewPointsforBKWPS10650005','InputPrep10650006','WaitingonK110650007','Review10650008','ClearReviewPointsforTR10650009','Finalize1stReview10650010','FinalReview10650011','PartnerSignoff10650012','BillPrintAssembly10650013','WaitingforClientSignature10650014','CloseOutTR10650015','FeeAnalysis10650016','Rollover10650017','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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