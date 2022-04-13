from django.core.management.base import BaseCommand, CommandError
from django.core.exceptions import ObjectDoesNotExist, MultipleObjectsReturned
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from insightly.models import Project, Stage, UserModel, Pipeline
import json
from datetime import datetime
from pprint import pprint
from django.http import HttpResponse
from psycopg2.extras import RealDictCursor
from requests.models import Response
from unittest.mock import Mock
from itertools import count


class Command(BaseCommand):
    help = 'PostgreSQL to Slack'

    projnumber = 1

    def handle(self, *args, **options):
        woi_counter = 0
        intake_counter = 0
        projec_counter = 0
        projectnumbering_counter = 0
        projectnumbering1_counter = 0

        woi_messages = "All Other projects that need to be done, but are either (WOI - True) or in Intakes, in no particular order.\n"
        intake_messages = "Must be done by 10/15 - Out of intakes by Deadline(in order of out of intakes(OOI))\n"
        
        for idx, project_obj in enumerate(Project.objects.all()):                   
            woi = project_obj.woi
            stage_name = project_obj.stage            
            #ProjProfileFilter = project_obj.ProjProfileFilter
            user_name = project_obj.user_responsible
            project_status = project_obj.project_status
            projectstatuscancelled = project_obj.projectstatuscancelled
            projectstatuscompleted = project_obj.projectstatuscompleted

            TotalKPIProjects = 0
            if not projectstatuscancelled and not projectstatuscompleted:     
                TotalKPIProjects +=1   
                message = "*{name}* - *{stage_name}* - *{user_name}* - *{project_status}* - *{TurnAround_Time}* ".format(
                    name=project_obj.name,
                    stage_name=project_obj.stage,   
                    user_name = project_obj.user_responsible,
                    project_status = project_obj.project_status,
                    TotalDaysPer_stage = project_obj.TotalDaysPerStage,
                    TotalP4DaysPer_stage = project_obj.TotalP4DaysPerStage,
                    TurnAround_Time = project_obj.TurnAroundTime
                )
                intake_messages += message + "\n"   

        intake_list = intake_messages.split("\n")[1:-1]
        intake_list_str = "\n".join(intake_list)
        intake_list_str = "PROJECT NAME - TURN AROUND TIME - DMT\n" + intake_list_str
       
        all_messages = intake_list_str + "\n\n" + intake_messages  
        all_messages = intake_list_str + "\n\n"
        client = WebClient(token="xoxp-3872107291-218743594772-1769657010758-70b7b68f1007b088cd32f6f61325ae51")

        try:
            response = client.chat_postMessage(channel='#reports_bookkeeping-special-projects', text=all_messages)
            
        except SlackApiError as e:
            assert e.response["ok"] is False
            assert e.response["error"]  # str like 'invalid_auth', 'channel_not_found'
            raise CommandError(f"Got an error: {e.response['error']}")

        self.stdout.write(self.style.SUCCESS("Successfully sent message to slack"))




