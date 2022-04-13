from contextlib import AbstractContextManager
import requests
import base64
import json
import datetime
from django.core.serializers.json import DjangoJSONEncoder


def default(o):
    if isinstance(o, (datetime.date, datetime.datetime)):
        return o.isoformat()


class Session(AbstractContextManager):
    API_BASE_URL = 'https://api.na1.insightly.com/v3.1/'

    def __init__(self, API_KEY):
        self.session = requests.Session()
        self.token = base64.b64encode(API_KEY.encode("ascii")).decode("ascii")

    def __exit__(self, exc_type, exc, tb):
        self.session.close()

    def basic_auth(self, api_key):
        # Login equals to API Key with an empty password as per
        # Insightly API documentation.
        login = self.token
        password = ''
        return requests.auth.HTTPBasicAuth(login, password)

    def url(self, uri):
        return f'{self.API_BASE_URL}{uri}'

    def get(self, uri, params=None):
        return self.session.get(uri, headers={
            'Authorization': f'Basic {self.token}'})

    def post(self, uri, json=None):
        return self.session.post(uri, json=json, headers={
            'Authorization': f'Basic {self.token}'})

    def put(self, uri, json=None):
        return self.session.put(uri, json=json, headers={
            'Authorization': f'Basic {self.token}'})

    def delete(self, uri):
        return self.session.request('DELETE', self.url(uri), headers={
            'Authorization': f'Basic {self.token}'})

    def get_contacts(self):
        return self.get(self.url('contacts/'))

    def get_categories(self):
        return self.get(self.url(f'opportunitycategories/'))

    def get_opportunities(self):
        return self.get(self.url('opportunities/'))

    def get_projects(self):
        return self.get(self.url('Projects'))

    def get_pipelines(self):
        return self.get(self.url('Pipelines'))

    def get_pipeline_stages(self):
        return self.get(self.url('/PipelineStages/'))

    def get_pipeline_stage(self, id):
        return self.get(self.url(f'/PipelineStages/{id}'))

    def get_project_categories(self):
        return self.get(self.url('ProjectCategories'))

    def get_activity_sets(self):
        return self.get(self.url(f'/ActivitySets/'))

    def get_tasks(self, opp_id):
        return self.get(self.url(f'Tasks/Search?field_name=OPPORTUNITY_ID&field_value={opp_id}'))

    def get_current_user(self):
        return self.get(self.url(f"Users/Me"))

    def get_activites_from_activityset(self, activityset_id):
        return self.get(self.url(f"ActivitySets/{activityset_id}")).json()["ACTIVITIES"]

    def fetch_activity_id_from_list(self, activities):
        id_list = []
        for activity in activities:
            id_list.append(activity["ACTIVITY_ID"])
        return id_list

    def generate_activity_list(self, id_list, user_id):
        act_list = []
        for act_id in id_list:
            extra = {
                "ACTIVITY_ID": act_id,
                "RESPONSIBLE_USER_ID": user_id,
            }
            act_list.append(extra)
        return act_list

    def update_pipeline_opportunitiy(self, opp_id, pipeline_id, stage_id):
        data = {
            "PIPELINE_ID": pipeline_id,
            "PIPELINE_STAGE_CHANGE": {
                "STAGE_ID": stage_id,
            }
        }
        return self.put(self.url(f'opportunities/{opp_id}/pipeline'), data)

    def complete_task(self, task_id):
        data = {
            "TASK_ID": task_id,
            "COMPLETED": True,
            "PERCENT_COMPLETE": 100,
            "STATUS": "COMPLETED",
        }
        return self.put(self.url(f'Tasks/'), data)

    def update_stage_activity(self, stage_id, activity_id):
        data = {
            "STAGE_ID": stage_id,
            "ACTIVITYSET_ID": activity_id,
        }
        return self.put(self.url(f'PipelineStages/3751468/'), data)

    def add_activity2_opportunity(self, opp_id: int, pipeline_id: int, stage_id: int, activityset_id: int,
                                  activites: list, ):
        data = {
            "PIPELINE_ID": pipeline_id,
            "PIPELINE_STAGE_CHANGE": {
                "STAGE_ID": stage_id,
                "ACTIVITYSET_ASSIGNMENT": {
                    "ACTIVITYSET_ID": activityset_id,
                    "START_DATE": "2020-10-17T11:57:39.591Z",
                    "END_DATE": "2020-10-17T11:57:39.591Z",
                    "ACTIVITY_ASSIGNMENTS": activites
                }

            }
        }
        return self.put(self.url(f"opportunities/{opp_id}/Pipeline"), data)

    def fetch_pipeline_stages(self, pipeline_id):
        pip_list = []
        for i in self.get_pipeline_stages().json():
            if i['PIPELINE_ID'] == pipeline_id:
                pip_list.append(i)
        return pip_list