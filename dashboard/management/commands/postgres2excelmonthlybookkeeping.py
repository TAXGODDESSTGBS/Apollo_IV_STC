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
from insightly.models import Projectmonthlybookkeeping
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1j7zGmdtI98JrZU8LU6AigTWCtaXKuw7RVow64rLwTv4'
SAMPLE_RANGE_NAME = 'A1:AA10000'
HEADERS = (
    'Project ID', 'Project Name','Setup - Number of Days In P4', 'Monthly Bookkeeping Input Reconcile - Number of Days In P4','Monthly BK 0002 Self Review Print WPS - Number of Days In P4', 'Monthly Bookkeeping 0003 Review WPS - Number of Days in P4', 'Monthly BKP 0004 Clear Review Points - Number of Days In P4', 'Monthly BK 0005 Final Review - Number of Days in P4', 'Monthly BK 0006 Books Done but WOI from Client - Number of Days in P4','Monthly BKP 0006 1 Review with Client Additional Answers - Number of Days in P4','Monthly BKP 0006 Final CPA sign off send to client - Days in P4','End - Days in P4','User Responsible ID','Days in Sestup', 'Days in Monthly Bookkeeping 0001 Input Reconcile', 'Days in Monthly BK 0002 Self Review Print WPS','Days in Monthly BK 0003 Review WPS', 'Days in Monthly BK 0004 Clear Review Points','Days in Monthly BK 0005 Final Review', 'Days in Monthly BK 0006 Books Done but WOI drom Client', 'Days in Monthly BK 0006 Review with the Clients Additional Answers', 'Days in BK 0006 Final CPA sign off send to client','Days in BK End','Total Number of Days for all Stages','Total Number of P4 Days', 'Turn Around Time')
                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                       
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

            project_data = list(Projectmonthlybookkeeping.objects.values_list('projectmonthlybookkeeping_id', 'name', 'SetupP4','MonthlyBKP0001InputReconcileP4', 
                                                        'MonthlyBKP0002SelfReviewPrintWPSP4','MonthlyBKP0003ReviewWPSP4','MonthlyBKP0004ClearReviewPointsP4','MonthlyBKP0005FinalReviewP4','MonthlyBKP00060BooksDonebutWOIfromClientP4','MonthlyBKP00061RereviewwithclientsadditionalanswersP4','MonthlyBKP0006FinalCPAsignoffsendtoclientP4','MonthlyBKPENDP4','user_responsible_id', 'SetupDays','MonthlyBKP0001InputReconciledays','MonthlyBKP0002SelfReviewPrintWPSdays','MonthlyBKP0003ReviewWPSdays','MonthlyBKP0004ClearReviewPointsdays','MonthlyBKP0005FinalReviewdays','MonthlyBKP00060BooksDonebutWOIfromClientdays','MonthlyBKP00061Rereviewwithclientsadditionalanswersdays','MonthlyBKP0006FinalCPAsignoffsendtoclientdays','MonthlyBKPENDdays','TotalDaysPerStage', 'TotalP4DaysPerStage', 'TurnAroundTime'))
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





