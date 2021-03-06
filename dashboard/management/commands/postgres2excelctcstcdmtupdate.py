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
from insightly.models import Projectctcstcdmtupdate
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
#Number 30

SAMPLE_SPREADSHEET_ID = '12iRJ4jRZTyBeLu1Bpa-qpR3g_M0GtQl8nQnus9McVSo'
SAMPLE_RANGE_NAME = 'A1:AD10000'
HEADERS = ('Project ID','Project Name', 'Start - Days in P4','Billable CTC STC Project 0001 Setup Client Tasks - Days in P4','Billable CTC STC Project 0002 Admin for CTC Plan Prep - Days in P4','Billable CTC STC Project 0003 Create Ideas for Client - Days in P4','Billable CTC STC Project 0005 Input Prep - Days in P4','Billable CTC STC Project 00051 QA with the client - Days in P4','Billable CTC STC Project 0006 Review Project - Days in P4','Billable CTC STC Project 0007 CLRRVW PTS - Days in P4','Billable CTC STC Project 0008 Final Review - Days in P4','Billable CTC STC Project 0009 Assemble CTC Plan - Days in P4','Billable CTC STC Project 0011 Admin Wrap up - Days in P4','End - Days in P4','Start Days','Billable CTC STC Project 0001 Setup Client Tasks Days','Billable CTC STC Project 0002 Admin for CTC Plan Prep Days','Billable CTC STC Project 0003 Create Ideas for Client Days','Billable CTC STC Project 0005 Input Prep Days','Billable CTC STC Project 00051 QA with the client Days','Billable CTC STC Project 0006 Review Project Days','Billable CTC STC Project 0007 CLRRVWPTS Days','Billable CTC STC Project 0008 Final Review Days','Billable CTC STC Project 0009 Assemble CTC Plan Days','Billable CTC STC Project 0011 Admin Wrapup Days','End Days','TotalDaysPerStage','TotalP4DaysPerStage')

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

            project_data = list(Projectctcstcdmtupdate.objects.values_list('projectctcstcdmtupdate_id', 'name', 'startP4', 'billableCTCSTCProject0001SetupClientTasksP4','billableCTCSTCProject0002AdminforCTCPlanPrepP4','billableCTCSTCProject0003CreateIdeasforClientP4','billableCTCSTCProject0005InputPrepP4','billableCTCSTCProject00051QAwiththeclientP4','billableCTCSTCProject0006ReviewProjectP4','billableCTCSTCProject0007CLRRVWPTSP4','billableCTCSTCProject0008FinalReviewP4','billableCTCSTCProject0009AssembleCTCPlanP4','billableCTCSTCProject0011AdminWrapupdays','endP4','startDays','billableCTCSTCProject0001SetupClientTasksdays','billableCTCSTCProject0002AdminforCTCPlanPrepdays','billableCTCSTCProject0003CreateIdeasforClientdays','billableCTCSTCProject0005InputPrepdays','billableCTCSTCProject00051QAwiththeclientdays','billableCTCSTCProject0006ReviewProjectdays','billableCTCSTCProject0007CLRRVWPTSdays','billableCTCSTCProject0008FinalReviewdays','billableCTCSTCProject0009AssembleCTCPlandays','billableCTCSTCProject0011AdminWrapupdays','enddays', 'TotalDaysPerStage', 'TotalP4DaysPerStage'))
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


