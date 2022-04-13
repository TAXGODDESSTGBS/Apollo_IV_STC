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
from insightly.models import Projectirsnotice
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1knOVxfrhjzEu4LuuTZQrD7Wloo-hmhmdZh4pfZz7Yf8'
SAMPLE_RANGE_NAME = 'A1:AB10000'
HEADERS = (
    'Project ID', 'Project Name','Start Days In P4','IRS Notice 0001 Intakes for IRS notice admin Days In P4', 'IRS Notice 0002 1st Review CPA Level Tax Team Member Days in P4', 'IRS Notice 0003 Clear Review Points Days in P4', 'IRS Notice 0003 2nd Review Manager Level dept Head Days in P4' 'IRS Notice 0004 Mailing Physical Admin - Number of Days in P4', 'IRS Notice 0005 Follow Up Manager Level Department Head - Number of Days in P4','IRS notice 0006 Follow Up Admin - Number of Days in P4','IRS Notice 0007 Follow Up CPA - Days in P4','IRS Notice 0008 Close Out Notice Admin - Days in P4','end - Days in P4','Days in startDays','Days in IRS Notice 0001 Intakes for IRS notice admin', 'Days in IRS Notice 0002 1st Review CPA Level Tax Team Members','Days in IRS Notice 0003 Clear Review Points','Days in IRS notice 0003 2nd Review Manager Level Dept Head','Days in IRS Notice 0004 Mailing Physical Admin','Days in IRS notice 0005 Follow up manager level dept head','Days in IRS Notice 0006 Follow Up Admin days','Days in IRS notice 0007 Follow Up CPA Days','Days in IRS Notice 0008 Close Out Notice Admin','Days in end','Total Number of Days for all Stages','Total Number of P4 Days')
                                                  
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

            project_data = list(Projectirsnotice.objects.values_list('projectirsnotice_id', 'name', 'startP4','irsnotice0001intakesforirsnoticeadminP4','irsnotice00021streviewCPAleveltaxteammemberP4','irsnotice0003clearreviewpointsP4','irsnotice00032ndreviewmanagerleveldeptheadP4','irsnotice0004mailingphysicalazadminP4','irsnotice0005followupmanagerleveldeptheadP4','irsnotice0006followupadminP4','irsnotice0007followupCPAP4','irsnotice0008closeoutnoticeAdminP4','endP4','startDays','irsnotice0001intakesforirsnoticeadmindays', 'irsnotice00021streviewCPAleveltaxteammemberdays','irsnotice0003clearreviewpointsdays','irsnotice00032ndreviewmanagerleveldeptheaddays','irsnotice0004mailingphysicalazadmindays','irsnotice0005followupmanagerleveldeptheaddays','irsnotice0006followupadmindays','irsnotice0007followupCPAdays','irsnotice0008closeoutnoticeAdmindays','enddays','TotalP4DaysPerStage','TotalDaysPerStage'))
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


           

            
