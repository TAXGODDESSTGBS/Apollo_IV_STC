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
from insightly.models import Project1120
from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

SAMPLE_SPREADSHEET_ID = '1cnf5eJSQxVftD6rPaIa1C-qR7KgLvQp4vvSEY_X2UbA'
SAMPLE_RANGE_NAME = 'A1:AM10000'
HEADERS = (
    'Project ID','Project Name','Proformad - 1120 - 0001 - Days in P4','intakes - 1120 - 0002 - Days in P4','Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1120 - 0003 - Days in P4','Final Review of BK WPS - 1120 - 0004 - Days in P4','Clear Review Points for Bk - 1120 - 0005 - Days in P4','Input/Prep - 1120 - 0006 - Days in P4','Waiting on k-1 - 1120 - 0007 - Days in P4','Review - 1120 - 0008 - Days in P4','Clear Review Points - 1120 - 0009 - Days in P4','Finalize 1st Review - 1120 - 0010 - Days in P4','Final Review - 1120 - 0011 - Days in P4','Partner Signoff - 1120 - 0012 - Days in P4','Bill/Print & Assembly - 1120 - 0013 - Days in P4','Waiting for Client Signature - 1120 - 0014 - Days in P4','Close Out Tax Return - 1120 - 0015 - Days in P4','Fee Analysis - 1120 - 0016 - Days in P4','Rollover - 1120 - 0017 - Days in P4','Days in - Proformad - 1120 - 0001','Days in - intakes - 1120 - 0002','Days in - Bookkeeping Review for Tax Return (Print, Review, Prepare, Compile) - 1120 - 0003','Days in - Final Review of BK WPS - 1120 - 0004','Days in - Clear Review Points for Bk - 1120 - 0005','Days in - Input/Prep - 1120 - 0006','Days in - Waiting on k-1 - 1120 - 0007','Days in - Review - 1120 - 0008','Days in - Clear Review Points - 1120 - 0009','Days in - Finalize 1st Review - 1120 - 0010','Days in - Final Review - 1120 - 0011','Days in - Partner Signoff - 1120 - 0012','Days in - Bill/Print & Assembly - 1120 - 0013','Days in - Waiting for Client Signature - 1120 - 0014','Days in - Close Out Tax Return - 1120 - 0015','Days in - Fee Analysis - 1120 - 0016','Days in - Rollover - 1120 - 0017','Total P4 Days Per Stage','Total Days Per Stage','Turn Around Time')


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
        for idx, project_obj in enumerate(Project1120.objects.all()):                   
            woi = project_obj.woi
            stage_name = project_obj.stage  
            #'TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'
            total_daysperstage = project_obj.TotalDaysPerStage
            total_daysinP4 = project_obj.TotalP4DaysPerStage
            tat = total_daysperstage - total_daysinP4
            try:            
                credentials = get_credentials()
                service = build('sheets', 'v4', credentials=credentials)
                project_data = list(Project1120.objects.values_list('project1120_id', 'name','Proformad11200001P4','intakes11200002P4','BKPNGRevTRPrintRevPreCompile113P4','FinalReviewofBKWPS11200004P4','ClearReviewPointsforBk11200005P4','InputPrep11200006P4','Waitingonk111200007P4','Review11200008P4','ClearReviewPoints11200009P4','Finalize1stReview11200010P4','FinalReview11200011P4','PartnerSignoff11200012P4','BillPrintAssembly11200013P4','WaitingforClientSignature11200014P4','CloseOutTaxReturn11200015P4','FeeAnalysis11200016P4','Rollover11200017P4','Proformad11200001','intakes11200002','BKPNGRevTRPrintRevPreCompile113','FinalReviewofBKWPS11200004','ClearReviewPointsforBk11200005','InputPrep11200006','Waitingonk111200007','Review11200008','ClearReviewPoints11200009','Finalize1stReview11200010','FinalReview11200011','PartnerSignoff11200012','BillPrintAssembly11200013','WaitingforClientSignature11200014','CloseOutTaxReturn11200015','FeeAnalysis11200016','Rollover11200017','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime'))
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
        #    
        #try:            
        #    credentials = get_credentials()
        #    service = build('sheets', 'v4', credentials=credentials)
        #    project_data = list(Project1120.objects.values_list('project1120_id', 'name','Proformad11200001P4','intakes11200002P4','BKPNGRevTRPrintRevPreCompile113P4','FinalReviewofBKWPS11200004P4','ClearReviewPointsforBk11200005P4','InputPrep11200006P4','Waitingonk111200007P4','Review11200008P4','ClearReviewPoints11200009P4','Finalize1stReview11200010P4','FinalReview11200011P4','PartnerSignoff11200012P4','BillPrintAssembly11200013P4','WaitingforClientSignature11200014P4','CloseOutTaxReturn11200015P4','FeeAnalysis11200016P4','Rollover11200017P4','Proformad11200001','intakes11200002','BKPNGRevTRPrintRevPreCompile113','FinalReviewofBKWPS11200004','ClearReviewPointsforBk11200005','InputPrep11200006','Waitingonk111200007','Review11200008','ClearReviewPoints11200009','Finalize1stReview11200010','FinalReview11200011','PartnerSignoff11200012','BillPrintAssembly11200013','WaitingforClientSignature11200014','CloseOutTaxReturn11200015','FeeAnalysis11200016','Rollover11200017','TotalP4DaysPerStage', 'TotalDaysPerStage', 'TurnAroundTime',tat))
        #    project_data.insert(0, HEADERS)
        #    sheet = service.spreadsheets()
        #    sheet.values().clear(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #                         range=SAMPLE_RANGE_NAME).execute()
        #    response_date = sheet.values().update(
        #        spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #        valueInputOption='RAW',
        #        range=SAMPLE_RANGE_NAME,
        #        body=dict(
        #            majorDimension='ROWS',
        #            values=project_data)
        #    ).execute()
        #    print('Sheet successfully Updated', response_date)
          
        #except Exception as e:
        #    import traceback
        #    traceback.print_exc()
        #    print(e)