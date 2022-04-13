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
from insightly.models import Projectmonthlyperiodic
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1s5Km88q0nXUki_KTe2nnQY1fP7GKgz6Rj4pRbzT8Vks'
SAMPLE_RANGE_NAME = 'A1:AA10000'
HEADERS = (
    'Project ID', 'Project Name','Start Days in P4','Profit Cents Monthly Reports 0001 Input Prep days in P4','Profit Cents Monthly Reports 0002 Review Days in P4','Profit Cents Monthly Reports 0003 Clear Review Points Days in P4','End Days in P4', 'USER Responsible ID', 'Start Days','Profit Cents Monthly Reports 0001 Input Prep Days','Profit Cents Monthly Reports 0002 Review Days','Profit Cents Monthly Reports 0003 Clear Review Points Days', 'End Days', 'Total Days Per Stage', 'Total P4 Days Per Stage', 'Turn Around Time')

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


#class Command(BaseCommand):

#    def handle(self, *args, **options):
        #if Project.stage == 3235444 or Project.stage == 3235445 or Project.stage == 3235492 or Project.stage == 3235494 or Project.stage == 3235508:
#        try:
#            credentials = get_credentials()
#            service = build('sheets', 'v4', credentials=credentials)

#            project_data = list(Project.objects.values_list('project_id', 'name', 'IntakesP4', 'BookkeepingReviewforTaxReturnP4',
#                                                       'InputPrepP4', 'ReviewP4', 'BillPrinTRsAssemblyP4', 'IntakesStageDays', 'BookkeepingReviewforTaxReturnDays', 'InputPrepDays', 'ReviewDays', 'BillPrinTRsAssemblyDays', 'TotalDaysPerStage', 'TotalP4DaysPerStage'))
#            project_data.insert(0, HEADERS)
#            sheet = service.spreadsheets()
#            sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                                    range=SAMPLE_RANGE_NAME).execute()
#                response_date = sheet.values().update(
#                    spreadsheetId=SAMPLE_SPREADSHEET_ID,
#                    valueInputOption='RAW',
#                    range=SAMPLE_RANGE_NAME,
#                    body=dict(
#                        majorDimension='ROWS',
#                        values=project_data)
#                ).execute()
#                print('Sheet successfully Updated', response_date)

#            except Exception as e:
#                import traceback
#                traceback.print_exc()
#                print(e)

class Command(BaseCommand):

    def handle(self, *args, **options):
        #for idx, project_obj in enumerate(Project.objects.all()):
        #    fields = project_obj.allprojectcustomfieldsOOI                       
        #    woi = project_obj.woi
        #    stage_name = project_obj.stage            
        #    ProjProfileFilter = project_obj.ProjProfileFilter
        #    user_name = project_obj.user_responsible
        #    project_status = project_obj.project_status

        #    filtered_list = []

        #    for item in fields:

        #        try:    
        #            item = json.loads(json.dumps(item))
        #            print(item)    

        #        except Exception as e:
        #            raise CommandError(f"Invalid data given: {e}")
        #        date_value = item.get("FIELD_VALUE")

        #        try:
        #            datetime_obj = datetime.fromisoformat(date_value)
        #            new_item = item
        #            new_item["FIELD_VALUE"] = datetime_obj
        #            filtered_list.append(item)

        #        except Exception as e:
        #            print("Invalid datetime object")
        #            continue

        #    sorted_by_date = sorted(filtered_list, key=lambda k: k["FIELD_VALUE"])

        #    for item in sorted_by_date:
        #        item.get("FIELD_VALUE")
        #        pprint(sorted_by_date)

        #        ooi_date = ""

        #    for item in sorted_by_date:
        #        if item["FIELD_NAME"] == "PROJECT_FIELD_1":
        #            ooi_date = str(item["FIELD_VALUE"])
        #            break

        #        if not ooi_date:
        #            ooi_date = "Date not available"
        #end here            
        #        try:            
        #            credentials = get_credentials()
        #            service = build('sheets', 'v4', credentials=credentials)

        #            project_data = list(Project.objects.values_list('project_id', 'name', 'BookkeepingReviewforTaxReturnP4',
        #                                                        'InputPrepP4', 'ReviewP4', 'BookkeepingReviewforTaxReturnDays', 'InputPrepDays', 'ReviewDays', 'pipeline_id', 'TotalDaysPerStage', 'TotalP4DaysPerStage', 'TurnAroundTime')) and ooi_date
            #if not Project.ProjProfileFilter:
        #            project_data.insert(0, HEADERS)
        #            sheet = service.spreadsheets()
        #            sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #                                 range=SAMPLE_RANGE_NAME).execute()
        #            response_date = sheet.values().update(
        #                spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #                valueInputOption='RAW',
        #                range=SAMPLE_RANGE_NAME,
        #                body=dict(
        #                    majorDimension='ROWS',
        #                    values=project_data)
        #            ).execute()
        #            print('Sheet successfully Updated', response_date)
          
        #        except Exception as e:
        #            import traceback
        #            traceback.print_exc()
        #            print(e)

        try:            
            credentials = get_credentials()
            service = build('sheets', 'v4', credentials=credentials)

            project_data = list(Projectmonthlyperiodic.objects.values_list('projectmonthlyperiodic_id', 'name', 'startP4','profitCentsMonthlyReports0001InputPrepP4','profitCentsMonthlyReports0002ReviewP4','profitCentsMonthlyReports0003ClearReviewPointsP4','endP4', 'user_responsible_id', 'startDays','profitCentsMonthlyReports0001InputPrepdays','profitCentsMonthlyReports0002Reviewdays','profitCentsMonthlyReports0003ClearReviewPointsdays', 'enddays', 'TotalDaysPerStage', 'TotalP4DaysPerStage', 'TurnAroundTime'))
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


